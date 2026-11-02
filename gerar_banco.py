import sqlite3
import random

# 1. Estrutura base dos domínios do CLF-C02
dominios = [
    (1, "Domínio 1: Conceitos de Nuvem"),
    (2, "Domínio 2: Segurança e Conformidade"),
    (3, "Domínio 3: Tecnologia e Serviços"),
    (4, "Domínio 4: Faturamento, Preços e Suporte")
]

# 2. Banco de dados conceitual com chaves unificadas e validadas
banco_temas = [
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa deseja migrar para a nuvem da AWS para transformar custos fixos de TI em custos variáveis baseados no uso real. Qual vantagem do Cloud Computing isso representa?",
        "alternativas": ["Elasticidade", "Agilidade", "Trocar despesas de capital por despesas operacionais", "Economia de escala"],
        "correta": "Trocar despesas de capital por despesas operacionais",
        "explicacao": "A conversão de CapEx (Despesas de Capital) para OpEx (Despesas Operacionais) é um dos pilares financeiros da AWS."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "De acordo com o Modelo de Responsabilidade Compartilhada da AWS, qual das seguintes opções é uma responsabilidade exclusiva do cliente?",
        "alternativas": ["Segurança física das instalações", "Gerenciamento de patches do sistema operacional convidado", "Manutenção do software do hipervisor", "Descarte seguro de discos rígidos"],
        "correta": "Gerenciamento de patches do sistema operacional convidado",
        "explicacao": "A AWS cuida da segurança 'da' nuvem (infraestrutura) e o cliente cuida da segurança 'na' nuvem (dados e sistemas operacionais das instâncias EC2)."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual serviço da AWS fornece uma camada de armazenamento de arquivos em rede totalmente gerenciada, que pode ser montada simultaneamente por centenas de instâncias EC2 e servidores on-premises?",
        "alternativas": ["Amazon EBS", "Amazon S3", "Amazon EFS", "Amazon Instance Store"],
        "correta": "Amazon EFS",
        "explicacao": "O Amazon EFS fornece um sistema de arquivos Linux compartilhado via protocolo NFS que permite conexões simultâneas."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma empresa precisa receber alertas automáticos quando seus custos mensais estimados com serviços AWS ultrapassarem um limite pré-definido. Qual recurso deve ser configurado?",
        "alternativas": ["AWS Trusted Advisor", "AWS Budgets", "Cost Explorer", "AWS Pricing Calculator"],
        "correta": "AWS Budgets",
        "explicacao": "O AWS Budgets permite configurar orçamentos personalizados e disparar alertas quando os custos previstos ou reais excedem o limite estabelecido."
    }
]

# 3. Conexão e criação das tabelas no SQLite
conn = sqlite3.connect("aws_simulados.db")
cursor = conn.cursor()

# Habilita suporte a chaves estrangeiras
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS exam_categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    question_text TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    explanation TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES exam_categories(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alternatives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER,
    alternative_text TEXT NOT NULL,
    is_correct INTEGER NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);
""")

# 4. Inserindo domínios
cursor.executemany("INSERT OR IGNORE INTO exam_categories (id, name) VALUES (?, ?);", dominios)

# 5. Gerando e inserindo as 500 variações de forma segura
for i in range(1, 5001):
    tema_base = random.choice(banco_temas)
    dom_id = tema_base["dominio_id"]
    
    variacoes = [
        f" [Variação Simulado #{i}] ",
        f" [Questão de Revisão #{i}] ",
        f" [Cenário de Negócios #{i}] "
    ]
    prefixo = random.choice(variacoes)
    enunciado = prefixo + tema_base["template_pergunta"]
    
    # Inserir pergunta
    cursor.execute(
        "INSERT INTO questions (category_id, question_text, difficulty, explanation) VALUES (?, ?, ?, ?);",
        (dom_id, enunciado, "Medium", tema_base["explicacao"])
    )
    question_id = cursor.lastrowid
    
    # Coleta a lista usando a chave correta em português ("alternativas")
    alts = list(tema_base["alternativas"])
    random.shuffle(alts)
    
    # Inserir alternativas vinculadas
    for alt in alts:
        is_correct = 1 if alt == tema_base["correta"] else 0
        cursor.execute(
            "INSERT INTO alternatives (question_id, alternative_text, is_correct) VALUES (?, ?, ?);",
            (question_id, alt, is_correct)
        )

# Salvar alterações e fechar conexão
conn.commit()
conn.close()

print("Sucesso! Banco de dados 'aws_simulados.db' criado e populado com 5000 questões.")
