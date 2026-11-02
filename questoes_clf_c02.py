"""
Banco de questões do AWS Certified Cloud Practitioner (CLF-C02).

Cada questão possui:
    dominio_id         -> 1 a 4 (ver lista `dominios` em gerar_banco.py)
    template_pergunta  -> enunciado
    alternativas       -> exatamente 4 opções distintas
    correta            -> texto idêntico a uma das alternativas
    explicacao         -> justificativa exibida após a resposta

A distribuição segue o peso oficial dos domínios no exame:
    Domínio 1 (Conceitos de Nuvem) ............ 24%
    Domínio 2 (Segurança e Conformidade) ...... 30%
    Domínio 3 (Tecnologia e Serviços) ......... 34%
    Domínio 4 (Faturamento, Preços e Suporte) . 12%
"""

QUESTOES = [
    # =====================================================================
    # DOMÍNIO 1: CONCEITOS DE NUVEM
    # =====================================================================
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa deseja migrar para a nuvem da AWS para transformar custos fixos de TI em custos variáveis baseados no uso real. Qual vantagem do Cloud Computing isso representa?",
        "alternativas": ["Elasticidade", "Agilidade", "Trocar despesas de capital por despesas operacionais", "Economia de escala"],
        "correta": "Trocar despesas de capital por despesas operacionais",
        "explicacao": "A conversão de CapEx (Despesas de Capital) para OpEx (Despesas Operacionais) é um dos pilares financeiros da AWS: paga-se apenas pelo que é consumido, sem investimento antecipado em data centers e servidores."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A AWS consegue reduzir seus preços continuamente porque agrega o uso de centenas de milhares de clientes. Qual vantagem da nuvem descreve esse cenário?",
        "alternativas": ["Beneficiar-se de enormes economias de escala", "Parar de adivinhar a capacidade", "Tornar-se global em minutos", "Aumentar a velocidade e a agilidade"],
        "correta": "Beneficiar-se de enormes economias de escala",
        "explicacao": "Com o uso agregado de muitos clientes, a AWS obtém economias de escala maiores do que uma empresa conseguiria sozinha, o que se traduz em preços menores no modelo pré-pago."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa costumava comprar servidores em excesso para suportar picos de acesso que raramente aconteciam. Ao migrar para a AWS, ela passou a provisionar recursos conforme a demanda real. Qual vantagem da nuvem foi obtida?",
        "alternativas": ["Parar de adivinhar a capacidade", "Economia de escala", "Parar de gastar dinheiro com a manutenção de data centers", "Tornar-se global em minutos"],
        "correta": "Parar de adivinhar a capacidade",
        "explicacao": "Na nuvem não é preciso estimar a capacidade com antecedência: é possível aumentar ou reduzir os recursos conforme a necessidade, evitando ociosidade ou falta de capacidade."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma equipe de desenvolvimento passou a criar ambientes de teste em minutos, em vez de esperar semanas pela compra de hardware. Qual vantagem da nuvem isso representa?",
        "alternativas": ["Aumentar a velocidade e a agilidade", "Economia de escala", "Alta disponibilidade", "Trocar despesas de capital por despesas operacionais"],
        "correta": "Aumentar a velocidade e a agilidade",
        "explicacao": "Na AWS, novos recursos ficam disponíveis com poucos cliques, reduzindo de semanas para minutos o tempo necessário para experimentar e entregar soluções."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma startup brasileira deseja oferecer baixa latência para clientes na Europa e na Ásia sem construir data centers nesses continentes. Qual vantagem da nuvem atende a essa necessidade?",
        "alternativas": ["Tornar-se global em minutos", "Parar de adivinhar a capacidade", "Economia de escala", "Elasticidade"],
        "correta": "Tornar-se global em minutos",
        "explicacao": "A infraestrutura global da AWS permite implantar aplicações em várias Regiões do mundo com poucos cliques, oferecendo baixa latência a usuários em diferentes locais."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma loja virtual precisa adicionar servidores automaticamente durante a Black Friday e removê-los quando o tráfego volta ao normal. Qual característica da nuvem descreve essa capacidade?",
        "alternativas": ["Elasticidade", "Durabilidade", "Tolerância a falhas", "Alta disponibilidade"],
        "correta": "Elasticidade",
        "explicacao": "Elasticidade é a capacidade de adquirir recursos quando necessário e liberá-los quando não são mais precisos, acompanhando a demanda automaticamente."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual pilar do AWS Well-Architected Framework trata da capacidade de uma carga de trabalho se recuperar de falhas e executar sua função corretamente de forma consistente?",
        "alternativas": ["Confiabilidade", "Eficiência de performance", "Excelência operacional", "Segurança"],
        "correta": "Confiabilidade",
        "explicacao": "O pilar Confiabilidade aborda recuperação automática de falhas, escalabilidade horizontal e testes dos procedimentos de recuperação para que a carga de trabalho funcione como esperado."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual pilar do AWS Well-Architected Framework foca em minimizar os impactos ambientais da execução de cargas de trabalho na nuvem?",
        "alternativas": ["Sustentabilidade", "Otimização de custos", "Eficiência de performance", "Confiabilidade"],
        "correta": "Sustentabilidade",
        "explicacao": "O pilar Sustentabilidade, adicionado em 2021, trata da redução do consumo de energia e do uso eficiente de recursos para diminuir o impacto ambiental."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa quer automatizar mudanças, responder a eventos e definir padrões para gerenciar suas operações diárias na AWS. Qual pilar do Well-Architected Framework trata desses objetivos?",
        "alternativas": ["Excelência operacional", "Segurança", "Confiabilidade", "Sustentabilidade"],
        "correta": "Excelência operacional",
        "explicacao": "Excelência operacional envolve executar e monitorar sistemas e melhorar continuamente processos e procedimentos, como realizar operações como código e fazer mudanças pequenas e reversíveis."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual pilar do AWS Well-Architected Framework recomenda evitar gastos desnecessários, analisar despesas e escolher o tipo e a quantidade certa de recursos?",
        "alternativas": ["Otimização de custos", "Eficiência de performance", "Excelência operacional", "Confiabilidade"],
        "correta": "Otimização de custos",
        "explicacao": "O pilar Otimização de custos trata de entregar valor de negócio pelo menor preço, adotando um modelo de consumo e eliminando recursos ociosos."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa quer usar os recursos de computação de forma eficiente, adotando tecnologias como serverless e experimentando novos tipos de instância conforme a demanda evolui. Qual pilar do Well-Architected Framework trata disso?",
        "alternativas": ["Eficiência de performance", "Otimização de custos", "Confiabilidade", "Excelência operacional"],
        "correta": "Eficiência de performance",
        "explicacao": "Eficiência de performance trata do uso eficiente dos recursos para atender aos requisitos, mantendo essa eficiência à medida que a demanda muda e as tecnologias evoluem."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa mantém seu sistema legado no data center próprio e conecta esse ambiente a aplicações executadas na AWS. Qual modelo de implantação de nuvem está sendo usado?",
        "alternativas": ["Híbrido", "Totalmente na nuvem", "On-premises (nuvem privada)", "Multi-região"],
        "correta": "Híbrido",
        "explicacao": "O modelo híbrido conecta a infraestrutura on-premises aos recursos na nuvem, permitindo que as cargas de trabalho sejam distribuídas entre os dois ambientes."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa precisa de controle total sobre o sistema operacional, a rede e o software instalado em seus servidores virtuais na nuvem. Qual modelo de serviço oferece esse nível de controle?",
        "alternativas": ["Infraestrutura como Serviço (IaaS)", "Plataforma como Serviço (PaaS)", "Software como Serviço (SaaS)", "Função como Serviço (FaaS)"],
        "correta": "Infraestrutura como Serviço (IaaS)",
        "explicacao": "IaaS, como o Amazon EC2, fornece os blocos básicos de infraestrutura e oferece o maior nível de flexibilidade e controle sobre os recursos de TI."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Um desenvolvedor quer apenas enviar o código da aplicação e deixar que a AWS cuide automaticamente do provisionamento, balanceamento de carga e escalabilidade. Usando o AWS Elastic Beanstalk, qual modelo de serviço ele está adotando?",
        "alternativas": ["Plataforma como Serviço (PaaS)", "Infraestrutura como Serviço (IaaS)", "Software como Serviço (SaaS)", "Nuvem privada"],
        "correta": "Plataforma como Serviço (PaaS)",
        "explicacao": "No PaaS a infraestrutura subjacente é gerenciada pelo provedor, permitindo que o cliente se concentre na implantação e no gerenciamento das aplicações. O Elastic Beanstalk é um exemplo clássico."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Durante a adoção da nuvem, uma empresa precisa preparar seus funcionários com novas habilidades e adaptar a cultura organizacional. Qual perspectiva do AWS Cloud Adoption Framework (AWS CAF) trata desse tema?",
        "alternativas": ["Pessoas", "Plataforma", "Operações", "Segurança"],
        "correta": "Pessoas",
        "explicacao": "A perspectiva Pessoas do AWS CAF faz a ponte entre tecnologia e negócios, cuidando de cultura, estrutura organizacional, liderança e capacitação da força de trabalho."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual perspectiva do AWS Cloud Adoption Framework (AWS CAF) ajuda a orquestrar as iniciativas de nuvem, maximizando os benefícios organizacionais e minimizando os riscos da transformação?",
        "alternativas": ["Governança", "Negócios", "Plataforma", "Operações"],
        "correta": "Governança",
        "explicacao": "A perspectiva Governança trata de gerenciamento de programas e projetos, gestão de benefícios, riscos e finanças da nuvem durante a transformação."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa precisa migrar rapidamente centenas de servidores para o Amazon EC2 sem fazer nenhuma alteração nas aplicações. Qual estratégia de migração está sendo utilizada?",
        "alternativas": ["Redefinir a hospedagem (rehost)", "Refatorar (refactor)", "Recomprar (repurchase)", "Aposentar (retire)"],
        "correta": "Redefinir a hospedagem (rehost)",
        "explicacao": "Rehost, conhecido como 'lift and shift', move as aplicações para a nuvem sem alterações, sendo a forma mais rápida de migrar em grande escala."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa vai migrar seu banco de dados MySQL de um servidor próprio para o Amazon RDS, sem alterar o código da aplicação, para reduzir o trabalho de administração. Qual estratégia de migração está sendo aplicada?",
        "alternativas": ["Redefinir a plataforma (replatform)", "Redefinir a hospedagem (rehost)", "Refatorar (refactor)", "Reter (retain)"],
        "correta": "Redefinir a plataforma (replatform)",
        "explicacao": "Replatform ('lift, tinker and shift') faz algumas otimizações para aproveitar a nuvem, como trocar um banco autogerenciado por um serviço gerenciado, sem mudar a arquitetura principal da aplicação."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa decidiu reescrever sua aplicação monolítica como microsserviços serverless para ganhar escalabilidade e agilidade. Qual estratégia de migração é essa?",
        "alternativas": ["Refatorar (refactor)", "Redefinir a hospedagem (rehost)", "Realocar (relocate)", "Recomprar (repurchase)"],
        "correta": "Refatorar (refactor)",
        "explicacao": "Refatorar (ou rearquitetar) muda a forma como a aplicação é construída, normalmente usando recursos nativos da nuvem. É a estratégia que exige mais esforço, mas traz mais benefícios."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Durante a análise do portfólio de TI para migração, uma empresa identificou aplicações que não são mais usadas e decidiu desligá-las. Qual estratégia de migração é essa?",
        "alternativas": ["Aposentar (retire)", "Reter (retain)", "Recomprar (repurchase)", "Realocar (relocate)"],
        "correta": "Aposentar (retire)",
        "explicacao": "Aposentar consiste em desativar aplicações que não são mais úteis, reduzindo custos e a superfície a ser protegida e migrada."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Um arquiteto colocou uma fila do Amazon SQS entre o front-end e o processamento de pedidos para que a falha de um componente não derrube o outro. Qual princípio de design da nuvem foi aplicado?",
        "alternativas": ["Desacoplar os componentes (acoplamento fraco)", "Escalabilidade vertical", "Servidores como animais de estimação", "Arquitetura monolítica"],
        "correta": "Desacoplar os componentes (acoplamento fraco)",
        "explicacao": "Com acoplamento fraco, os componentes se comunicam de forma assíncrona e uma falha ou lentidão em um deles não se propaga para os demais."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa precisa transferir 80 TB de dados para a AWS, mas sua conexão com a internet levaria meses para concluir a cópia. Qual serviço é o mais indicado?",
        "alternativas": ["AWS Snowball Edge", "AWS Direct Connect", "Amazon S3 Transfer Acceleration", "AWS Site-to-Site VPN"],
        "correta": "AWS Snowball Edge",
        "explicacao": "O AWS Snowball Edge é um dispositivo físico enviado ao cliente para transferir grandes volumes de dados offline, evitando a dependência da largura de banda da internet."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma empresa quer migrar seu banco de dados Oracle on-premises para a AWS mantendo o banco de origem em funcionamento durante a migração, com mínimo tempo de inatividade. Qual serviço deve ser usado?",
        "alternativas": ["AWS Database Migration Service (AWS DMS)", "AWS DataSync", "AWS Snowball Edge", "AWS Backup"],
        "correta": "AWS Database Migration Service (AWS DMS)",
        "explicacao": "O AWS DMS migra bancos de dados para a AWS de forma rápida e segura; o banco de origem continua operacional durante a migração, minimizando o tempo de inatividade."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Para suportar mais usuários, uma equipe passou a adicionar novas instâncias EC2 atrás de um balanceador de carga, em vez de trocar a instância por uma maior. Que tipo de escalabilidade é essa?",
        "alternativas": ["Escalabilidade horizontal", "Escalabilidade vertical", "Escalabilidade diagonal", "Escalabilidade manual"],
        "correta": "Escalabilidade horizontal",
        "explicacao": "Escalar horizontalmente significa adicionar mais recursos (por exemplo, mais instâncias). Escalar verticalmente significa aumentar a capacidade de um único recurso (instância maior)."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual prática aumenta a disponibilidade de uma aplicação executada no Amazon EC2?",
        "alternativas": ["Distribuir as instâncias em várias Zonas de Disponibilidade", "Executar todas as instâncias em uma única Zona de Disponibilidade", "Usar uma única instância de maior tamanho", "Armazenar os dados apenas no armazenamento de instância"],
        "correta": "Distribuir as instâncias em várias Zonas de Disponibilidade",
        "explicacao": "As Zonas de Disponibilidade são isoladas entre si; distribuir a aplicação entre elas evita que a falha de um data center torne a aplicação indisponível."
    },

    # =====================================================================
    # DOMÍNIO 2: SEGURANÇA E CONFORMIDADE
    # =====================================================================
    {
        "dominio_id": 2,
        "template_pergunta": "De acordo com o Modelo de Responsabilidade Compartilhada da AWS, qual das seguintes opções é uma responsabilidade exclusiva do cliente?",
        "alternativas": ["Segurança física das instalações", "Gerenciamento de patches do sistema operacional convidado", "Manutenção do software do hipervisor", "Descarte seguro de discos rígidos"],
        "correta": "Gerenciamento de patches do sistema operacional convidado",
        "explicacao": "A AWS cuida da segurança 'da' nuvem (infraestrutura) e o cliente cuida da segurança 'na' nuvem (dados e sistemas operacionais das instâncias EC2)."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "De acordo com o Modelo de Responsabilidade Compartilhada, qual das opções a seguir é responsabilidade da AWS?",
        "alternativas": ["Segurança física dos data centers", "Configuração dos security groups", "Criptografia dos dados do cliente", "Gerenciamento de usuários e permissões do IAM"],
        "correta": "Segurança física dos data centers",
        "explicacao": "A AWS é responsável pela segurança da nuvem: instalações físicas, hardware, rede global e software de virtualização. Configurações de acesso e dados são responsabilidade do cliente."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Ao usar o Amazon RDS, qual tarefa é de responsabilidade da AWS?",
        "alternativas": ["Aplicar patches no sistema operacional e no mecanismo do banco de dados", "Criar os usuários do banco de dados e suas permissões", "Configurar as regras dos security groups do banco", "Decidir se os dados serão criptografados"],
        "correta": "Aplicar patches no sistema operacional e no mecanismo do banco de dados",
        "explicacao": "Em serviços gerenciados como o RDS, a AWS assume a manutenção do sistema operacional e do mecanismo do banco. O cliente continua responsável por acessos, rede e proteção dos dados."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual é a prática recomendada para o usuário raiz (root) de uma conta da AWS?",
        "alternativas": ["Habilitar MFA e usá-lo apenas para tarefas que exigem o usuário raiz", "Usá-lo diariamente para tarefas administrativas", "Compartilhar suas credenciais com a equipe de operações", "Criar chaves de acesso para uso em scripts"],
        "correta": "Habilitar MFA e usá-lo apenas para tarefas que exigem o usuário raiz",
        "explicacao": "O usuário raiz tem acesso irrestrito à conta. A AWS recomenda protegê-lo com MFA, não criar chaves de acesso para ele e usar identidades do IAM nas tarefas do dia a dia."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Um administrador concedeu a um analista apenas a permissão de leitura em um bucket específico do S3, que é tudo o que ele precisa para trabalhar. Qual prática de segurança foi aplicada?",
        "alternativas": ["Princípio do privilégio mínimo", "Defesa em profundidade", "Separação de contas", "Criptografia em trânsito"],
        "correta": "Princípio do privilégio mínimo",
        "explicacao": "O privilégio mínimo consiste em conceder somente as permissões necessárias para executar uma tarefa, reduzindo o impacto de credenciais comprometidas ou erros."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma aplicação executada em uma instância EC2 precisa ler objetos de um bucket do S3. Qual é a forma mais segura de conceder esse acesso?",
        "alternativas": ["Associar uma função (role) do IAM à instância", "Gravar as chaves de acesso de um usuário do IAM no código", "Usar as credenciais do usuário raiz", "Tornar o bucket público"],
        "correta": "Associar uma função (role) do IAM à instância",
        "explicacao": "As funções do IAM fornecem credenciais temporárias que são rotacionadas automaticamente, eliminando a necessidade de armazenar chaves de acesso na instância."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma empresa tem 30 desenvolvedores que precisam das mesmas permissões. Qual recurso do IAM simplifica o gerenciamento dessas permissões?",
        "alternativas": ["Grupos do IAM", "Funções vinculadas a serviços", "Políticas de bucket do S3", "Listas de controle de acesso de rede"],
        "correta": "Grupos do IAM",
        "explicacao": "Um grupo do IAM reúne usuários e permite anexar políticas uma única vez; todos os membros herdam essas permissões, facilitando a administração."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma empresa com várias contas na AWS quer impedir que qualquer conta da área de desenvolvimento use serviços fora de uma lista aprovada, inclusive para administradores. Qual recurso deve ser usado?",
        "alternativas": ["Políticas de controle de serviço (SCPs) do AWS Organizations", "Grupos do IAM", "AWS Config", "Security groups"],
        "correta": "Políticas de controle de serviço (SCPs) do AWS Organizations",
        "explicacao": "As SCPs definem o máximo de permissões disponível nas contas de uma organização ou unidade organizacional, valendo inclusive para os administradores dessas contas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma empresa quer que seus funcionários acessem várias contas da AWS e aplicações corporativas com um único login centralizado. Qual serviço atende a esse requisito?",
        "alternativas": ["AWS IAM Identity Center", "Amazon Cognito", "AWS Secrets Manager", "AWS Directory Service apenas"],
        "correta": "AWS IAM Identity Center",
        "explicacao": "O AWS IAM Identity Center (sucessor do AWS Single Sign-On) centraliza o acesso da força de trabalho a várias contas da AWS e aplicações com um único login."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Um auditor solicitou os relatórios de conformidade SOC e PCI da infraestrutura da AWS. Onde a empresa pode obter esses documentos?",
        "alternativas": ["AWS Artifact", "AWS Config", "AWS Trusted Advisor", "AWS CloudTrail"],
        "correta": "AWS Artifact",
        "explicacao": "O AWS Artifact é o portal de autoatendimento para baixar relatórios de conformidade da AWS (como SOC e PCI) e aceitar acordos, como o BAA."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual serviço da AWS protege aplicações contra ataques de negação de serviço distribuída (DDoS), estando disponível automaticamente para todos os clientes sem custo adicional em sua versão Standard?",
        "alternativas": ["AWS Shield", "AWS WAF", "Amazon GuardDuty", "Amazon Inspector"],
        "correta": "AWS Shield",
        "explicacao": "O AWS Shield Standard protege automaticamente contra os ataques DDoS mais comuns. O Shield Advanced oferece proteção adicional e acesso à equipe de resposta a DDoS."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma aplicação web vem sofrendo tentativas de injeção de SQL e cross-site scripting (XSS). Qual serviço permite criar regras para bloquear essas requisições?",
        "alternativas": ["AWS WAF", "AWS Shield Standard", "Network ACLs", "Amazon Macie"],
        "correta": "AWS WAF",
        "explicacao": "O AWS WAF é um firewall de aplicações web que filtra requisições HTTP/HTTPS com base em regras, protegendo contra ataques como injeção de SQL e XSS."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual serviço usa machine learning para analisar logs do AWS CloudTrail, logs de fluxo da VPC e logs de DNS em busca de atividades maliciosas na conta?",
        "alternativas": ["Amazon GuardDuty", "Amazon Inspector", "AWS Config", "Amazon Macie"],
        "correta": "Amazon GuardDuty",
        "explicacao": "O Amazon GuardDuty é um serviço de detecção de ameaças que monitora continuamente atividades suspeitas, como chamadas de API incomuns ou comunicação com endereços maliciosos."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma empresa quer verificar automaticamente suas instâncias EC2 e imagens de contêiner em busca de vulnerabilidades de software conhecidas. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Inspector", "Amazon GuardDuty", "AWS Shield", "AWS Artifact"],
        "correta": "Amazon Inspector",
        "explicacao": "O Amazon Inspector avalia continuamente instâncias EC2, imagens de contêiner no Amazon ECR e funções Lambda em busca de vulnerabilidades (CVEs) e exposição de rede indesejada."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma empresa precisa descobrir quais buckets do S3 armazenam dados pessoais sensíveis, como números de CPF e cartões de crédito. Qual serviço atende a essa necessidade?",
        "alternativas": ["Amazon Macie", "Amazon Inspector", "AWS CloudTrail", "Amazon Detective"],
        "correta": "Amazon Macie",
        "explicacao": "O Amazon Macie usa machine learning e correspondência de padrões para descobrir e proteger dados sensíveis armazenados no Amazon S3."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma instância EC2 de produção foi encerrada e a equipe precisa descobrir qual usuário fez essa ação e quando. Qual serviço fornece essa informação?",
        "alternativas": ["AWS CloudTrail", "Amazon CloudWatch", "AWS Config", "AWS Trusted Advisor"],
        "correta": "AWS CloudTrail",
        "explicacao": "O AWS CloudTrail registra as chamadas de API feitas na conta, incluindo quem fez a ação, quando, de qual endereço IP e quais recursos foram afetados."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma empresa precisa manter o histórico de alterações de configuração dos seus recursos e avaliar se eles continuam em conformidade com regras internas. Qual serviço deve ser utilizado?",
        "alternativas": ["AWS Config", "AWS CloudTrail", "Amazon GuardDuty", "AWS Artifact"],
        "correta": "AWS Config",
        "explicacao": "O AWS Config registra as configurações dos recursos ao longo do tempo e avalia continuamente sua conformidade com regras definidas pela empresa."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual serviço permite criar e gerenciar chaves criptográficas e controlar seu uso em diversos serviços da AWS?",
        "alternativas": ["AWS Key Management Service (AWS KMS)", "AWS Certificate Manager", "AWS Secrets Manager", "AWS IAM"],
        "correta": "AWS Key Management Service (AWS KMS)",
        "explicacao": "O AWS KMS facilita a criação e o controle das chaves usadas para criptografar dados e é integrado à maioria dos serviços da AWS, como S3, EBS e RDS."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Por exigência regulatória, uma empresa precisa armazenar suas chaves de criptografia em um módulo de segurança de hardware (HSM) dedicado, de inquilino único e sob seu controle exclusivo. Qual serviço atende a esse requisito?",
        "alternativas": ["AWS CloudHSM", "AWS KMS com chaves gerenciadas pela AWS", "AWS Secrets Manager", "AWS Certificate Manager"],
        "correta": "AWS CloudHSM",
        "explicacao": "O AWS CloudHSM fornece HSMs dedicados na nuvem, nos quais o cliente gerencia as próprias chaves com controle exclusivo, atendendo a requisitos rigorosos de conformidade."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma aplicação usa usuário e senha para acessar um banco de dados, e a empresa quer armazenar essas credenciais com segurança e rotacioná-las automaticamente. Qual serviço é o mais adequado?",
        "alternativas": ["AWS Secrets Manager", "AWS Certificate Manager", "Amazon Macie", "AWS Artifact"],
        "correta": "AWS Secrets Manager",
        "explicacao": "O AWS Secrets Manager armazena segredos como credenciais de banco de dados e chaves de API, permitindo rotação automática sem precisar alterar o código da aplicação."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual serviço permite provisionar, gerenciar e renovar automaticamente certificados SSL/TLS para uso com o Elastic Load Balancing e o Amazon CloudFront?",
        "alternativas": ["AWS Certificate Manager (ACM)", "AWS KMS", "AWS CloudHSM", "AWS Secrets Manager"],
        "correta": "AWS Certificate Manager (ACM)",
        "explicacao": "O ACM provisiona e renova certificados SSL/TLS públicos e privados; os certificados públicos usados com serviços integrados não têm custo adicional."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual recurso atua como um firewall virtual no nível da instância EC2, é stateful e permite configurar apenas regras de permissão?",
        "alternativas": ["Security group", "Network ACL", "AWS WAF", "Tabela de rotas"],
        "correta": "Security group",
        "explicacao": "Security groups controlam o tráfego de entrada e saída das instâncias. Por serem stateful, o tráfego de resposta é liberado automaticamente; só aceitam regras de permissão (allow)."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma empresa precisa bloquear explicitamente um endereço IP específico no nível da sub-rede da VPC. Qual recurso deve ser usado?",
        "alternativas": ["Network ACL", "Security group", "Grupo do IAM", "Internet gateway"],
        "correta": "Network ACL",
        "explicacao": "As Network ACLs atuam no nível da sub-rede, são stateless e aceitam regras de permissão e de negação (deny), permitindo bloquear endereços IP específicos."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Após um alerta de segurança, a equipe precisa investigar e visualizar a causa raiz de uma atividade suspeita, analisando relações entre recursos, usuários e eventos. Qual serviço é o mais adequado?",
        "alternativas": ["Amazon Detective", "AWS Artifact", "AWS Shield", "AWS Certificate Manager"],
        "correta": "Amazon Detective",
        "explicacao": "O Amazon Detective coleta dados de logs automaticamente e usa análise de grafos para ajudar a investigar a causa raiz de possíveis problemas de segurança."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma empresa quer uma visão centralizada dos alertas de segurança de serviços como GuardDuty, Inspector e Macie, além de verificações automáticas de boas práticas de segurança. Qual serviço oferece isso?",
        "alternativas": ["AWS Security Hub", "AWS CloudTrail", "Amazon CloudWatch", "AWS Organizations"],
        "correta": "AWS Security Hub",
        "explicacao": "O AWS Security Hub reúne e prioriza descobertas de segurança de vários serviços da AWS e de parceiros, e executa verificações contínuas com base em padrões de boas práticas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Em qual formato são escritas as políticas de permissão do AWS IAM?",
        "alternativas": ["JSON", "XML", "YAML", "CSV"],
        "correta": "JSON",
        "explicacao": "As políticas do IAM são documentos JSON compostos por declarações com elementos como Effect, Action, Resource e Condition."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Desde janeiro de 2023, os novos objetos enviados ao Amazon S3 são criptografados em repouso por padrão. Qual opção de criptografia é aplicada automaticamente?",
        "alternativas": ["Criptografia no lado do servidor com chaves gerenciadas pelo Amazon S3 (SSE-S3)", "Criptografia no lado do servidor com chaves fornecidas pelo cliente (SSE-C)", "Criptografia no lado do cliente", "Nenhuma: os objetos só são criptografados se o cliente configurar"],
        "correta": "Criptografia no lado do servidor com chaves gerenciadas pelo Amazon S3 (SSE-S3)",
        "explicacao": "O Amazon S3 aplica a SSE-S3 como nível básico de criptografia a todos os novos objetos, sem custo adicional. O cliente pode optar por outras opções, como SSE-KMS."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual serviço analisa a conta e recomenda melhorias como habilitar MFA no usuário raiz, fechar portas abertas em security groups e revisar buckets do S3 com acesso público?",
        "alternativas": ["AWS Trusted Advisor", "AWS Artifact", "AWS Cost Explorer", "Amazon Detective"],
        "correta": "AWS Trusted Advisor",
        "explicacao": "O AWS Trusted Advisor inspeciona o ambiente e oferece recomendações de boas práticas em categorias como segurança, otimização de custos, performance, tolerância a falhas e limites de serviço."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma empresa quer identificar quais de seus recursos, como buckets do S3 e funções do IAM, estão compartilhados com entidades fora da sua conta ou organização. Qual recurso deve ser usado?",
        "alternativas": ["IAM Access Analyzer", "AWS Artifact", "Amazon Inspector", "AWS Budgets"],
        "correta": "IAM Access Analyzer",
        "explicacao": "O IAM Access Analyzer analisa as políticas de recursos e identifica aqueles que podem ser acessados por entidades externas, ajudando a evitar acessos não intencionais."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma empresa está criando um aplicativo móvel e precisa de cadastro, login e gerenciamento de usuários finais, inclusive com login via Google e Facebook. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Cognito", "AWS IAM Identity Center", "AWS Organizations", "Grupos do IAM"],
        "correta": "Amazon Cognito",
        "explicacao": "O Amazon Cognito oferece autenticação, autorização e gerenciamento de usuários para aplicações web e móveis, com suporte a provedores de identidade sociais e corporativos."
    },

    # =====================================================================
    # DOMÍNIO 3: TECNOLOGIA E SERVIÇOS
    # =====================================================================
    {
        "dominio_id": 3,
        "template_pergunta": "Qual serviço da AWS fornece uma camada de armazenamento de arquivos em rede totalmente gerenciada, que pode ser montada simultaneamente por centenas de instâncias EC2 e servidores on-premises?",
        "alternativas": ["Amazon EBS", "Amazon S3", "Amazon EFS", "Amazon Instance Store"],
        "correta": "Amazon EFS",
        "explicacao": "O Amazon EFS fornece um sistema de arquivos Linux compartilhado via protocolo NFS que permite conexões simultâneas."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma instância EC2 precisa de um disco persistente de armazenamento em bloco para executar um banco de dados, mantendo os dados mesmo quando a instância é interrompida. Qual serviço deve ser usado?",
        "alternativas": ["Amazon EBS", "Amazon S3", "Amazon S3 Glacier", "Armazenamento de instância (instance store)"],
        "correta": "Amazon EBS",
        "explicacao": "O Amazon EBS fornece volumes de armazenamento em bloco persistentes para instâncias EC2 dentro de uma Zona de Disponibilidade. O instance store é temporário e perde os dados quando a instância é interrompida."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa precisa guardar registros por 10 anos por motivos legais, raramente os acessa e aceita aguardar até 12 horas para recuperá-los. Qual classe de armazenamento do S3 tem o menor custo?",
        "alternativas": ["S3 Glacier Deep Archive", "S3 Standard", "S3 Standard-IA", "S3 Intelligent-Tiering"],
        "correta": "S3 Glacier Deep Archive",
        "explicacao": "O S3 Glacier Deep Archive é a classe de menor custo do S3, ideal para retenção de longo prazo de dados raramente acessados, com recuperação em até 12 horas."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa armazena dados no S3 com padrões de acesso imprevisíveis e quer otimizar custos automaticamente, sem impacto na performance. Qual classe de armazenamento é a mais indicada?",
        "alternativas": ["S3 Intelligent-Tiering", "S3 Glacier Deep Archive", "S3 One Zone-IA", "S3 Standard"],
        "correta": "S3 Intelligent-Tiering",
        "explicacao": "O S3 Intelligent-Tiering move automaticamente os objetos entre níveis de acesso conforme o uso, reduzindo custos para dados com padrões de acesso desconhecidos ou variáveis."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Arquivos de backup são acessados poucas vezes por mês, mas precisam estar disponíveis imediatamente quando solicitados e resistir à perda de uma Zona de Disponibilidade. Qual classe do S3 é a mais adequada?",
        "alternativas": ["S3 Standard-IA", "S3 One Zone-IA", "S3 Glacier Deep Archive", "S3 Express One Zone"],
        "correta": "S3 Standard-IA",
        "explicacao": "O S3 Standard-IA (acesso infrequente) tem custo de armazenamento menor que o Standard, acesso em milissegundos e armazena os dados em várias Zonas de Disponibilidade."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa quer executar código em resposta ao envio de arquivos para o S3, sem provisionar ou gerenciar servidores e pagando apenas pelo tempo de execução. Qual serviço deve ser utilizado?",
        "alternativas": ["AWS Lambda", "Amazon EC2", "Amazon Lightsail", "AWS Elastic Beanstalk"],
        "correta": "AWS Lambda",
        "explicacao": "O AWS Lambda é um serviço de computação serverless que executa código em resposta a eventos, escala automaticamente e cobra pelo número de requisições e pelo tempo de execução."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual serviço ajusta automaticamente o número de instâncias EC2 de uma aplicação de acordo com a demanda e substitui instâncias com falha?",
        "alternativas": ["Amazon EC2 Auto Scaling", "Elastic Load Balancing", "Amazon CloudWatch", "AWS CloudFormation"],
        "correta": "Amazon EC2 Auto Scaling",
        "explicacao": "O Amazon EC2 Auto Scaling adiciona ou remove instâncias com base em políticas e métricas, mantendo a capacidade desejada e a disponibilidade da aplicação."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual serviço distribui automaticamente o tráfego de entrada da aplicação entre várias instâncias EC2 em diferentes Zonas de Disponibilidade?",
        "alternativas": ["Elastic Load Balancing", "Amazon Route 53", "Amazon CloudFront", "AWS Global Accelerator"],
        "correta": "Elastic Load Balancing",
        "explicacao": "O Elastic Load Balancing distribui o tráfego entre vários destinos, como instâncias EC2, contêineres e endereços IP, e envia requisições apenas para destinos saudáveis."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa quer um banco de dados relacional MySQL gerenciado, com backups automáticos e aplicação de patches feita pela AWS. Qual serviço deve ser escolhido?",
        "alternativas": ["Amazon RDS", "Amazon DynamoDB", "Amazon Redshift", "Amazon ElastiCache"],
        "correta": "Amazon RDS",
        "explicacao": "O Amazon RDS é um serviço gerenciado de banco de dados relacional compatível com MySQL, PostgreSQL, MariaDB, Oracle e SQL Server, que automatiza backups, patches e alta disponibilidade."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual banco de dados relacional da AWS é compatível com MySQL e PostgreSQL, foi criado para a nuvem e replica os dados em seis cópias distribuídas por três Zonas de Disponibilidade?",
        "alternativas": ["Amazon Aurora", "Amazon DynamoDB", "Amazon Neptune", "Amazon DocumentDB"],
        "correta": "Amazon Aurora",
        "explicacao": "O Amazon Aurora combina a performance de bancos comerciais com o custo de bancos de código aberto e mantém seis cópias dos dados em três Zonas de Disponibilidade."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação de jogos precisa de um banco de dados NoSQL de chave-valor, totalmente gerenciado e serverless, com latência de milissegundos de um dígito em qualquer escala. Qual serviço é o mais indicado?",
        "alternativas": ["Amazon DynamoDB", "Amazon RDS", "Amazon Redshift", "Amazon Aurora"],
        "correta": "Amazon DynamoDB",
        "explicacao": "O Amazon DynamoDB é um banco de dados NoSQL de chave-valor e documentos, serverless e totalmente gerenciado, com performance de milissegundos de um dígito em qualquer escala."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa precisa de um data warehouse para executar consultas analíticas complexas sobre petabytes de dados históricos de vendas. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Redshift", "Amazon DynamoDB", "Amazon RDS", "Amazon ElastiCache"],
        "correta": "Amazon Redshift",
        "explicacao": "O Amazon Redshift é um data warehouse gerenciado em escala de petabytes, otimizado para consultas analíticas (OLAP) em grandes volumes de dados."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Para reduzir a carga no banco de dados e acelerar a leitura de dados acessados com frequência, uma empresa quer adicionar um cache em memória compatível com Redis. Qual serviço deve ser usado?",
        "alternativas": ["Amazon ElastiCache", "Amazon S3", "Amazon EBS", "Amazon Redshift"],
        "correta": "Amazon ElastiCache",
        "explicacao": "O Amazon ElastiCache é um serviço de cache em memória totalmente gerenciado, compatível com Valkey, Redis OSS e Memcached, que reduz a latência das leituras para microssegundos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um portal de vídeos quer entregar conteúdo estático e streaming com baixa latência para usuários do mundo todo, usando cache em locais de borda. Qual serviço deve ser usado?",
        "alternativas": ["Amazon CloudFront", "Amazon Route 53", "AWS Direct Connect", "Elastic Load Balancing"],
        "correta": "Amazon CloudFront",
        "explicacao": "O Amazon CloudFront é a rede de entrega de conteúdo (CDN) da AWS, que armazena conteúdo em cache nos pontos de presença (edge locations) próximos aos usuários."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual serviço da AWS oferece registro de domínios, resolução DNS e verificações de saúde para direcionar usuários às aplicações?",
        "alternativas": ["Amazon Route 53", "Amazon CloudFront", "Amazon VPC", "AWS Global Accelerator"],
        "correta": "Amazon Route 53",
        "explicacao": "O Amazon Route 53 é um serviço de DNS altamente disponível e escalável, que também permite registrar domínios e rotear o tráfego com base em políticas e verificações de saúde."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual serviço permite criar uma rede virtual logicamente isolada na AWS, com controle sobre faixas de IP, sub-redes, tabelas de rotas e gateways?",
        "alternativas": ["Amazon VPC", "AWS Direct Connect", "Amazon Route 53", "AWS Transit Gateway"],
        "correta": "Amazon VPC",
        "explicacao": "A Amazon VPC (Virtual Private Cloud) permite definir uma rede virtual isolada, na qual se lançam recursos da AWS com controle total do ambiente de rede."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa precisa de uma conexão de rede privada e dedicada entre seu data center e a AWS, com largura de banda consistente e sem trafegar pela internet pública. Qual serviço atende a esse requisito?",
        "alternativas": ["AWS Direct Connect", "AWS Site-to-Site VPN", "Internet gateway", "Amazon CloudFront"],
        "correta": "AWS Direct Connect",
        "explicacao": "O AWS Direct Connect estabelece uma conexão física dedicada entre o ambiente on-premises e a AWS, oferecendo performance de rede mais previsível do que conexões pela internet."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa precisa conectar rapidamente seu escritório à VPC por meio de um túnel criptografado pela internet, com baixo custo inicial. Qual opção é a mais adequada?",
        "alternativas": ["AWS Site-to-Site VPN", "AWS Direct Connect", "VPC peering", "NAT gateway"],
        "correta": "AWS Site-to-Site VPN",
        "explicacao": "O AWS Site-to-Site VPN cria túneis IPsec criptografados pela internet entre a rede local e a AWS, podendo ser configurado em pouco tempo."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Como é definida uma Zona de Disponibilidade na infraestrutura global da AWS?",
        "alternativas": ["Um ou mais data centers distintos com energia, rede e conectividade redundantes dentro de uma Região", "Um ponto de presença usado para cache de conteúdo", "Uma área geográfica que contém várias Regiões", "Um único servidor físico dedicado a um cliente"],
        "correta": "Um ou mais data centers distintos com energia, rede e conectividade redundantes dentro de uma Região",
        "explicacao": "Cada Região da AWS é composta por várias Zonas de Disponibilidade isoladas fisicamente, conectadas entre si por redes de baixa latência."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual componente da infraestrutura global da AWS é usado pelo Amazon CloudFront para armazenar conteúdo em cache perto dos usuários finais?",
        "alternativas": ["Pontos de presença (edge locations)", "Zonas de Disponibilidade", "Regiões", "AWS Outposts"],
        "correta": "Pontos de presença (edge locations)",
        "explicacao": "Os pontos de presença estão distribuídos em centenas de cidades e são usados por serviços como CloudFront e Route 53 para reduzir a latência para os usuários."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Por requisitos de baixa latência e residência de dados, uma empresa precisa executar serviços da AWS dentro de seu próprio data center, usando as mesmas APIs e ferramentas. Qual serviço atende a essa necessidade?",
        "alternativas": ["AWS Outposts", "AWS Snowball Edge", "AWS Direct Connect", "AWS Storage Gateway"],
        "correta": "AWS Outposts",
        "explicacao": "O AWS Outposts leva a infraestrutura e os serviços da AWS para as instalações do cliente, oferecendo uma experiência híbrida consistente."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa executa processamentos em lote tolerantes a interrupções e com horários flexíveis, e quer o maior desconto possível no Amazon EC2. Qual opção de compra é a mais indicada?",
        "alternativas": ["Instâncias Spot", "Instâncias sob demanda", "Hosts dedicados", "Instâncias reservadas com pagamento adiantado"],
        "correta": "Instâncias Spot",
        "explicacao": "As Instâncias Spot usam capacidade ociosa do EC2 com descontos de até 90% em relação ao sob demanda, mas podem ser interrompidas pela AWS com aviso de dois minutos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma equipe quer executar contêineres sem precisar provisionar, configurar ou escalar servidores ou clusters de máquinas virtuais. Qual serviço deve ser usado?",
        "alternativas": ["AWS Fargate", "Amazon EC2", "AWS Outposts", "Amazon Lightsail"],
        "correta": "AWS Fargate",
        "explicacao": "O AWS Fargate é um mecanismo de computação serverless para contêineres que funciona com o Amazon ECS e o Amazon EKS, eliminando o gerenciamento de servidores."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa já usa Kubernetes on-premises e quer executar seus clusters na AWS com o plano de controle gerenciado pela AWS. Qual serviço deve ser escolhido?",
        "alternativas": ["Amazon EKS", "Amazon ECS", "AWS Lambda", "AWS Batch"],
        "correta": "Amazon EKS",
        "explicacao": "O Amazon Elastic Kubernetes Service (EKS) é um serviço gerenciado e certificado de Kubernetes. O Amazon ECS é o orquestrador de contêineres próprio da AWS."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação precisa armazenar mensagens em uma fila até que um processo de back-end esteja disponível para consumi-las. Qual serviço atende a esse requisito?",
        "alternativas": ["Amazon SQS", "Amazon SNS", "Amazon EventBridge", "Amazon Kinesis Video Streams"],
        "correta": "Amazon SQS",
        "explicacao": "O Amazon Simple Queue Service (SQS) é um serviço de filas de mensagens totalmente gerenciado que permite desacoplar e escalar microsserviços e aplicações distribuídas."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa quer enviar a mesma notificação, ao mesmo tempo, para vários assinantes por e-mail, SMS e para funções Lambda, no modelo publicação/assinatura (pub/sub). Qual serviço deve ser usado?",
        "alternativas": ["Amazon SNS", "Amazon SQS", "Amazon SES", "AWS Step Functions"],
        "correta": "Amazon SNS",
        "explicacao": "O Amazon Simple Notification Service (SNS) usa tópicos para enviar mensagens a vários assinantes simultaneamente, como e-mail, SMS, filas SQS e funções Lambda."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma equipe quer coletar métricas de uso de CPU das instâncias EC2 e receber um alarme quando o uso passar de 80%. Qual serviço deve ser utilizado?",
        "alternativas": ["Amazon CloudWatch", "AWS CloudTrail", "AWS Config", "AWS Trusted Advisor"],
        "correta": "Amazon CloudWatch",
        "explicacao": "O Amazon CloudWatch coleta métricas, logs e eventos dos recursos e aplicações, permitindo criar painéis e alarmes que disparam ações automáticas."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa quer descrever toda a sua infraestrutura em arquivos de modelo (templates) para criá-la de forma repetível e padronizada em várias contas e Regiões. Qual serviço deve ser usado?",
        "alternativas": ["AWS CloudFormation", "AWS Config", "Amazon CloudWatch", "AWS Systems Manager"],
        "correta": "AWS CloudFormation",
        "explicacao": "O AWS CloudFormation implementa infraestrutura como código: os recursos são descritos em templates JSON ou YAML e provisionados de forma automatizada e consistente."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma equipe de ciência de dados precisa de um serviço gerenciado para criar, treinar e implantar modelos de machine learning personalizados. Qual serviço deve ser escolhido?",
        "alternativas": ["Amazon SageMaker AI", "Amazon Rekognition", "Amazon Polly", "Amazon Athena"],
        "correta": "Amazon SageMaker AI",
        "explicacao": "O Amazon SageMaker AI oferece ferramentas para todo o ciclo de vida de machine learning: preparação de dados, treinamento, ajuste e implantação de modelos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa quer identificar automaticamente objetos, pessoas e textos em imagens e vídeos sem desenvolver seus próprios modelos de machine learning. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Rekognition", "Amazon Polly", "Amazon Comprehend", "Amazon Lex"],
        "correta": "Amazon Rekognition",
        "explicacao": "O Amazon Rekognition é um serviço de visão computacional que analisa imagens e vídeos para detectar objetos, rostos, textos e conteúdo impróprio."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um analista quer executar consultas SQL diretamente sobre arquivos armazenados no Amazon S3, sem carregar os dados em um banco e sem gerenciar servidores. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Athena", "Amazon Redshift", "Amazon RDS", "Amazon DynamoDB"],
        "correta": "Amazon Athena",
        "explicacao": "O Amazon Athena é um serviço de consulta interativa serverless que analisa dados no S3 usando SQL padrão, cobrando pela quantidade de dados verificados."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa quer que seus servidores on-premises continuem acessando arquivos localmente, enquanto os dados são armazenados de forma durável na nuvem da AWS. Qual serviço permite essa integração híbrida?",
        "alternativas": ["AWS Storage Gateway", "AWS Snowball Edge", "Amazon EFS", "AWS Outposts"],
        "correta": "AWS Storage Gateway",
        "explicacao": "O AWS Storage Gateway é um serviço de armazenamento híbrido que dá às aplicações on-premises acesso a armazenamento na nuvem, com cache local para baixa latência."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Instâncias EC2 em uma sub-rede privada precisam baixar atualizações da internet, mas não podem receber conexões iniciadas pela internet. Qual recurso deve ser usado?",
        "alternativas": ["NAT gateway", "Internet gateway associado diretamente à sub-rede privada", "VPC peering", "AWS Direct Connect"],
        "correta": "NAT gateway",
        "explicacao": "O NAT gateway permite que instâncias em sub-redes privadas iniciem conexões de saída para a internet, impedindo que conexões externas sejam iniciadas em direção a elas."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma empresa quer converter textos em fala natural para criar versões em áudio dos seus artigos. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Polly", "Amazon Transcribe", "Amazon Translate", "Amazon Textract"],
        "correta": "Amazon Polly",
        "explicacao": "O Amazon Polly converte texto em fala realista. O Transcribe faz o inverso (fala em texto), o Translate traduz idiomas e o Textract extrai texto de documentos."
    },

    # =====================================================================
    # DOMÍNIO 4: FATURAMENTO, PREÇOS E SUPORTE
    # =====================================================================
    {
        "dominio_id": 4,
        "template_pergunta": "Uma empresa precisa receber alertas automáticos quando seus custos mensais estimados com serviços AWS ultrapassarem um limite pré-definido. Qual recurso deve ser configurado?",
        "alternativas": ["AWS Trusted Advisor", "AWS Budgets", "Cost Explorer", "AWS Pricing Calculator"],
        "correta": "AWS Budgets",
        "explicacao": "O AWS Budgets permite configurar orçamentos personalizados e disparar alertas quando os custos previstos ou reais excedem o limite estabelecido."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Um gestor financeiro quer visualizar e analisar os gastos com a AWS dos últimos 12 meses, agrupados por serviço, e obter uma previsão de custos futuros. Qual ferramenta deve ser usada?",
        "alternativas": ["AWS Cost Explorer", "AWS Pricing Calculator", "AWS Artifact", "AWS Organizations"],
        "correta": "AWS Cost Explorer",
        "explicacao": "O AWS Cost Explorer oferece uma interface para visualizar, entender e gerenciar os custos e o uso da AWS ao longo do tempo, incluindo previsões."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Antes de migrar, uma empresa quer estimar quanto vai pagar por mês pela arquitetura que pretende criar na AWS. Qual ferramenta deve ser usada?",
        "alternativas": ["AWS Pricing Calculator", "AWS Cost Explorer", "AWS Budgets", "AWS Billing Conductor"],
        "correta": "AWS Pricing Calculator",
        "explicacao": "A AWS Pricing Calculator permite modelar soluções e estimar seus custos antes de criar qualquer recurso. O Cost Explorer analisa gastos já realizados."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual plano do AWS Support inclui um Technical Account Manager (TAM) designado e tempo de resposta de 15 minutos para casos críticos de negócio?",
        "alternativas": ["Enterprise", "Business", "Developer", "Basic"],
        "correta": "Enterprise",
        "explicacao": "O plano Enterprise inclui um TAM designado, que atua de forma proativa com o cliente, e resposta em até 15 minutos para casos críticos de negócio."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "O que está incluído no plano Basic do AWS Support, disponível sem custo adicional para todos os clientes?",
        "alternativas": ["AWS Health Dashboard e as verificações principais do AWS Trusted Advisor", "Suporte técnico 24x7 por telefone com engenheiros", "Um Technical Account Manager designado", "Orientação arquitetural para casos de uso específicos"],
        "correta": "AWS Health Dashboard e as verificações principais do AWS Trusted Advisor",
        "explicacao": "O plano Basic oferece atendimento ao cliente para dúvidas de conta e faturamento, documentação, fóruns, o AWS Health Dashboard e as verificações principais do Trusted Advisor, mas não inclui suporte técnico."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma empresa executa uma aplicação com uso estável e previsível 24 horas por dia e pode se comprometer com um valor de uso por 3 anos. Qual opção reduz mais os custos de computação?",
        "alternativas": ["Savings Plans com compromisso de 3 anos", "Instâncias sob demanda", "Instâncias Spot", "Hosts dedicados sob demanda"],
        "correta": "Savings Plans com compromisso de 3 anos",
        "explicacao": "Savings Plans e Instâncias Reservadas oferecem grandes descontos em troca de um compromisso de 1 ou 3 anos, sendo ideais para cargas estáveis. As Spot não são indicadas para cargas que não toleram interrupções."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma empresa precisa usar suas licenças de software existentes, vinculadas a soquetes e núcleos físicos, em servidores físicos dedicados exclusivamente a ela. Qual opção do EC2 atende a esse requisito?",
        "alternativas": ["Hosts dedicados", "Instâncias Spot", "Instâncias sob demanda em locação compartilhada", "Savings Plans de computação"],
        "correta": "Hosts dedicados",
        "explicacao": "Os Hosts dedicados são servidores físicos totalmente dedicados ao cliente, com visibilidade de soquetes e núcleos, permitindo usar licenças vinculadas ao servidor (BYOL)."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma empresa com várias contas da AWS quer receber uma única fatura e somar o uso de todas as contas para obter descontos por volume. Qual recurso deve ser usado?",
        "alternativas": ["Faturamento consolidado do AWS Organizations", "AWS Cost Explorer", "AWS Budgets", "Tags de alocação de custos"],
        "correta": "Faturamento consolidado do AWS Organizations",
        "explicacao": "O faturamento consolidado reúne as cobranças de todas as contas da organização em uma única fatura e combina o uso para aplicar descontos por volume."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma empresa quer identificar na fatura da AWS quanto cada departamento (Marketing, Vendas, TI) gasta com recursos. Qual prática deve ser adotada?",
        "alternativas": ["Aplicar tags de alocação de custos aos recursos", "Criar um usuário do IAM para cada departamento", "Usar uma única conta com um só orçamento", "Contratar o plano de suporte Enterprise"],
        "correta": "Aplicar tags de alocação de custos aos recursos",
        "explicacao": "Tags de alocação de custos, depois de ativadas, permitem organizar e filtrar os custos por projeto, departamento ou centro de custo nos relatórios de faturamento."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Em geral, qual tipo de transferência de dados NÃO é cobrado pela AWS?",
        "alternativas": ["Transferência de dados de entrada, da internet para a AWS", "Transferência de dados de saída, da AWS para a internet", "Transferência de dados entre Regiões diferentes", "Transferência de dados entre Zonas de Disponibilidade"],
        "correta": "Transferência de dados de entrada, da internet para a AWS",
        "explicacao": "Na maioria dos serviços, a entrada de dados vinda da internet não é cobrada. A saída para a internet e a transferência entre Regiões ou Zonas de Disponibilidade geralmente são cobradas."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma empresa quer encontrar, comprar e implantar rapidamente um software de segurança de um fornecedor terceiro, com cobrança incluída na fatura da AWS. Onde ela deve procurar?",
        "alternativas": ["AWS Marketplace", "AWS Artifact", "AWS Partner Network", "AWS re:Post"],
        "correta": "AWS Marketplace",
        "explicacao": "O AWS Marketplace é um catálogo digital com milhares de softwares de fornecedores independentes, que podem ser comprados e implantados com cobrança na própria fatura da AWS."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma empresa suspeita que suas instâncias EC2 estão superdimensionadas e quer recomendações de tamanhos mais adequados com base no histórico de uso. Qual serviço deve ser usado?",
        "alternativas": ["AWS Compute Optimizer", "AWS Pricing Calculator", "AWS Artifact", "Amazon Inspector"],
        "correta": "AWS Compute Optimizer",
        "explicacao": "O AWS Compute Optimizer analisa métricas de uso com machine learning e recomenda configurações ideais para EC2, Auto Scaling, EBS, Lambda e outros recursos, reduzindo custos."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma empresa sem experiência em nuvem quer contratar uma consultoria certificada pela AWS para planejar e executar sua migração. Qual recurso ajuda a encontrar esse tipo de empresa?",
        "alternativas": ["AWS Partner Network (APN)", "AWS Marketplace", "AWS Trusted Advisor", "AWS Health Dashboard"],
        "correta": "AWS Partner Network (APN)",
        "explicacao": "A AWS Partner Network reúne empresas de consultoria e tecnologia validadas pela AWS, que podem ajudar os clientes a projetar, migrar e gerenciar suas cargas de trabalho."
    },
]
