import sqlite3
import random

# 1. Estrutura base dos domínios do CLF-C02
dominios = [
    (1, "Domínio 1: Conceitos de Nuvem"),
    (2, "Domínio 2: Segurança e Conformidade"),
    (3, "Domínio 3: Tecnologia e Serviços"),
    (4, "Domínio 4: Faturamento, Preços e Suporte")
]

# 2. Banco de questões reais do CLF-C02 (arquivo questoes_clf_c02.py)
from questoes_clf_c02 import QUESTOES

# Validação: cada questão precisa de 4 alternativas distintas e uma correta entre elas
ids_dominios = {d[0] for d in dominios}
for n, q in enumerate(QUESTOES, start=1):
    assert q["dominio_id"] in ids_dominios, f"Questão {n}: domínio inválido"
    assert len(q["alternativas"]) == 4, f"Questão {n}: precisa de 4 alternativas"
    assert len(set(q["alternativas"])) == 4, f"Questão {n}: alternativas repetidas"
    assert q["correta"] in q["alternativas"], f"Questão {n}: resposta correta fora das alternativas"
assert len({q["template_pergunta"] for q in QUESTOES}) == len(QUESTOES), "Há enunciados duplicados"

# 3. Conexão e criação das tabelas no SQLite
conn = sqlite3.connect("aws_simulados.db")
cursor = conn.cursor()

# Habilita suporte a chaves estrangeiras
cursor.execute("PRAGMA foreign_keys = ON;")

# Recria as tabelas para que rodar o script de novo não duplique as questões
cursor.execute("DROP TABLE IF EXISTS alternatives;")
cursor.execute("DROP TABLE IF EXISTS questions;")
cursor.execute("DROP TABLE IF EXISTS exam_categories;")

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

# 5. Inserindo cada questão uma única vez, com as alternativas embaralhadas
for tema_base in QUESTOES:
    cursor.execute(
        "INSERT INTO questions (category_id, question_text, difficulty, explanation) VALUES (?, ?, ?, ?);",
        (tema_base["dominio_id"], tema_base["template_pergunta"], "Medium", tema_base["explicacao"])
    )
    question_id = cursor.lastrowid

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

print(f"Sucesso! Banco de dados 'aws_simulados.db' criado e populado com {len(QUESTOES)} questões.")
for id_dom, nome_dom in dominios:
    qtd = sum(1 for q in QUESTOES if q["dominio_id"] == id_dom)
    print(f"  • {nome_dom}: {qtd} questões")
