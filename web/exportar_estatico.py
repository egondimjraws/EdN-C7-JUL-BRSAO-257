"""
Gera a versão estática da interface web na pasta docs/, para publicar no GitHub Pages.

Lê o banco aws_simulados.db (somente leitura) e cria:
    docs/index.html     -> cópia de web/static/index.html em modo estático
    docs/questoes.json  -> questões, alternativas, gabarito e explicações
    docs/.nojekyll      -> faz o GitHub Pages publicar os arquivos como estão

Uso (na pasta do projeto):
    python3 web/exportar_estatico.py

Rode de novo sempre que o banco for regenerado com gerar_banco.py.
"""

import json
import os
import sqlite3
import sys

PASTA_WEB = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(PASTA_WEB)
CAMINHO_BANCO = os.path.join(RAIZ, "aws_simulados.db")
PAGINA_ORIGEM = os.path.join(PASTA_WEB, "static", "index.html")
PASTA_DESTINO = os.path.join(RAIZ, "docs")

TOTAL_QUESTOES_EXAME = 64
TEMPO_EXAME_SEGUNDOS = 90 * 60


def exportar_questoes():
    uri = "file:" + CAMINHO_BANCO.replace("\\", "/") + "?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT q.id, q.question_text, q.explanation, c.name
        FROM questions q
        JOIN exam_categories c ON q.category_id = c.id
        ORDER BY q.id;
        """
    )
    questoes = []
    for id_q, texto, explicacao, categoria in cur.fetchall():
        alts = conn.execute(
            "SELECT id, alternative_text, is_correct FROM alternatives WHERE question_id = ? ORDER BY id;",
            (id_q,),
        ).fetchall()
        corretas = [a_id for a_id, _, ok in alts if ok == 1]
        if len(alts) != 4 or len(corretas) != 1:
            sys.exit(f"Erro: a questão {id_q} precisa ter 4 alternativas e exatamente 1 correta.")
        questoes.append(
            {
                "id": id_q,
                "texto": texto,
                "categoria": categoria,
                "explicacao": explicacao,
                "alternativas": [{"id": a_id, "texto": a_txt} for a_id, a_txt, _ in alts],
                "correta_id": corretas[0],
            }
        )
    conn.close()
    return questoes


def main():
    if not os.path.exists(CAMINHO_BANCO):
        sys.exit("Erro: 'aws_simulados.db' não encontrado. Execute 'python3 gerar_banco.py' primeiro.")

    questoes = exportar_questoes()
    os.makedirs(PASTA_DESTINO, exist_ok=True)

    dados = {"total_exame": TOTAL_QUESTOES_EXAME, "tempo_limite": TEMPO_EXAME_SEGUNDOS, "questoes": questoes}
    with open(os.path.join(PASTA_DESTINO, "questoes.json"), "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, separators=(",", ":"))

    pagina = open(PAGINA_ORIGEM, encoding="utf-8").read()
    marcador = '<html lang="pt-BR">'
    if pagina.count(marcador) != 1:
        sys.exit("Erro: não encontrei a tag <html lang=\"pt-BR\"> em web/static/index.html.")
    pagina = pagina.replace(marcador, '<html lang="pt-BR" data-modo="estatico">')
    with open(os.path.join(PASTA_DESTINO, "index.html"), "w", encoding="utf-8") as f:
        f.write(pagina)

    open(os.path.join(PASTA_DESTINO, ".nojekyll"), "w").close()

    tamanho = os.path.getsize(os.path.join(PASTA_DESTINO, "questoes.json")) / 1024
    print(f"Versão estática gerada em docs/ com {len(questoes)} questões (questoes.json: {tamanho:.0f} KB).")


if __name__ == "__main__":
    main()
