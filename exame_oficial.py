import sqlite3
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def formatar_tempo(segundos_restantes):
    if segundos_restantes <= 0:
        return "TEMPO ESGOTADO"
    minutos = int(segundos_restantes // 60)
    segundos = int(segundos_restantes % 60)
    return f"{minutos:02d}:{segundos:02d}"

def rodar_exame():
    if not os.path.exists("aws_simulados.db"):
        print("Erro: O arquivo 'aws_simulados.db' não foi encontrado nesta pasta.")
        print("Execute o script 'gerar_banco.py' primeiro para estruturar os dados.")
        return

    limpar_tela()
    print("=" * 80)
    print("         CONEXÃO ESTABELECIDA - EXAME AWS CERTIFIED CLOUD PRACTITIONER       ")
    print("=" * 80)
    
    nome_usuario = input("\n👉 Por favor, insira o seu nome para iniciar o exame: ").strip()
    if not nome_usuario:
        nome_usuario = "Candidato(a)"

    limpar_tela()
    print("=" * 80)
    print(f"Olá, {nome_usuario}! Prepare-se para o seu Simulado Oficial.")
    print("-" * 80)
    print("📋 REGRAS E INSTRUÇÕES:")
    print("• Quantidade: 64 questões sorteadas aleatoriamente.")
    print("• Tempo Limite: 90 minutos.")
    print("• Critério de Aprovação: Mínimo de 70% de acertos (Nota 700/1000).")
    print("• O tempo continuará correndo enquanto você lê as perguntas!")
    print("=" * 80)
    input("\nPressione ENTER quando estiver pronto para iniciar o cronômetro...")

    conn = sqlite3.connect("aws_simulados.db")
    cursor = conn.cursor()

    # Sorteia exatamente 64 questões do banco de dados
    cursor.execute("""
        SELECT q.id, q.question_text, q.explanation, c.name 
        FROM questions q
        JOIN exam_categories c ON q.category_id = c.id
        ORDER BY RANDOM() 
        LIMIT 64;
    """)
    questoes = cursor.fetchall()

    if len(questoes) < 64:
        print(f"\n⚠️ Alerta: Seu banco possui apenas {len(questoes)} questões. Preencha o banco para rodar com 64.")
        conn.close()
        return

    total_questoes = 64
    acertos = 0
    erros = 0
    tempo_limite_segundos = 90 * 60
    tempo_inicio = time.time()

    # Dicionário para armazenar o desempenho por categoria
    desempenho_categorias = {}

    for idx, questao in enumerate(questoes, start=1):
        id_pergunta, texto_pergunta, explicacao, nome_categoria = questao

        # Inicializa a categoria no relatório se não existir
        if nome_categoria not in desempenho_categorias:
            desempenho_categorias[nome_categoria] = {"total": 0, "acertos": 0}
        desempenho_categorias[nome_categoria]["total"] += 1

        # Controle de tempo dinâmico
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicio
        tempo_restante = tempo_limite_segundos - tempo_decorrido

        if tempo_restante <= 0:
            limpar_tela()
            print("\n" + "!" * 80)
            print("🚨 ATENÇÃO: O TEMPO LIMITE DE 90 MINUTOS FOI ESGOTADO!")
            print("O exame foi encerrado automaticamente. Computando respostas respondidas...")
            print("!" * 80)
            time.sleep(3)
            break

        limpar_tela()
        print("=" * 80)
        print(f" QUESTÃO {idx} de {total_questoes}   |   ⏱️ TEMPO RESTANTE: {formatar_tempo(tempo_restante)}")
        print("=" * 80)
        print(f"📂 {nome_categoria}")
        print(f"\n❓ {texto_pergunta}\n")

        # Busca as alternativas da pergunta atual
        cursor.execute("""
            SELECT id, alternative_text, is_correct 
            FROM alternatives 
            WHERE question_id = ?;
        """, (id_pergunta,))
        alternativas = cursor.fetchall()

        letras = ['A', 'B', 'C', 'D']
        mapeamento_opcoes = {}

        for i_alt, alt in enumerate(alternativas):
            id_alt, texto_alt, eh_correta = alt
            letra = letras[i_alt]
            mapeamento_opcoes[letra] = eh_correta
            print(f"   {letra}) {texto_alt}")

        print("\n" + "-" * 80)

        # Validação da resposta
        while True:
            # Verifica o tempo novamente dentro do loop de input
            if (time.time() - tempo_inicio) > tempo_limite_segundos:
                break

            resposta_usuario = input("👉 Escolha a alternativa (A, B, C, D): ").strip().upper()
            if resposta_usuario in letras:
                break
            print("⚠️ Entrada inválida! Digite apenas A, B, C ou D.")

        # Re-verifica se o tempo estourou enquanto o usuário digitava
        if (time.time() - tempo_inicio) > tempo_limite_segundos:
            break

        # Contabiliza resultado
        if mapeamento_opcoes[resposta_usuario] == 1:
            acertos += 1
            desempenho_categorias[nome_categoria]["acertos"] += 1
        else:
            erros += 1

    # FIM DO EXAME - CÁLCULO DAS MÉTRICAS
    tempo_total_gasto = time.time() - tempo_inicio
    if tempo_total_gasto > tempo_limite_segundos:
        tempo_total_gasto = tempo_limite_segundos

    questoes_respondidas = acertos + erros
    
    # Prevenção contra divisão por zero caso o tempo acabe na primeira questão
    percentual_acertos = (acertos / total_questoes) * 100 if total_questoes > 0 else 0
    
    # A AWS usa uma escala de 100 a 1000 pontos
    nota_aws = 100 + int(percentual_acertos * 9)
    status_aprovacao = "🎉 APROVADO(A)!" if nota_aws >= 700 else "❌ REPROVADO(A)"

    # EXIBIÇÃO DO RESUMO FINAL
    limpar_tela()
    print("=" * 80)
    print("                      RELATÓRIO DE DESEMPENHO FINAL                         ")
    print("=" * 80)
    print(f"👤 Candidato(a): {nome_usuario}")
    print(f"⏱️ Tempo de Prova Utilizado: {formatar_tempo(tempo_total_gasto)} (de 90:00 min)")
    print(f"📝 Questões Respondidas: {questoes_respondidas} de {total_questoes}")
    print("-" * 80)
    print(f"✅ Total de Acertos: {acertos}")
    print(f"❌ Total de Erros: {erros + (total_questoes - questoes_respondidas)}")
    print(f"📊 Percentual de Acertos: {percentual_acertos:.2f}%")
    print(f"💯 Nota do Simulado: {nota_aws} / 1000 (Mínimo para aprovação: 700)")
    print("-" * 80)
    print(f"STATUS DO EXAME: {status_aprovacao}")
    print("=" * 80)
    
    print("\n📈 DESEMPENHO DETALHADO POR DOMÍNIO:")
    for cat, dados in desempenho_categorias.items():
        if dados["total"] > 0:
            pct_cat = (dados["acertos"] / dados["total"]) * 100
            print(f"• {cat}: {dados['acertos']}/{dados['total']} acertos ({pct_cat:.1f}%)")
    print("=" * 80)
    print("\nBons estudos! Continue revisando os conceitos para cravar a certificação real.")
    print("=" * 80 + "\n")

    conn.close()

if __name__ == "__main__":
    rodar_exame()
