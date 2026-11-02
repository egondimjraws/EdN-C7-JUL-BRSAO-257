import sqlite3
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def rodar_simulado():
    # Conecta ao banco de dados SQLite
    if not os.path.exists("aws_simulados.db"):
        print("Erro: O arquivo 'aws_simulados.db' não foi encontrado nesta pasta.")
        print("Por favor, execute o script 'gerar_banco.py' primeiro para criar o banco de dados.")
        return

    conn = sqlite3.connect("aws_simulados.db")
    cursor = conn.cursor()

    while True:
        limpar_tela()
        print("=" * 97)
        print("              C7-JUL-BRSAO-257  SIMULADO INTERATIVO - AWS CLOUD PRACTITIONER (CLF-C02)       ")
        print("=" * 97)

        # 1. Busca uma pergunta aleatória do banco de dados juntamente com o nome da categoria
        cursor.execute("""
            SELECT q.id, q.question_text, q.explanation, c.name 
            FROM questions q
            JOIN exam_categories c ON q.category_id = c.id
            ORDER BY RANDOM() 
            LIMIT 1;
        """)
        pergunta = cursor.fetchone()
        
        if not pergunta:
            print("Nenhuma pergunta encontrada no banco de dados.")
            break

        id_pergunta, texto_pergunta, explicacao, nome_categoria = pergunta

        print(f"\n📂 {nome_categoria}")
        print(f"❓ {texto_pergunta}\n")

        # 2. Busca as alternativas correspondentes à pergunta sorteada
        cursor.execute("""
            SELECT id, alternative_text, is_correct 
            FROM alternatives 
            WHERE question_id = ?;
        """, (id_pergunta,))
        alternativas = cursor.fetchall()

        # Mapeamento de letras para as opções
        letras = ['A', 'B', 'C', 'D']
        mapeamento_opcoes = {}
        alternativa_correta_letra = ""

        # Exibe as alternativas na tela
        for idx, alt in enumerate(alternativas):
            id_alt, texto_alt, eh_correta = alt
            letra = letras[idx]
            mapeamento_opcoes[letra] = (texto_alt, eh_correta)
            
            if eh_correta == 1:
                alternativa_correta_letra = letra
                
            print(f"   {letra}) {texto_alt}")

        print("\n" + "-" * 80)
        
        # 3. Validação do input do usuário
        while True:
            resposta_usuario = input("👉 Digite a sua resposta (A, B, C, D) ou 'SAIR' para encerrar: ").strip().upper()
            
            if resposta_usuario == 'SAIR':
                print("\nSimulado encerrado. Bons estudos!")
                conn.close()
                return
                
            if resposta_usuario in letras:
                break
            print("⚠️ Opção inválida! Escolha apenas entre A, B, C ou D.")

        # 4. Verificação do resultado
        _, acertou = mapeamento_opcoes[resposta_usuario]

        print("\n" + "=" * 80)
        if acertou == 1:
            print("✅ PARABÉNS! Você acertou a questão!")
        else:
            print(f"❌ INCORRETO. A alternativa certa era a letra ({alternativa_correta_letra}).")
        
        print(f"\n📖 EXPLICAÇÃO DA AWS:\n{explicacao}")
        print("=" * 80)

        # Aguarda comando do usuário para continuar ou parar
        continuar = input("\nPressione ENTER para ir para a próxima pergunta ou digite 'S' para sair: ").strip().upper()
        if continuar == 'S':
            print("\nSimulado encerrado. Bons estudos!")
            break

    conn.close()

if __name__ == "__main__":
    rodar_simulado()
