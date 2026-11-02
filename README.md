# ☁️ AWS Cloud Practitioner (CLF-C02) -  Simulados Interativos SQL & Python

Este repositório contém uma aplicação baseada em terminal desenvolvida para auxiliar na preparação para o exame de certificação **AWS Certified Cloud Practitioner (CLF-C02)**. O sistema utiliza uma base de dados local **SQLite** estruturada de acordo com os domínios oficiais da AWS e gerencia os questionários por meio de scripts Python dinâmicos.

## 🛠️ Arquitetura do Repositório

O projeto é composto pelos seguintes arquivos principais:

*   **`gerar_banco.py`**: Script de automação e carga de dados. Cria o arquivo de banco de dados SQLite e popula las tabelas com as questões estruturadas.
*   **`questoes_clf_c02.py`**: Banco com as questões reais do exame, organizadas pelos 4 domínios oficiais, com alternativas, gabarito e explicação.
*   **`simuladoaws.py`**: Modo de treino livre. Sorteia perguntas aleatórias e fornece a validação e explicação da AWS imediatamente após a resposta.
*   **`exame_oficial.py`**: Modo de exame simulado. Configura um ambiente de teste estrito com 64 questões, cronômetro regressivo de 90 minutos e gera uma nota final baseada na escala oficial da AWS (100 a 1000).
*   **`web/`**: Interface web opcional (`servidor_web.py` + `static/index.html`) com os modos de treino e exame no navegador, usando o mesmo banco de dados.

---

## 📌 Pré-requisitos

### 🐧 Linux (Fedora/Ubuntu)
Certifique-se de ter o Python 3 instalado. Você também pode instalar o cliente do SQLite se quiser inspecionar os dados manualmente:

```bash
# No Fedora
sudo dnf install python3 sqlite

# No Ubuntu/Debian
sudo apt install python3 sqlite3
```

### 🪟 Windows
1. Certifique-se de ter o **Python 3** instalado na sua máquina (baixe pelo site oficial ou via Microsoft Store).
2. **Importante:** Marque a opção **"Add python.exe to PATH"** durante o processo de instalação do Python.
3. Você pode utilizar o **PowerShell** ou o **Prompt de Comando (CMD)** para rodar as instruções abaixo.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo na ordem indicada para configurar e rodar os simulados no seu terminal (Linux) ou console (Windows).

### Passo 1: Inicializar o Banco de Dados (`aws_simulados.db`)
Antes de iniciar qualquer simulado, você precisa criar a estrutura do banco de dados e populá-la. Execute o script gerador:

* **Linux / Windows:**
```bash
python3 gerar_banco.py
```
*(Nota para usuários de Windows: Se o comando `python3` não funcionar, utilize apenas `python gerar_banco.py`)*

*Retorno esperado:* Uma mensagem de sucesso confirmando que o arquivo local `aws_simulados.db` foi gerado com as 500 questões populadas.

No total são 2.504 registros:

| Tabela | Registros |
|---|---:|
| `exam_categories` | 4 |
| `questions` | 500 |
| `alternatives` | 2.000 |

São 4 alternativas para cada questão.

### Passo 2: Executar o Modo Treino Livre (`simuladoaws.py`)
Se você quer praticar sem pressão de tempo e conferir as justificativas de cada resposta na hora, utilize este script:

* **Linux / Windows:**
```bash
python3 simuladoaws.py
```
*(No Windows, se necessário, use: `python simuladoaws.py`)*

*   **Funcionamento**: O terminal limpa a tela, exibe uma pergunta aleatória por vez com suas 4 alternativas e pede o seu input (`A, B, C, D`). Após responder, o gabarito comentado da AWS é exibido. Digite `SAIR` a qualquer momento para finalizar.

### Passo 3: Realizar o Exame Completo (`exame_oficial.py`)
Para simular a experiência real do dia da prova da AWS, execute o gerenciador de exames:

* **Linux / Windows:**
```bash
python3 exame_oficial.py
```
*(No Windows, se necessário, use: `python exame_oficial.py`)*

*   **Funcionamento**: O script solicitará o seu nome e iniciará um cronômetro regressivo de **90 minutos**. Serão exibidas **64 questões** consecutivas sem feedback imediato.
*   **Encerramento por Tempo**: Se o cronômetro zerar antes de você concluir, o exame é interrompido e computa apenas as respostas enviadas até o momento.
*   **Painel de Desempenho**: Ao final, o sistema exibe um relatório com o tempo total gasto, percentual de acertos, a nota na escala AWS (mínimo de 700 para passar) e um diagnóstico detalhado de desempenho por domínio para você saber onde precisa focar seus estudos.

### Opcional: Usar a Interface Web no Navegador (`web/servidor_web.py`)
Se preferir estudar pelo navegador em vez do terminal, inicie o servidor web (depois de executar o Passo 1):

* **Linux / Windows:**
```bash
python3 web/servidor_web.py
```
*(No Windows, se necessário, use: `python web\servidor_web.py`)*

O navegador abre automaticamente em `http://127.0.0.1:8000`. Se essa porta já estiver em uso por outro programa, escolha outra:
```bash
python3 web/servidor_web.py --porta 8080
```
Para iniciar sem abrir o navegador automaticamente, use `--sem-navegador`. Pressione `CTRL+C` no terminal para encerrar o servidor.

*   **Sem instalação extra**: Usa apenas a biblioteca padrão do Python e lê o `aws_simulados.db` em modo somente leitura, sem alterar os dados.
*   **Treino livre**: Uma questão aleatória por vez, com gabarito, explicação da AWS e placar de acertos.
*   **Exame simulado**: 64 questões com cronômetro de 90 minutos. É possível navegar entre as questões, alterar respostas e marcar questões para revisar. Ao zerar o tempo, o exame é encerrado automaticamente.
*   **Resultado**: Nota na escala AWS (100 a 1000, aprovação com 700), desempenho por domínio e revisão de cada questão com a explicação.
*   **Atalhos de teclado**: `A`–`D` para responder, `Enter` para a próxima questão no treino e as setas `←` `→` para navegar no exame.

---

## ⚙️ Customização: Alterando Parâmetros do Simulado

Se você quiser modificar o volume de dados gerados, o tamanho do exame ou o tempo limite do cronômetro, você pode alterar as configurações diretamente no código-fonte dos scripts:

### 1. Adicionar ou alterar questões no Banco de Dados
As questões ficam no arquivo `questoes_clf_c02.py`, divididas pelos 4 domínios conforme o peso oficial da prova (24%, 30%, 34% e 12%). Para incluir uma nova questão:
1. Abra o arquivo `questoes_clf_c02.py`.
2. Adicione um novo item à lista `QUESTOES`, seguindo o mesmo formato:
   ```python
   {
       "dominio_id": 3,
       "template_pergunta": "Qual serviço oferece armazenamento de objetos com 99,999999999% de durabilidade?",
       "alternativas": ["Amazon S3", "Amazon EBS", "Amazon EFS", "Instance Store"],
       "correta": "Amazon S3",
       "explicacao": "O Amazon S3 foi projetado para 11 noves de durabilidade."
   },
   ```
3. Execute `python3 gerar_banco.py` novamente. O banco é recriado do zero, sem duplicar questões, e o script valida se cada questão tem 4 alternativas distintas com a correta entre elas.

### 2. Alterar o número de questões exibidas no Exame Oficial
O simulado oficial vem configurado com **64 questões** (padrão da prova real). Se quiser fazer um teste mais rápido ou mais longo:
1. Abra o arquivo `exame_oficial.py`.
2. Vá até a **linha 40** (na query SQL que busca as perguntas) e altere o valor do `LIMIT`:
   ```sql
   -- Exemplo: Alterando para rodar um simulado rápido de 20 questões
   LIMIT 20;
   ```
3. Atualize a variável `total_questoes` na **linha 49** para corresponder ao novo valor:
   ```python
   total_questoes = 20
   ```
   *Nota: Certifique-se de que o seu banco de dados foi populado com uma quantidade total de perguntas maior ou igual ao limite configurado aqui.*

### 3. Alterar o Tempo Limite do Cronômetro
O tempo padrão do simulado estrito é de **90 minutos** (5400 segundos). Se você quiser encurtar o tempo para treinar agilidade ou dar mais tempo para revisar com calma:
1. Abra o arquivo `exame_oficial.py`.
2. Vá até a **linha 52** onde a variável `tempo_limite_segundos` está definida.
3. Altere o cálculo para a quantidade de minutos desejada:
   ```python
   # Exemplo: Alterando o tempo limite para um simulado rápido de 30 minutos
   tempo_limite_segundos = 30 * 60
   ```
4. *(Opcional)* Se quiser que a tela de regras iniciais exiba o texto correto correspondente ao seu novo tempo, altere a mensagem informativa que está na **linha 27**.

---

## 🗃️ Estrutura do Banco de Dados SQL

O arquivo `aws_simulados.db` gerado respeita a seguinte modelagem relacional:

*   **`exam_categories`**: Armazena os 4 escopos oficiais da certificação CLF-C02.
*   **`questions`**: Guarda os enunciados das questões, nível de dificuldade e o texto explicativo/gabarito.
*   **`alternatives`**: Registra as opções de resposta atreladas por chave estrangeira (`FOREIGN KEY`) a cada questão, utilizando flags inteiras (`1` para correto, `0` para incorreto) compatíveis com o motor leve do SQLite.

---
💡 *Dica de estudo: Foque em compreender as justificativas geradas no final do `exame_oficial.py` para fixar as diferenças críticas entre os serviços principais da AWS (como as diferenças entre S3, EBS e EFS).*
