"""
Interface web para os simulados AWS Cloud Practitioner (CLF-C02).

Usa apenas a biblioteca padrão do Python e lê o mesmo banco
`aws_simulados.db` (em modo somente leitura) usado pelos scripts de terminal.

Uso:
    python3 web/servidor_web.py            # abre em http://127.0.0.1:8000
    python3 web/servidor_web.py --porta 8080
"""

import argparse
import json
import os
import sqlite3
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

PASTA_WEB = os.path.dirname(os.path.abspath(__file__))
PASTA_STATIC = os.path.join(PASTA_WEB, "static")
CAMINHO_BANCO = os.path.join(os.path.dirname(PASTA_WEB), "aws_simulados.db")

TOTAL_QUESTOES_EXAME = 64
TEMPO_EXAME_SEGUNDOS = 90 * 60


def conectar():
    """Abre o banco em modo somente leitura (não altera os dados existentes)."""
    uri = "file:" + CAMINHO_BANCO.replace("\\", "/") + "?mode=ro"
    return sqlite3.connect(uri, uri=True)


def buscar_questoes(conn, limite):
    """Sorteia questões e devolve sem indicar qual alternativa é a correta."""
    cur = conn.cursor()
    cur.execute(
        """
        SELECT q.id, q.question_text, c.name
        FROM questions q
        JOIN exam_categories c ON q.category_id = c.id
        ORDER BY RANDOM()
        LIMIT ?;
        """,
        (limite,),
    )
    questoes = []
    for id_q, texto, categoria in cur.fetchall():
        cur2 = conn.cursor()
        cur2.execute(
            "SELECT id, alternative_text FROM alternatives WHERE question_id = ? ORDER BY id;",
            (id_q,),
        )
        alternativas = [{"id": a_id, "texto": a_txt} for a_id, a_txt in cur2.fetchall()]
        questoes.append(
            {"id": id_q, "texto": texto, "categoria": categoria, "alternativas": alternativas}
        )
    return questoes


def gabarito(conn, id_questao):
    """Retorna (id da alternativa correta, explicação, categoria) de uma questão."""
    cur = conn.cursor()
    cur.execute(
        """
        SELECT q.explanation, c.name,
               (SELECT a.id FROM alternatives a WHERE a.question_id = q.id AND a.is_correct = 1)
        FROM questions q
        JOIN exam_categories c ON q.category_id = c.id
        WHERE q.id = ?;
        """,
        (id_questao,),
    )
    linha = cur.fetchone()
    if not linha:
        return None
    explicacao, categoria, id_correta = linha
    return id_correta, explicacao, categoria


def corrigir_exame(conn, respostas, tempo_gasto):
    """Mesma regra do exame_oficial.py: nota = 100 + percentual * 9."""
    acertos = 0
    por_dominio = {}
    detalhes = []
    for item in respostas:
        g = gabarito(conn, int(item.get("questao_id", 0)))
        if not g:
            continue
        id_correta, explicacao, categoria = g
        escolhida = item.get("alternativa_id")
        acertou = escolhida is not None and int(escolhida) == id_correta
        dom = por_dominio.setdefault(categoria, {"total": 0, "acertos": 0})
        dom["total"] += 1
        if acertou:
            acertos += 1
            dom["acertos"] += 1
        detalhes.append(
            {
                "questao_id": int(item["questao_id"]),
                "alternativa_id": escolhida,
                "correta_id": id_correta,
                "acertou": acertou,
                "explicacao": explicacao,
            }
        )

    respondidas = sum(1 for r in respostas if r.get("alternativa_id") is not None)
    percentual = acertos / TOTAL_QUESTOES_EXAME * 100
    nota = 100 + int(percentual * 9)
    return {
        "total": TOTAL_QUESTOES_EXAME,
        "respondidas": respondidas,
        "acertos": acertos,
        "erros": TOTAL_QUESTOES_EXAME - acertos,
        "percentual": round(percentual, 2),
        "nota": nota,
        "aprovado": nota >= 700,
        "tempo_gasto": min(int(tempo_gasto), TEMPO_EXAME_SEGUNDOS),
        "por_dominio": [
            {"dominio": k, **v} for k, v in sorted(por_dominio.items())
        ],
        "detalhes": detalhes,
    }


class Manipulador(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PASTA_STATIC, **kwargs)

    def log_message(self, formato, *args):
        pass  # mantém o terminal limpo

    def enviar_json(self, dados, status=200):
        corpo = json.dumps(dados, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(corpo)

    def ler_json(self):
        tamanho = int(self.headers.get("Content-Length", 0) or 0)
        if tamanho <= 0 or tamanho > 1_000_000:
            return {}
        try:
            return json.loads(self.rfile.read(tamanho).decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            return {}

    def do_GET(self):
        caminho = urlparse(self.path).path
        if caminho == "/api/questao":
            with conectar() as conn:
                q = buscar_questoes(conn, 1)
            return self.enviar_json(q[0] if q else {"erro": "Nenhuma questão no banco."}, 200 if q else 404)
        if caminho == "/api/exame":
            with conectar() as conn:
                q = buscar_questoes(conn, TOTAL_QUESTOES_EXAME)
            if len(q) < TOTAL_QUESTOES_EXAME:
                return self.enviar_json(
                    {"erro": f"O banco possui apenas {len(q)} questões; são necessárias {TOTAL_QUESTOES_EXAME}."},
                    409,
                )
            return self.enviar_json(
                {"questoes": q, "tempo_limite": TEMPO_EXAME_SEGUNDOS}
            )
        if caminho.startswith("/api/"):
            return self.enviar_json({"erro": "Rota não encontrada."}, 404)
        return super().do_GET()

    def do_POST(self):
        caminho = urlparse(self.path).path
        dados = self.ler_json()
        try:
            if caminho == "/api/responder":
                with conectar() as conn:
                    g = gabarito(conn, int(dados.get("questao_id", 0)))
                if not g:
                    return self.enviar_json({"erro": "Questão não encontrada."}, 404)
                id_correta, explicacao, _ = g
                return self.enviar_json(
                    {
                        "acertou": int(dados.get("alternativa_id", 0)) == id_correta,
                        "correta_id": id_correta,
                        "explicacao": explicacao,
                    }
                )
            if caminho == "/api/corrigir":
                respostas = dados.get("respostas") or []
                with conectar() as conn:
                    resultado = corrigir_exame(conn, respostas, float(dados.get("tempo_gasto", 0)))
                return self.enviar_json(resultado)
        except (TypeError, ValueError):
            return self.enviar_json({"erro": "Dados inválidos."}, 400)
        return self.enviar_json({"erro": "Rota não encontrada."}, 404)


def main():
    parser = argparse.ArgumentParser(description="Interface web dos simulados AWS CLF-C02")
    parser.add_argument("--porta", type=int, default=8000)
    parser.add_argument("--sem-navegador", action="store_true", help="não abrir o navegador automaticamente")
    args = parser.parse_args()

    if not os.path.exists(CAMINHO_BANCO):
        print("Erro: o arquivo 'aws_simulados.db' não foi encontrado.")
        print("Execute 'python3 gerar_banco.py' na pasta do projeto primeiro.")
        sys.exit(1)

    servidor = ThreadingHTTPServer(("127.0.0.1", args.porta), Manipulador)
    url = f"http://127.0.0.1:{args.porta}"
    print("=" * 60)
    print(" Simulados AWS CLF-C02 - Interface Web")
    print(f" Acesse: {url}")
    print(" Pressione CTRL+C para encerrar.")
    print("=" * 60)
    if not args.sem_navegador:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado. Bons estudos!")
    finally:
        servidor.server_close()


if __name__ == "__main__":
    main()
