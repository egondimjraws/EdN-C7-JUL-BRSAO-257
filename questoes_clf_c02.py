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
        "template_pergunta": "A lojinha do Alyson deseja migrar para a nuvem da AWS para transformar custos fixos de TI em custos variáveis baseados no uso real. Qual vantagem do Cloud Computing isso representa?",
        "alternativas": ["Aumentar a elasticidade para atender picos de demanda", "Ganhar agilidade no provisionamento de novos recursos de TI", "Trocar despesas de capital por despesas operacionais", "Economia de escala"],
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
        "template_pergunta": "A lojinha do Alyson costumava comprar servidores em excesso para suportar picos de acesso que raramente aconteciam. Ao migrar para a AWS, ela passou a provisionar recursos conforme a demanda real. Qual vantagem da nuvem foi obtida?",
        "alternativas": ["Parar de adivinhar a capacidade", "Economia de escala", "Parar de gastar dinheiro com a manutenção de data centers", "Tornar-se global em minutos com várias Regiões"],
        "correta": "Parar de adivinhar a capacidade",
        "explicacao": "Na nuvem não é preciso estimar a capacidade com antecedência: é possível aumentar ou reduzir os recursos conforme a necessidade, evitando ociosidade ou falta de capacidade."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma equipe de desenvolvimento passou a criar ambientes de teste em minutos, em vez de esperar semanas pela compra de hardware. Qual vantagem da nuvem isso representa?",
        "alternativas": ["Aumentar a velocidade e a agilidade", "Economia de escala", "Alta disponibilidade em várias Zonas de Disponibilidade", "Trocar despesas de capital por despesas operacionais"],
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
        "template_pergunta": "A lojinha do Alyson quer automatizar mudanças, responder a eventos e definir padrões para gerenciar suas operações diárias na AWS. Qual pilar do Well-Architected Framework trata desses objetivos?",
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
        "template_pergunta": "A lojinha do Alyson quer usar os recursos de computação de forma eficiente, adotando tecnologias como serverless e experimentando novos tipos de instância conforme a demanda evolui. Qual pilar do Well-Architected Framework trata disso?",
        "alternativas": ["Eficiência de performance", "Otimização de custos", "Confiabilidade", "Excelência operacional"],
        "correta": "Eficiência de performance",
        "explicacao": "Eficiência de performance trata do uso eficiente dos recursos para atender aos requisitos, mantendo essa eficiência à medida que a demanda muda e as tecnologias evoluem."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson mantém seu sistema legado no data center próprio e conecta esse ambiente a aplicações executadas na AWS. Qual modelo de implantação de nuvem está sendo usado?",
        "alternativas": ["Híbrido", "Totalmente na nuvem", "On-premises (nuvem privada)", "Multi-região"],
        "correta": "Híbrido",
        "explicacao": "O modelo híbrido conecta a infraestrutura on-premises aos recursos na nuvem, permitindo que as cargas de trabalho sejam distribuídas entre os dois ambientes."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson precisa de controle total sobre o sistema operacional, a rede e o software instalado em seus servidores virtuais na nuvem. Qual modelo de serviço oferece esse nível de controle?",
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
        "template_pergunta": "A lojinha do Alyson precisa migrar rapidamente centenas de servidores para o Amazon EC2 sem fazer nenhuma alteração nas aplicações. Qual estratégia de migração está sendo utilizada?",
        "alternativas": ["Redefinir a hospedagem (rehost)", "Refatorar ou rearquitetar (refactor)", "Recomprar como SaaS (repurchase)", "Aposentar (retire)"],
        "correta": "Redefinir a hospedagem (rehost)",
        "explicacao": "Rehost, conhecido como 'lift and shift', move as aplicações para a nuvem sem alterações, sendo a forma mais rápida de migrar em grande escala."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson vai migrar seu banco de dados MySQL de um servidor próprio para o Amazon RDS, sem alterar o código da aplicação, para reduzir o trabalho de administração. Qual estratégia de migração está sendo aplicada?",
        "alternativas": ["Redefinir a plataforma (replatform)", "Redefinir a hospedagem (rehost)", "Refatorar (refactor)", "Reter (retain)"],
        "correta": "Redefinir a plataforma (replatform)",
        "explicacao": "Replatform ('lift, tinker and shift') faz algumas otimizações para aproveitar a nuvem, como trocar um banco autogerenciado por um serviço gerenciado, sem mudar a arquitetura principal da aplicação."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson decidiu reescrever sua aplicação monolítica como microsserviços serverless para ganhar escalabilidade e agilidade. Qual estratégia de migração é essa?",
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
        "template_pergunta": "A lojinha do Alyson precisa transferir 80 TB de dados para a AWS, mas sua conexão com a internet levaria meses para concluir a cópia. Qual serviço é o mais indicado?",
        "alternativas": ["AWS Snowball Edge", "AWS Direct Connect", "Amazon S3 Transfer Acceleration", "AWS Site-to-Site VPN"],
        "correta": "AWS Snowball Edge",
        "explicacao": "O AWS Snowball Edge é um dispositivo físico enviado ao cliente para transferir grandes volumes de dados offline, evitando a dependência da largura de banda da internet."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer migrar seu banco de dados Oracle on-premises para a AWS mantendo o banco de origem em funcionamento durante a migração, com mínimo tempo de inatividade. Qual serviço deve ser usado?",
        "alternativas": ["AWS Database Migration Service (AWS DMS)", "AWS DataSync", "AWS Snowball Edge Storage Optimized", "AWS Schema Conversion Tool (AWS SCT)"],
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
        "alternativas": ["Distribuir as instâncias em várias Zonas de Disponibilidade", "Executar todas as instâncias em uma única Zona de Disponibilidade", "Usar uma única instância de maior tamanho, com mais CPU e memória", "Armazenar os dados apenas no armazenamento de instância para reduzir a latência"],
        "correta": "Distribuir as instâncias em várias Zonas de Disponibilidade",
        "explicacao": "As Zonas de Disponibilidade são isoladas entre si; distribuir a aplicação entre elas evita que a falha de um data center torne a aplicação indisponível."
    },

    # =====================================================================
    # DOMÍNIO 2: SEGURANÇA E CONFORMIDADE
    # =====================================================================
    {
        "dominio_id": 2,
        "template_pergunta": "De acordo com o Modelo de Responsabilidade Compartilhada da AWS, qual das seguintes opções é uma responsabilidade exclusiva do cliente?",
        "alternativas": ["Segurança física das instalações e controle de acesso aos data centers", "Gerenciamento de patches do sistema operacional convidado", "Manutenção e atualização do software do hipervisor dos hosts", "Descarte seguro de discos rígidos"],
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
        "alternativas": ["Aplicar patches no sistema operacional e no mecanismo do banco de dados", "Criar os usuários do banco de dados e definir as permissões de cada um deles", "Configurar as regras dos security groups do banco", "Decidir se os dados armazenados no banco serão criptografados em repouso"],
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
        "alternativas": ["Associar uma função (role) do IAM à instância", "Gravar as chaves de acesso de um usuário do IAM no código", "Usar as credenciais do usuário raiz configuradas na instância", "Tornar o bucket público para que a instância consiga ler os objetos"],
        "correta": "Associar uma função (role) do IAM à instância",
        "explicacao": "As funções do IAM fornecem credenciais temporárias que são rotacionadas automaticamente, eliminando a necessidade de armazenar chaves de acesso na instância."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson tem 30 desenvolvedores que precisam das mesmas permissões. Qual recurso do IAM simplifica o gerenciamento dessas permissões?",
        "alternativas": ["Grupos do IAM", "Funções vinculadas a serviços", "Políticas de bucket do S3", "Listas de controle de acesso de rede"],
        "correta": "Grupos do IAM",
        "explicacao": "Um grupo do IAM reúne usuários e permite anexar políticas uma única vez; todos os membros herdam essas permissões, facilitando a administração."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson com várias contas na AWS quer impedir que qualquer conta da área de desenvolvimento use serviços fora de uma lista aprovada, inclusive para administradores. Qual recurso deve ser usado?",
        "alternativas": ["Políticas de controle de serviço (SCPs) do AWS Organizations", "Grupos do IAM", "Regras do AWS Config com notificação para os administradores", "Security groups restritivos aplicados em todas as VPCs das contas"],
        "correta": "Políticas de controle de serviço (SCPs) do AWS Organizations",
        "explicacao": "As SCPs definem o máximo de permissões disponível nas contas de uma organização ou unidade organizacional, valendo inclusive para os administradores dessas contas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer que seus funcionários acessem várias contas da AWS e aplicações corporativas com um único login centralizado. Qual serviço atende a esse requisito?",
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
        "template_pergunta": "A lojinha do Alyson quer verificar automaticamente suas instâncias EC2 e imagens de contêiner em busca de vulnerabilidades de software conhecidas. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Inspector", "Amazon GuardDuty", "AWS Shield", "AWS Artifact"],
        "correta": "Amazon Inspector",
        "explicacao": "O Amazon Inspector avalia continuamente instâncias EC2, imagens de contêiner no Amazon ECR e funções Lambda em busca de vulnerabilidades (CVEs) e exposição de rede indesejada."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson precisa descobrir quais buckets do S3 armazenam dados pessoais sensíveis, como números de CPF e cartões de crédito. Qual serviço atende a essa necessidade?",
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
        "template_pergunta": "A lojinha do Alyson precisa manter o histórico de alterações de configuração dos seus recursos e avaliar se eles continuam em conformidade com regras internas. Qual serviço deve ser utilizado?",
        "alternativas": ["AWS Config", "AWS CloudTrail", "Amazon GuardDuty", "AWS Artifact"],
        "correta": "AWS Config",
        "explicacao": "O AWS Config registra as configurações dos recursos ao longo do tempo e avalia continuamente sua conformidade com regras definidas pela empresa."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual serviço permite criar e gerenciar chaves criptográficas e controlar seu uso em diversos serviços da AWS?",
        "alternativas": ["AWS Key Management Service (AWS KMS)", "AWS Certificate Manager", "AWS Secrets Manager", "AWS Identity and Access Management (IAM)"],
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
        "alternativas": ["AWS Certificate Manager (ACM)", "AWS Key Management Service (AWS KMS)", "AWS CloudHSM", "AWS Secrets Manager"],
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
        "template_pergunta": "A lojinha do Alyson precisa bloquear explicitamente um endereço IP específico no nível da sub-rede da VPC. Qual recurso deve ser usado?",
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
        "template_pergunta": "A lojinha do Alyson quer uma visão centralizada dos alertas de segurança de serviços como GuardDuty, Inspector e Macie, além de verificações automáticas de boas práticas de segurança. Qual serviço oferece isso?",
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
        "template_pergunta": "A lojinha do Alyson quer identificar quais de seus recursos, como buckets do S3 e funções do IAM, estão compartilhados com entidades fora da sua conta ou organização. Qual recurso deve ser usado?",
        "alternativas": ["IAM Access Analyzer", "AWS Artifact", "Amazon Inspector", "AWS Budgets"],
        "correta": "IAM Access Analyzer",
        "explicacao": "O IAM Access Analyzer analisa as políticas de recursos e identifica aqueles que podem ser acessados por entidades externas, ajudando a evitar acessos não intencionais."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson está criando um aplicativo móvel e precisa de cadastro, login e gerenciamento de usuários finais, inclusive com login via Google e Facebook. Qual serviço deve ser usado?",
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
        "template_pergunta": "A lojinha do Alyson precisa guardar registros por 10 anos por motivos legais, raramente os acessa e aceita aguardar até 12 horas para recuperá-los. Qual classe de armazenamento do S3 tem o menor custo?",
        "alternativas": ["S3 Glacier Deep Archive", "S3 Standard", "S3 Standard-IA", "S3 Intelligent-Tiering"],
        "correta": "S3 Glacier Deep Archive",
        "explicacao": "O S3 Glacier Deep Archive é a classe de menor custo do S3, ideal para retenção de longo prazo de dados raramente acessados, com recuperação em até 12 horas."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson armazena dados no S3 com padrões de acesso imprevisíveis e quer otimizar custos automaticamente, sem impacto na performance. Qual classe de armazenamento é a mais indicada?",
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
        "template_pergunta": "A lojinha do Alyson quer executar código em resposta ao envio de arquivos para o S3, sem provisionar ou gerenciar servidores e pagando apenas pelo tempo de execução. Qual serviço deve ser utilizado?",
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
        "template_pergunta": "A lojinha do Alyson quer um banco de dados relacional MySQL gerenciado, com backups automáticos e aplicação de patches feita pela AWS. Qual serviço deve ser escolhido?",
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
        "template_pergunta": "A lojinha do Alyson precisa de um data warehouse para executar consultas analíticas complexas sobre petabytes de dados históricos de vendas. Qual serviço deve ser usado?",
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
        "template_pergunta": "A lojinha do Alyson precisa de uma conexão de rede privada e dedicada entre seu data center e a AWS, com largura de banda consistente e sem trafegar pela internet pública. Qual serviço atende a esse requisito?",
        "alternativas": ["AWS Direct Connect", "AWS Site-to-Site VPN", "Internet gateway", "Amazon CloudFront"],
        "correta": "AWS Direct Connect",
        "explicacao": "O AWS Direct Connect estabelece uma conexão física dedicada entre o ambiente on-premises e a AWS, oferecendo performance de rede mais previsível do que conexões pela internet."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson precisa conectar rapidamente seu escritório à VPC por meio de um túnel criptografado pela internet, com baixo custo inicial. Qual opção é a mais adequada?",
        "alternativas": ["AWS Site-to-Site VPN", "AWS Direct Connect", "VPC peering", "NAT gateway"],
        "correta": "AWS Site-to-Site VPN",
        "explicacao": "O AWS Site-to-Site VPN cria túneis IPsec criptografados pela internet entre a rede local e a AWS, podendo ser configurado em pouco tempo."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Como é definida uma Zona de Disponibilidade na infraestrutura global da AWS?",
        "alternativas": ["Um ou mais data centers distintos com energia, rede e conectividade redundantes dentro de uma Região", "Um ponto de presença usado pelo CloudFront para armazenar conteúdo em cache perto dos usuários finais em grandes cidades", "Uma área geográfica isolada que agrupa várias Regiões da AWS em um mesmo continente", "Um único servidor físico dedicado a um cliente"],
        "correta": "Um ou mais data centers distintos com energia, rede e conectividade redundantes dentro de uma Região",
        "explicacao": "Cada Região da AWS é composta por várias Zonas de Disponibilidade isoladas fisicamente, conectadas entre si por redes de baixa latência."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual componente da infraestrutura global da AWS é usado pelo Amazon CloudFront para armazenar conteúdo em cache perto dos usuários finais?",
        "alternativas": ["Pontos de presença (edge locations)", "Zonas de Disponibilidade de cada Região", "Regiões", "Racks do AWS Outposts nas instalações do cliente"],
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
        "template_pergunta": "A lojinha do Alyson executa processamentos em lote tolerantes a interrupções e com horários flexíveis, e quer o maior desconto possível no Amazon EC2. Qual opção de compra é a mais indicada?",
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
        "template_pergunta": "A lojinha do Alyson já usa Kubernetes on-premises e quer executar seus clusters na AWS com o plano de controle gerenciado pela AWS. Qual serviço deve ser escolhido?",
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
        "template_pergunta": "A lojinha do Alyson quer enviar a mesma notificação, ao mesmo tempo, para vários assinantes por e-mail, SMS e para funções Lambda, no modelo publicação/assinatura (pub/sub). Qual serviço deve ser usado?",
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
        "template_pergunta": "A lojinha do Alyson quer descrever toda a sua infraestrutura em arquivos de modelo (templates) para criá-la de forma repetível e padronizada em várias contas e Regiões. Qual serviço deve ser usado?",
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
        "template_pergunta": "A lojinha do Alyson quer identificar automaticamente objetos, pessoas e textos em imagens e vídeos sem desenvolver seus próprios modelos de machine learning. Qual serviço deve ser usado?",
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
        "template_pergunta": "A lojinha do Alyson quer que seus servidores on-premises continuem acessando arquivos localmente, enquanto os dados são armazenados de forma durável na nuvem da AWS. Qual serviço permite essa integração híbrida?",
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
        "template_pergunta": "A lojinha do Alyson quer converter textos em fala natural para criar versões em áudio dos seus artigos. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Polly", "Amazon Transcribe", "Amazon Translate", "Amazon Textract"],
        "correta": "Amazon Polly",
        "explicacao": "O Amazon Polly converte texto em fala realista. O Transcribe faz o inverso (fala em texto), o Translate traduz idiomas e o Textract extrai texto de documentos."
    },

    # =====================================================================
    # DOMÍNIO 4: FATURAMENTO, PREÇOS E SUPORTE
    # =====================================================================
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson precisa receber alertas automáticos quando seus custos mensais estimados com serviços AWS ultrapassarem um limite pré-definido. Qual recurso deve ser configurado?",
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
        "alternativas": ["AWS Health Dashboard e as verificações principais do AWS Trusted Advisor", "Suporte técnico 24x7 por telefone, chat e e-mail com engenheiros de suporte", "Um Technical Account Manager designado para acompanhar a conta de forma proativa", "Orientação arquitetural personalizada para casos de uso específicos da empresa"],
        "correta": "AWS Health Dashboard e as verificações principais do AWS Trusted Advisor",
        "explicacao": "O plano Basic oferece atendimento ao cliente para dúvidas de conta e faturamento, documentação, fóruns, o AWS Health Dashboard e as verificações principais do Trusted Advisor, mas não inclui suporte técnico."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson executa uma aplicação com uso estável e previsível 24 horas por dia e pode se comprometer com um valor de uso por 3 anos. Qual opção reduz mais os custos de computação?",
        "alternativas": ["Savings Plans com compromisso de 3 anos", "Instâncias sob demanda, sem nenhum compromisso", "Instâncias Spot", "Hosts dedicados sob demanda sem compromisso"],
        "correta": "Savings Plans com compromisso de 3 anos",
        "explicacao": "Savings Plans e Instâncias Reservadas oferecem grandes descontos em troca de um compromisso de 1 ou 3 anos, sendo ideais para cargas estáveis. As Spot não são indicadas para cargas que não toleram interrupções."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson precisa usar suas licenças de software existentes, vinculadas a soquetes e núcleos físicos, em servidores físicos dedicados exclusivamente a ela. Qual opção do EC2 atende a esse requisito?",
        "alternativas": ["Hosts dedicados", "Instâncias Spot", "Instâncias sob demanda em locação compartilhada", "Savings Plans de computação"],
        "correta": "Hosts dedicados",
        "explicacao": "Os Hosts dedicados são servidores físicos totalmente dedicados ao cliente, com visibilidade de soquetes e núcleos, permitindo usar licenças vinculadas ao servidor (BYOL)."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson com várias contas da AWS quer receber uma única fatura e somar o uso de todas as contas para obter descontos por volume. Qual recurso deve ser usado?",
        "alternativas": ["Faturamento consolidado do AWS Organizations", "Relatórios mensais por conta no AWS Cost Explorer", "AWS Budgets", "Tags de alocação de custos ativadas em cada conta"],
        "correta": "Faturamento consolidado do AWS Organizations",
        "explicacao": "O faturamento consolidado reúne as cobranças de todas as contas da organização em uma única fatura e combina o uso para aplicar descontos por volume."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson quer identificar na fatura da AWS quanto cada departamento (Marketing, Vendas, TI) gasta com recursos. Qual prática deve ser adotada?",
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
        "template_pergunta": "A lojinha do Alyson quer encontrar, comprar e implantar rapidamente um software de segurança de um fornecedor terceiro, com cobrança incluída na fatura da AWS. Onde ela deve procurar?",
        "alternativas": ["AWS Marketplace", "AWS Artifact", "AWS Partner Network", "AWS re:Post"],
        "correta": "AWS Marketplace",
        "explicacao": "O AWS Marketplace é um catálogo digital com milhares de softwares de fornecedores independentes, que podem ser comprados e implantados com cobrança na própria fatura da AWS."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson suspeita que suas instâncias EC2 estão superdimensionadas e quer recomendações de tamanhos mais adequados com base no histórico de uso. Qual serviço deve ser usado?",
        "alternativas": ["AWS Compute Optimizer", "AWS Pricing Calculator", "AWS Artifact", "Amazon Inspector"],
        "correta": "AWS Compute Optimizer",
        "explicacao": "O AWS Compute Optimizer analisa métricas de uso com machine learning e recomenda configurações ideais para EC2, Auto Scaling, EBS, Lambda e outros recursos, reduzindo custos."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson sem experiência em nuvem quer contratar uma consultoria certificada pela AWS para planejar e executar sua migração. Qual recurso ajuda a encontrar esse tipo de empresa?",
        "alternativas": ["AWS Partner Network (APN)", "AWS Marketplace", "AWS Trusted Advisor", "AWS Health Dashboard"],
        "correta": "AWS Partner Network (APN)",
        "explicacao": "A AWS Partner Network reúne empresas de consultoria e tecnologia validadas pela AWS, que podem ajudar os clientes a projetar, migrar e gerenciar suas cargas de trabalho."
    },
]

# =========================================================================
# AMPLIAÇÃO: DOMÍNIO 1 - CONCEITOS DE NUVEM
# =========================================================================
QUESTOES += [
    {
        "dominio_id": 1,
        "template_pergunta": "Qual opção descreve corretamente a computação em nuvem?",
        "alternativas": ["Entrega sob demanda de recursos de TI pela internet com pagamento conforme o uso", "Aluguel de servidores físicos com contrato mínimo de cinco anos", "Instalação de softwares diretamente nos computadores dos funcionários", "Compra antecipada de hardware para um data center próprio"],
        "correta": "Entrega sob demanda de recursos de TI pela internet com pagamento conforme o uso",
        "explicacao": "Computação em nuvem é a entrega sob demanda de poder computacional, banco de dados, armazenamento, aplicações e outros recursos de TI pela internet, com preço de pagamento conforme o uso."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual modelo de preço da AWS permite pagar apenas pelos recursos consumidos, sem contratos de longo prazo nem pagamentos antecipados?",
        "alternativas": ["Pagamento conforme o uso (pay-as-you-go)", "Licença perpétua com pagamento único na contratação", "Pagamento antecipado obrigatório de três anos", "Taxa fixa mensal cobrada independentemente do uso"],
        "correta": "Pagamento conforme o uso (pay-as-you-go)",
        "explicacao": "No modelo pay-as-you-go o cliente paga somente pelo que usa, pelo tempo que usa, sem compromisso de longo prazo, o que reduz riscos e custos iniciais."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer que sua equipe de TI pare de cuidar de racks, cabeamento, energia e refrigeração para se concentrar em projetos que diferenciam o negócio. Qual vantagem da nuvem atende a esse objetivo?",
        "alternativas": ["Parar de gastar dinheiro com a operação e manutenção de data centers", "Tornar-se global em minutos, usando a infraestrutura em vários continentes", "Parar de adivinhar a capacidade", "Beneficiar-se de enormes economias de escala obtidas pela AWS com milhões de clientes"],
        "correta": "Parar de gastar dinheiro com a operação e manutenção de data centers",
        "explicacao": "Na nuvem, a AWS cuida da infraestrutura física. A empresa deixa de gastar com o trabalho pesado de manter data centers e pode focar em seus clientes e produtos."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Como a AWS chama tarefas como gerenciar servidores, aplicar patches em hardware e manter data centers, que consomem esforço mas não diferenciam o negócio do cliente?",
        "alternativas": ["Trabalho pesado indiferenciado (undifferentiated heavy lifting)", "Excelência operacional", "Computação de borda (edge computing) em pontos de presença da AWS", "Dívida técnica (technical debt) acumulada pela infraestrutura legada"],
        "correta": "Trabalho pesado indiferenciado (undifferentiated heavy lifting)",
        "explicacao": "A AWS usa o termo 'trabalho pesado indiferenciado' para atividades de infraestrutura necessárias, mas que não agregam valor competitivo. Serviços gerenciados eliminam boa parte desse esforço."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual conceito descreve um sistema que permanece operacional e acessível com o mínimo de tempo de inatividade, mesmo durante falhas de componentes?",
        "alternativas": ["Alta disponibilidade", "Elasticidade", "Durabilidade", "Agilidade"],
        "correta": "Alta disponibilidade",
        "explicacao": "Alta disponibilidade é a capacidade de manter o sistema funcionando com o mínimo de interrupções, geralmente usando redundância em várias Zonas de Disponibilidade."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma aplicação continua funcionando sem nenhuma interrupção para os usuários mesmo quando um de seus servidores falha, porque há componentes redundantes assumindo a carga imediatamente. Qual característica é essa?",
        "alternativas": ["Tolerância a falhas", "Elasticidade", "Escalabilidade vertical", "Agilidade"],
        "correta": "Tolerância a falhas",
        "explicacao": "Tolerância a falhas é a capacidade de um sistema continuar operando sem interrupção quando um ou mais componentes falham, graças à redundância."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "O Amazon S3 foi projetado para 99,999999999% (11 noves) de proteção contra a perda de objetos. A qual conceito esse número se refere?",
        "alternativas": ["Durabilidade", "Disponibilidade", "Latência", "Elasticidade"],
        "correta": "Durabilidade",
        "explicacao": "Durabilidade mede a probabilidade de os dados armazenados não serem perdidos. Disponibilidade mede o tempo em que o serviço está acessível para uso."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual conceito descreve a capacidade de um sistema crescer para atender a um aumento de carga de trabalho, adicionando recursos?",
        "alternativas": ["Escalabilidade", "Durabilidade", "Conformidade", "Portabilidade"],
        "correta": "Escalabilidade",
        "explicacao": "Escalabilidade é a capacidade de aumentar recursos para lidar com mais carga, seja adicionando mais instâncias (horizontal) ou aumentando o tamanho delas (vertical)."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma equipe trocou uma instância EC2 t3.medium por uma m5.xlarge, com mais CPU e memória, para suportar mais usuários. Que tipo de escalabilidade foi aplicada?",
        "alternativas": ["Escalabilidade vertical", "Escalabilidade horizontal", "Elasticidade automática", "Tolerância a falhas"],
        "correta": "Escalabilidade vertical",
        "explicacao": "Escalar verticalmente é aumentar a capacidade de um recurso existente, como trocar uma instância por outra maior. Tem limite físico e costuma exigir reinicialização."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual afirmação descreve corretamente a diferença entre escalabilidade e elasticidade?",
        "alternativas": ["Escalabilidade é crescer para atender a mais carga; elasticidade é ajustar os recursos automaticamente para cima e para baixo conforme a demanda", "Escalabilidade é reduzir recursos para economizar custos; elasticidade é comprar hardware antecipadamente para suportar picos de demanda futuros", "Elasticidade exige compra de hardware; escalabilidade não", "Não há diferença: os dois termos significam reduzir custos fixos"],
        "correta": "Escalabilidade é crescer para atender a mais carga; elasticidade é ajustar os recursos automaticamente para cima e para baixo conforme a demanda",
        "explicacao": "Um sistema elástico é escalável e, além disso, libera os recursos quando a demanda cai, evitando pagar por capacidade ociosa."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma lei exige que os dados pessoais de clientes de uma empresa brasileira permaneçam armazenados no Brasil. Qual fator é determinante na escolha da Região da AWS?",
        "alternativas": ["Conformidade e requisitos de residência de dados", "Quantidade de pontos de presença da Região", "Proximidade da sede da AWS nos Estados Unidos", "Número de serviços em versão prévia na Região"],
        "correta": "Conformidade e requisitos de residência de dados",
        "explicacao": "Os quatro fatores principais para escolher uma Região são: conformidade e governança de dados, proximidade dos clientes (latência), disponibilidade de serviços e preço."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson vai lançar um jogo online para usuários do Japão e quer a menor latência possível. Qual critério deve orientar a escolha da Região?",
        "alternativas": ["Proximidade dos usuários finais", "Região com o maior número de serviços", "Região onde a empresa abriu a conta", "Região com o fuso horário da equipe de desenvolvimento"],
        "correta": "Proximidade dos usuários finais",
        "explicacao": "Quanto mais próxima a Região estiver dos usuários, menor tende a ser a latência. Para usuários no Japão, a Região de Tóquio seria uma escolha natural."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson planeja usar um serviço da AWS lançado recentemente e precisa decidir em qual Região implantar sua aplicação. Que fator ela deve verificar?",
        "alternativas": ["Se o serviço está disponível na Região desejada", "Se a Região tem o mesmo fuso horário da equipe de desenvolvimento", "Se a Região usa a mesma moeda e o mesmo idioma da empresa", "Nada: todos os serviços estão disponíveis em todas as Regiões"],
        "correta": "Se o serviço está disponível na Região desejada",
        "explicacao": "Nem todos os serviços e recursos estão disponíveis em todas as Regiões. Novos serviços costumam ser lançados em algumas Regiões primeiro."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Por que o mesmo tipo de instância EC2 pode ter custos diferentes nas Regiões de São Paulo e do Norte da Virgínia?",
        "alternativas": ["Os preços dos serviços variam de acordo com a Região", "A AWS cobra mais de clientes de acordo com a nacionalidade", "O preço depende do número de usuários do IAM da conta", "As instâncias em São Paulo sempre usam hardware de geração anterior"],
        "correta": "Os preços dos serviços variam de acordo com a Região",
        "explicacao": "Custos locais como energia, impostos e infraestrutura fazem os preços variarem entre Regiões. O preço é um dos fatores de escolha da Região."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual ferramenta gratuita permite revisar uma carga de trabalho com base nas boas práticas do AWS Well-Architected Framework e acompanhar os riscos encontrados?",
        "alternativas": ["AWS Well-Architected Tool", "AWS Trusted Advisor", "AWS Config", "AWS Pricing Calculator"],
        "correta": "AWS Well-Architected Tool",
        "explicacao": "A AWS Well-Architected Tool, disponível no console sem custo, guia a revisão das cargas de trabalho com perguntas sobre os seis pilares e gera um plano de melhorias."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Os princípios 'implementar uma base sólida de identidade', 'habilitar a rastreabilidade' e 'aplicar segurança em todas as camadas' pertencem a qual pilar do Well-Architected Framework?",
        "alternativas": ["Segurança", "Confiabilidade", "Excelência operacional", "Eficiência de performance"],
        "correta": "Segurança",
        "explicacao": "O pilar Segurança trata da proteção de dados, sistemas e ativos, com princípios como privilégio mínimo, rastreabilidade, segurança em todas as camadas e proteção de dados em trânsito e em repouso."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Os princípios 'testar os procedimentos de recuperação', 'escalar horizontalmente para aumentar a disponibilidade' e 'parar de adivinhar a capacidade' pertencem a qual pilar do Well-Architected Framework?",
        "alternativas": ["Confiabilidade", "Segurança", "Otimização de custos", "Sustentabilidade"],
        "correta": "Confiabilidade",
        "explicacao": "O pilar Confiabilidade inclui recuperar-se automaticamente de falhas, testar a recuperação, escalar horizontalmente, parar de adivinhar a capacidade e gerenciar mudanças por automação."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Os princípios 'democratizar tecnologias avançadas', 'usar arquiteturas serverless' e 'experimentar com mais frequência' pertencem a qual pilar do Well-Architected Framework?",
        "alternativas": ["Eficiência de performance", "Excelência operacional", "Confiabilidade", "Segurança"],
        "correta": "Eficiência de performance",
        "explicacao": "O pilar Eficiência de performance incentiva consumir tecnologias complexas como serviço, tornar-se global em minutos, usar serverless e experimentar diferentes configurações."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Os princípios 'implementar a gestão financeira da nuvem', 'medir a eficiência geral' e 'analisar e atribuir despesas' pertencem a qual pilar do Well-Architected Framework?",
        "alternativas": ["Otimização de custos", "Eficiência de performance", "Sustentabilidade", "Excelência operacional"],
        "correta": "Otimização de custos",
        "explicacao": "O pilar Otimização de custos inclui adotar um modelo de consumo, medir a eficiência, parar de gastar com trabalho pesado indiferenciado e atribuir despesas aos responsáveis."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Os princípios 'realizar operações como código', 'fazer mudanças frequentes, pequenas e reversíveis' e 'aprender com todas as falhas operacionais' pertencem a qual pilar do Well-Architected Framework?",
        "alternativas": ["Excelência operacional", "Confiabilidade", "Segurança", "Otimização de custos"],
        "correta": "Excelência operacional",
        "explicacao": "O pilar Excelência operacional trata de executar e monitorar sistemas para entregar valor de negócio e melhorar continuamente processos e procedimentos."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Os princípios 'maximizar a utilização dos recursos' e 'usar serviços gerenciados para reduzir a infraestrutura necessária' estão associados principalmente a qual pilar do Well-Architected Framework?",
        "alternativas": ["Sustentabilidade", "Segurança", "Confiabilidade", "Excelência operacional"],
        "correta": "Sustentabilidade",
        "explicacao": "O pilar Sustentabilidade busca reduzir o impacto ambiental, maximizando a utilização, adotando hardware mais eficiente e usando serviços gerenciados que compartilham infraestrutura."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Quantos pilares possui atualmente o AWS Well-Architected Framework?",
        "alternativas": ["Seis", "Quatro", "Cinco", "Sete"],
        "correta": "Seis",
        "explicacao": "Os seis pilares são: Excelência operacional, Segurança, Confiabilidade, Eficiência de performance, Otimização de custos e Sustentabilidade."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma equipe simula periodicamente falhas, como a queda de uma Zona de Disponibilidade, para testar sua arquitetura e seus procedimentos de resposta. Que prática recomendada pela AWS é essa?",
        "alternativas": ["Realizar game days", "Escalar verticalmente", "Provisionar capacidade por estimativa", "Fazer implantações manuais"],
        "correta": "Realizar game days",
        "explicacao": "Game days simulam eventos reais em ambiente controlado para validar arquiteturas, processos e equipes, um dos princípios gerais de design do Well-Architected Framework."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Na nuvem, uma empresa cria sob demanda um ambiente idêntico ao de produção, executa testes de carga e depois o desliga, pagando apenas pelas horas usadas. Qual princípio geral de design é esse?",
        "alternativas": ["Testar sistemas em escala de produção", "Parar de adivinhar a capacidade", "Projetar arquiteturas monolíticas", "Usar servidores de longa duração"],
        "correta": "Testar sistemas em escala de produção",
        "explicacao": "Na nuvem é possível criar ambientes de teste em escala de produção apenas pelo tempo necessário, algo caro ou inviável em data centers tradicionais."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual é um benefício de definir a infraestrutura como código (IaC)?",
        "alternativas": ["Criar ambientes reproduzíveis, versionados e consistentes", "Eliminar a necessidade de controles de segurança", "Garantir que os recursos não tenham custo", "Dispensar qualquer tipo de teste"],
        "correta": "Criar ambientes reproduzíveis, versionados e consistentes",
        "explicacao": "Com IaC, a infraestrutura é descrita em arquivos que podem ser versionados, revisados e reaplicados, reduzindo erros manuais e diferenças entre ambientes."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Em vez de corrigir manualmente um servidor com problema, a equipe o encerra e lança uma nova instância a partir de uma imagem padronizada. Qual princípio de arquitetura em nuvem está sendo aplicado?",
        "alternativas": ["Tratar servidores como recursos descartáveis", "Tratar servidores como animais de estimação", "Escalar verticalmente", "Manter servidores de longa duração"],
        "correta": "Tratar servidores como recursos descartáveis",
        "explicacao": "Na nuvem, os recursos são descartáveis: é mais rápido e confiável substituir uma instância com problema por outra criada de forma automatizada do que consertá-la manualmente."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma aplicação passou a guardar os dados de sessão dos usuários no Amazon DynamoDB em vez da memória de cada instância, permitindo adicionar ou remover instâncias livremente. Qual princípio de design foi aplicado?",
        "alternativas": ["Projetar componentes sem estado (stateless)", "Acoplamento forte", "Escalabilidade vertical das instâncias existentes", "Arquitetura monolítica em uma única instância"],
        "correta": "Projetar componentes sem estado (stateless)",
        "explicacao": "Componentes sem estado não guardam dados de sessão localmente, o que permite que qualquer instância atenda qualquer requisição e facilita a escalabilidade horizontal."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson dividiu sua aplicação em serviços pequenos e independentes, cada um com sua própria função, que se comunicam por APIs. Qual estilo de arquitetura é esse?",
        "alternativas": ["Arquitetura de microsserviços", "Arquitetura monolítica", "Arquitetura cliente-servidor de camada única", "Mainframe"],
        "correta": "Arquitetura de microsserviços",
        "explicacao": "Em microsserviços, cada serviço pode ser desenvolvido, implantado e escalado de forma independente, aumentando a agilidade e isolando falhas."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual característica descreve corretamente a computação serverless na AWS?",
        "alternativas": ["Não é preciso provisionar nem gerenciar servidores, e a escalabilidade é automática", "Não existe nenhum servidor físico envolvido na execução", "O cliente é responsável por aplicar patches no sistema operacional", "A cobrança é feita por servidor provisionado por mês"],
        "correta": "Não é preciso provisionar nem gerenciar servidores, e a escalabilidade é automática",
        "explicacao": "Em serverless os servidores existem, mas são totalmente gerenciados pela AWS. O cliente foca no código e paga pelo uso real, como no AWS Lambda."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual perspectiva do AWS Cloud Adoption Framework (AWS CAF) ajuda a garantir que os investimentos em nuvem acelerem os objetivos e resultados de negócio?",
        "alternativas": ["Negócios", "Plataforma", "Segurança", "Operações"],
        "correta": "Negócios",
        "explicacao": "A perspectiva Negócios garante que a nuvem esteja alinhada à estratégia da empresa, envolvendo áreas como gestão de portfólio, inovação e monetização de dados."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual perspectiva do AWS CAF trata da construção de uma plataforma de nuvem híbrida escalável, envolvendo arquitetura, engenharia de plataforma e modernização de aplicações?",
        "alternativas": ["Plataforma", "Pessoas", "Governança", "Negócios"],
        "correta": "Plataforma",
        "explicacao": "A perspectiva Plataforma reúne capacidades técnicas como arquitetura da plataforma, engenharia de dados, provisionamento e CI/CD, e modernização de aplicações."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual perspectiva do AWS CAF foca na confidencialidade, integridade e disponibilidade dos dados e das cargas de trabalho na nuvem?",
        "alternativas": ["Segurança", "Operações", "Plataforma", "Pessoas"],
        "correta": "Segurança",
        "explicacao": "A perspectiva Segurança inclui capacidades como gerenciamento de identidade e acesso, detecção de ameaças, proteção de infraestrutura e de dados e resposta a incidentes."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual perspectiva do AWS CAF garante que os serviços de nuvem sejam entregues no nível acordado com o negócio, cobrindo monitoramento, gerenciamento de incidentes e continuidade?",
        "alternativas": ["Operações", "Negócios", "Governança", "Segurança"],
        "correta": "Operações",
        "explicacao": "A perspectiva Operações trata de observabilidade, gerenciamento de eventos, incidentes e problemas, mudanças, desempenho e capacidade dos serviços em nuvem."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual é um dos benefícios de negócio esperados com a adoção da nuvem segundo o AWS Cloud Adoption Framework?",
        "alternativas": ["Redução do risco de negócio", "Eliminação total da necessidade de treinamento", "Garantia de migração sem nenhum custo", "Substituição obrigatória de todas as aplicações por SaaS"],
        "correta": "Redução do risco de negócio",
        "explicacao": "O AWS CAF destaca quatro benefícios: redução do risco de negócio, melhoria do desempenho ESG, aumento da receita e aumento da eficiência operacional."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Quais são as fases da jornada de transformação para a nuvem descritas no AWS Cloud Adoption Framework?",
        "alternativas": ["Imaginar, alinhar, lançar e escalar", "Planejar, construir, testar e implantar", "Descobrir, projetar, operar e encerrar", "Comprar, instalar, configurar e manter"],
        "correta": "Imaginar, alinhar, lançar e escalar",
        "explicacao": "O AWS CAF organiza a transformação em quatro fases iterativas: Imaginar (Envision), Alinhar (Align), Lançar (Launch) e Escalar (Scale)."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual é a sequência de fases recomendada pela AWS para uma migração em larga escala?",
        "alternativas": ["Avaliar, mobilizar, migrar e modernizar", "Imaginar, alinhar, lançar e escalar", "Comprar, instalar, testar e desligar", "Projetar, codificar, compilar e distribuir"],
        "correta": "Avaliar, mobilizar, migrar e modernizar",
        "explicacao": "Na fase Avaliar cria-se o caso de negócio; em Mobilizar, prepara-se a organização e a base na nuvem; depois as cargas são migradas e modernizadas."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Algumas aplicações de uma empresa dependem de sistemas que ainda não podem ser migrados, por isso continuarão on-premises por enquanto. Qual estratégia de migração é essa?",
        "alternativas": ["Reter (retain)", "Aposentar (retire)", "Redefinir a hospedagem (rehost)", "Recomprar (repurchase)"],
        "correta": "Reter (retain)",
        "explicacao": "Reter significa manter a aplicação no ambiente atual, normalmente por dependências, requisitos de conformidade ou porque a migração ainda não se justifica."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson vai desativar seu sistema de CRM próprio e passar a usar uma solução de CRM oferecida como SaaS. Qual estratégia de migração é essa?",
        "alternativas": ["Recomprar (repurchase)", "Refatorar (refactor)", "Redefinir a plataforma (replatform)", "Reter (retain)"],
        "correta": "Recomprar (repurchase)",
        "explicacao": "Recomprar, também chamado de 'drop and shop', é substituir a aplicação atual por um produto diferente, normalmente uma solução SaaS."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson vai mover suas máquinas virtuais VMware para o VMware Cloud on AWS sem converter as VMs nem alterar as aplicações. Qual estratégia de migração é essa?",
        "alternativas": ["Realocar (relocate)", "Refatorar (refactor)", "Recomprar (repurchase)", "Aposentar (retire)"],
        "correta": "Realocar (relocate)",
        "explicacao": "Realocar move a infraestrutura para a nuvem no nível do hipervisor, sem comprar hardware novo, reescrever aplicações ou modificar as operações existentes."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual serviço automatiza a migração no modelo lift and shift, replicando continuamente servidores físicos e virtuais para a AWS com mínimo tempo de inatividade?",
        "alternativas": ["AWS Application Migration Service", "AWS Database Migration Service", "AWS DataSync", "AWS Transfer Family"],
        "correta": "AWS Application Migration Service",
        "explicacao": "O AWS Application Migration Service (AWS MGN) replica os servidores de origem para a AWS e permite fazer a virada (cutover) com pouca interrupção, sendo o serviço recomendado para rehost."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson está migrando dezenas de aplicações com ferramentas diferentes e quer acompanhar o progresso de todas as migrações em um único lugar. Qual serviço deve ser usado?",
        "alternativas": ["AWS Migration Hub", "AWS Organizations", "AWS Config", "Amazon CloudWatch"],
        "correta": "AWS Migration Hub",
        "explicacao": "O AWS Migration Hub oferece um local central para descobrir servidores, planejar e acompanhar o status das migrações feitas com ferramentas da AWS e de parceiros."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Antes de migrar, uma empresa precisa coletar informações sobre seus servidores on-premises, como configuração, utilização e dependências entre eles. Qual serviço ajuda nessa tarefa?",
        "alternativas": ["AWS Application Discovery Service", "AWS Application Migration Service", "AWS Snowball Edge", "AWS Systems Manager"],
        "correta": "AWS Application Discovery Service",
        "explicacao": "O AWS Application Discovery Service coleta dados de uso, configuração e dependências dos servidores on-premises para apoiar o planejamento da migração."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson vai migrar um banco de dados Oracle para o Amazon Aurora PostgreSQL e precisa converter o esquema e o código do banco. Qual ferramenta auxilia nessa conversão?",
        "alternativas": ["AWS Schema Conversion Tool (AWS SCT)", "AWS DataSync", "AWS Application Migration Service", "AWS Backup"],
        "correta": "AWS Schema Conversion Tool (AWS SCT)",
        "explicacao": "Em migrações heterogêneas (entre mecanismos diferentes), o AWS SCT converte esquemas e objetos de código. O AWS DMS faz a migração dos dados."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer copiar e sincronizar periodicamente, pela rede, grandes volumes de arquivos de seus servidores NFS e SMB para o Amazon S3 e o Amazon EFS. Qual serviço é o mais indicado?",
        "alternativas": ["AWS DataSync", "AWS Snowball Edge", "AWS Database Migration Service", "Amazon CloudFront"],
        "correta": "AWS DataSync",
        "explicacao": "O AWS DataSync automatiza e acelera a transferência online de dados entre armazenamento on-premises e serviços da AWS, como S3, EFS e FSx."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Parceiros de negócio de uma empresa enviam arquivos via SFTP, e ela quer que esses arquivos sejam gravados diretamente no Amazon S3 sem manter um servidor SFTP próprio. Qual serviço deve ser usado?",
        "alternativas": ["AWS Transfer Family", "AWS DataSync", "AWS Storage Gateway", "Amazon EFS"],
        "correta": "AWS Transfer Family",
        "explicacao": "O AWS Transfer Family oferece endpoints gerenciados de SFTP, FTPS, FTP e AS2 que gravam os arquivos diretamente no Amazon S3 ou no Amazon EFS."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Ao calcular o custo total de propriedade (TCO) de um data center on-premises para comparar com a AWS, o que deve ser considerado além do preço do hardware?",
        "alternativas": ["Energia, refrigeração, espaço físico e equipe de manutenção", "Somente o preço de compra dos servidores e dos equipamentos de rede", "Apenas o custo das licenças de software dos sistemas operacionais", "Somente o custo mensal do link de internet usado pelo data center"],
        "correta": "Energia, refrigeração, espaço físico e equipe de manutenção",
        "explicacao": "O TCO inclui custos diretos e indiretos, como instalações, energia, refrigeração, hardware de rede e armazenamento, licenças e pessoas para operar a infraestrutura."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer criar um caso de negócio para migrar para a AWS, com base em dados reais de uso dos seus servidores on-premises e em uma projeção de custos na nuvem. Qual serviço ajuda nessa análise?",
        "alternativas": ["Migration Evaluator", "AWS Budgets", "AWS Cost Explorer", "AWS Artifact"],
        "correta": "Migration Evaluator",
        "explicacao": "O Migration Evaluator analisa o ambiente atual e gera um caso de negócio com a projeção de custos na AWS, ajudando a justificar e planejar a migração."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Por que migrar um banco de dados autogerenciado em instâncias EC2 para o Amazon RDS pode reduzir o custo total de propriedade?",
        "alternativas": ["A AWS assume tarefas como backups, patches e alta disponibilidade, reduzindo o esforço operacional", "O Amazon RDS é sempre gratuito", "O Amazon RDS dispensa o pagamento de armazenamento e de transferência de dados para qualquer destino", "O Amazon RDS elimina a necessidade de qualquer configuração de segurança, de rede e de controle de acesso ao banco"],
        "correta": "A AWS assume tarefas como backups, patches e alta disponibilidade, reduzindo o esforço operacional",
        "explicacao": "Serviços gerenciados reduzem o tempo que a equipe gasta com administração, o que diminui custos de pessoal e permite focar em atividades de maior valor."
    },
]

QUESTOES += [
    {
        "dominio_id": 1,
        "template_pergunta": "Uma equipe ajustou o tipo e o tamanho das suas instâncias EC2 para que correspondam ao uso real de CPU e memória, eliminando capacidade ociosa. Como se chama essa prática?",
        "alternativas": ["Dimensionamento correto (rightsizing)", "Escalabilidade vertical obrigatória", "Provisionamento excessivo", "Locação dedicada"],
        "correta": "Dimensionamento correto (rightsizing)",
        "explicacao": "Rightsizing é escolher o tipo e o tamanho de recurso que atendem à carga com o menor custo, sendo uma das formas mais eficazes de otimizar gastos na nuvem."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer reaproveitar na AWS as licenças de software que já comprou para seu data center. Qual modelo de licenciamento é esse?",
        "alternativas": ["Traga sua própria licença (BYOL)", "Licença incluída no preço da instância", "Licença por usuário do IAM", "Licença gratuita fornecida pela AWS"],
        "correta": "Traga sua própria licença (BYOL)",
        "explicacao": "No modelo BYOL o cliente usa na nuvem licenças já adquiridas, desde que os termos do fabricante permitam. Em alguns casos é necessário usar Hosts dedicados."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson lança instâncias EC2 com Windows Server e paga a licença do sistema operacional embutida no preço por hora da instância. Qual modelo de licenciamento está sendo usado?",
        "alternativas": ["Licença incluída", "Traga sua própria licença (BYOL)", "Licença perpétua", "Licenciamento por soquete físico"],
        "correta": "Licença incluída",
        "explicacao": "No modelo de licença incluída, o custo da licença já faz parte do preço do recurso, sem necessidade de comprar ou gerenciar licenças separadamente."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual destes custos é fixo em um data center on-premises, mas se torna variável quando a empresa migra para a AWS?",
        "alternativas": ["Compra de servidores físicos", "Salário do diretor financeiro", "Treinamento dos funcionários", "Assinatura de jornais do escritório"],
        "correta": "Compra de servidores físicos",
        "explicacao": "On-premises, servidores são comprados antecipadamente (custo fixo). Na nuvem, paga-se pelo uso da capacidade computacional, transformando esse custo em variável."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson automatizou o desligamento dos ambientes de desenvolvimento à noite e nos fins de semana. Qual benefício econômico da nuvem isso aproveita?",
        "alternativas": ["Pagar apenas pelas horas em que os recursos estão em uso", "Obter um desconto fixo por compromisso de três anos", "Eliminar a cobrança pelo armazenamento", "Receber hardware dedicado gratuitamente"],
        "correta": "Pagar apenas pelas horas em que os recursos estão em uso",
        "explicacao": "Com o modelo pay-as-you-go, recursos desligados deixam de gerar custos de computação. A automação ajuda a evitar pagar por capacidade ociosa."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma startup desenvolveu todas as suas aplicações diretamente na AWS, sem nenhuma infraestrutura em data center próprio. Qual modelo de implantação ela utiliza?",
        "alternativas": ["Implantação em nuvem (totalmente na nuvem)", "Implantação híbrida (on-premises e nuvem)", "On-premises (nuvem privada)", "Colocation em data center de terceiros"],
        "correta": "Implantação em nuvem (totalmente na nuvem)",
        "explicacao": "No modelo totalmente na nuvem, todas as partes da aplicação são executadas na nuvem, seja criadas nela ou migradas de um ambiente anterior."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson usa ferramentas de virtualização e gerenciamento de recursos em seu próprio data center para oferecer recursos sob demanda às suas equipes. Qual modelo de implantação é esse?",
        "alternativas": ["On-premises (nuvem privada)", "Implantação em nuvem pública", "Implantação híbrida", "Software como Serviço"],
        "correta": "On-premises (nuvem privada)",
        "explicacao": "A implantação on-premises, também chamada de nuvem privada, usa tecnologias de virtualização em infraestrutura própria, sem os benefícios de escala da nuvem pública."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson usa um serviço de e-mail corporativo pronto, acessado pelo navegador, sem gerenciar servidores nem a aplicação. Qual modelo de serviço é esse?",
        "alternativas": ["Software como Serviço (SaaS)", "Infraestrutura como Serviço (IaaS)", "Plataforma como Serviço (PaaS)", "Nuvem privada"],
        "correta": "Software como Serviço (SaaS)",
        "explicacao": "No SaaS o provedor entrega um produto completo, que ele mesmo executa e gerencia. O cliente apenas usa o software."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Em qual modelo de serviço de nuvem o cliente tem a MENOR responsabilidade de gerenciamento?",
        "alternativas": ["Software como Serviço (SaaS)", "Infraestrutura como Serviço (IaaS)", "Plataforma como Serviço (PaaS)", "On-premises"],
        "correta": "Software como Serviço (SaaS)",
        "explicacao": "No SaaS o provedor gerencia infraestrutura, plataforma e aplicação. No PaaS o cliente gerencia a aplicação, e no IaaS também o sistema operacional e o software instalado."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual estratégia de recuperação de desastres tem o menor custo, mas o maior tempo de recuperação?",
        "alternativas": ["Backup e restauração", "Luz piloto (pilot light)", "Espera ativa (warm standby)", "Multissite ativo-ativo"],
        "correta": "Backup e restauração",
        "explicacao": "Em backup e restauração, os dados são copiados regularmente e a infraestrutura só é recriada após o desastre. É barato, mas pode levar horas para restabelecer o serviço."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual estratégia de recuperação de desastres oferece o menor tempo de recuperação, mantendo a carga de trabalho em execução completa em mais de uma Região ao mesmo tempo?",
        "alternativas": ["Multissite ativo-ativo", "Backup e restauração", "Luz piloto (pilot light)", "Espera ativa (warm standby)"],
        "correta": "Multissite ativo-ativo",
        "explicacao": "No multissite ativo-ativo, a carga de trabalho roda em vários locais simultaneamente, permitindo recuperação quase imediata, mas com o maior custo."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson mantém apenas o núcleo do seu ambiente, como o banco de dados replicado, sempre ativo em outra Região, e escala os demais componentes somente quando ocorre um desastre. Qual estratégia de recuperação é essa?",
        "alternativas": ["Luz piloto (pilot light)", "Backup e restauração", "Multissite ativo-ativo", "Espera ativa (warm standby)"],
        "correta": "Luz piloto (pilot light)",
        "explicacao": "Na luz piloto, os dados são replicados e os elementos essenciais ficam prontos, mas desligados ou mínimos; o restante é provisionado no momento do desastre."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson mantém em outra Região uma cópia reduzida, mas totalmente funcional, de seu ambiente de produção, que pode ser escalada rapidamente em caso de desastre. Qual estratégia é essa?",
        "alternativas": ["Espera ativa (warm standby)", "Luz piloto (pilot light)", "Backup e restauração", "Retenção on-premises"],
        "correta": "Espera ativa (warm standby)",
        "explicacao": "Na espera ativa, uma versão menor do ambiente está sempre em execução e atendendo requisições, reduzindo o tempo de recuperação em relação à luz piloto."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual métrica de recuperação de desastres indica a quantidade máxima aceitável de perda de dados, medida em tempo desde o último ponto de recuperação?",
        "alternativas": ["Objetivo de ponto de recuperação (RPO)", "Objetivo de tempo de recuperação (RTO)", "Acordo de nível de serviço (SLA)", "Custo total de propriedade (TCO)"],
        "correta": "Objetivo de ponto de recuperação (RPO)",
        "explicacao": "O RPO define quanto dado pode ser perdido, por exemplo 'no máximo 1 hora'. O RTO define quanto tempo o serviço pode ficar indisponível."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual métrica de recuperação de desastres indica o tempo máximo aceitável entre a interrupção do serviço e o seu restabelecimento?",
        "alternativas": ["Objetivo de tempo de recuperação (RTO)", "Objetivo de ponto de recuperação (RPO)", "Tempo médio entre falhas (MTBF)", "Custo total de propriedade (TCO)"],
        "correta": "Objetivo de tempo de recuperação (RTO)",
        "explicacao": "O RTO é o atraso máximo aceitável para restaurar o serviço. Estratégias de recuperação mais caras, como multissite, permitem RTOs menores."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson precisa proteger sua aplicação contra a indisponibilidade de uma Região inteira da AWS. Qual abordagem é a mais adequada?",
        "alternativas": ["Replicar a carga de trabalho em outra Região da AWS", "Distribuir as instâncias em várias sub-redes da mesma Zona de Disponibilidade", "Usar uma instância EC2 maior e com mais capacidade de rede", "Aumentar o tamanho dos volumes EBS e ativar snapshots manuais"],
        "correta": "Replicar a carga de trabalho em outra Região da AWS",
        "explicacao": "Usar várias Zonas de Disponibilidade protege contra falhas de data centers. Para se proteger da falha de uma Região inteira, é preciso uma estratégia multirregião."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Como a infraestrutura global da AWS ajuda empresas a atender requisitos de soberania de dados em diferentes países?",
        "alternativas": ["O cliente escolhe a Região onde os dados ficam, e eles não saem dela sem uma ação do cliente", "A AWS replica automaticamente os dados para todas as Regiões, garantindo que fiquem perto de cada país", "Os dados ficam sempre armazenados nos Estados Unidos", "Os pontos de presença guardam a cópia principal dos dados, mantendo-os sempre no país do usuário"],
        "correta": "O cliente escolhe a Região onde os dados ficam, e eles não saem dela sem uma ação do cliente",
        "explicacao": "Os dados armazenados em uma Região permanecem nela, a menos que o cliente configure explicitamente a replicação ou a transferência para outro local."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Na nuvem, se um experimento não der certo, a empresa simplesmente desliga os recursos e deixa de pagar por eles. Qual benefício isso proporciona?",
        "alternativas": ["Baixo custo de experimentação, o que aumenta a agilidade e a inovação", "Garantia de que todos os experimentos terão sucesso antes de chegar à produção", "Eliminação da necessidade de planejamento e de testes antes de cada lançamento", "Desconto automático em todos os serviços usados durante os experimentos"],
        "correta": "Baixo custo de experimentação, o que aumenta a agilidade e a inovação",
        "explicacao": "Como não há investimento em hardware, o custo de testar ideias é baixo. Isso incentiva a experimentação frequente e acelera a inovação."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A frase 'tudo falha o tempo todo' resume qual princípio de arquitetura recomendado pela AWS?",
        "alternativas": ["Projetar para falhas, assumindo que os componentes vão falhar", "Comprar hardware mais caro e confiável para evitar qualquer falha", "Manter tudo em uma única instância grande, com o hardware mais confiável", "Desativar o monitoramento para reduzir alertas falsos da equipe"],
        "correta": "Projetar para falhas, assumindo que os componentes vão falhar",
        "explicacao": "Projetar para falhas significa eliminar pontos únicos de falha com redundância, automação e recuperação automática, para que a aplicação continue funcionando."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma equipe coleta dados sobre como as escolhas de arquitetura afetam o comportamento da carga de trabalho e usa essas informações para decidir as próximas melhorias. Qual princípio geral de design é esse?",
        "alternativas": ["Orientar a arquitetura por dados", "Arquitetura definida uma única vez", "Provisionamento por estimativa", "Acoplamento forte"],
        "correta": "Orientar a arquitetura por dados",
        "explicacao": "Na nuvem é possível coletar dados sobre o efeito das decisões de arquitetura e tomar decisões baseadas em fatos, em vez de suposições."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Em um data center tradicional, as decisões de arquitetura costumam ser definidas uma única vez. Na nuvem, a arquitetura pode mudar continuamente conforme as necessidades. Qual princípio geral de design descreve isso?",
        "alternativas": ["Permitir arquiteturas evolutivas", "Testar sistemas em escala de produção", "Parar de adivinhar a capacidade", "Usar servidores como animais de estimação"],
        "correta": "Permitir arquiteturas evolutivas",
        "explicacao": "A automação e os testes sob demanda reduzem o risco de mudanças, permitindo que a arquitetura evolua com o negócio e com as novas tecnologias."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "O AWS Well-Architected Framework oferece orientações adicionais para setores e tecnologias específicas, como serverless, SaaS e serviços financeiros. Como essas extensões são chamadas?",
        "alternativas": ["Lentes (lenses) do Well-Architected", "Perspectivas do AWS Cloud Adoption Framework", "Pilares adicionais", "Planos do AWS Support com orientação especializada"],
        "correta": "Lentes (lenses) do Well-Architected",
        "explicacao": "As lentes do Well-Architected ampliam as orientações dos seis pilares para domínios específicos, como Serverless Lens, SaaS Lens e Machine Learning Lens."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson vai migrar um banco MySQL on-premises para o Amazon Aurora MySQL. Por que, nesse caso, não é necessário converter o esquema do banco?",
        "alternativas": ["Porque é uma migração homogênea, entre mecanismos compatíveis", "Porque o Aurora não usa esquemas e armazena os dados como documentos", "Porque o AWS DMS só migra bancos NoSQL e ignora a estrutura das tabelas", "Porque o esquema é recriado automaticamente pelo Aurora após a migração"],
        "correta": "Porque é uma migração homogênea, entre mecanismos compatíveis",
        "explicacao": "Em migrações homogêneas (como MySQL para Aurora MySQL) o AWS DMS migra os dados diretamente. A conversão de esquema com o AWS SCT só é necessária em migrações heterogêneas."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual é um benefício de segurança obtido ao migrar cargas de trabalho para a AWS?",
        "alternativas": ["Herdar controles de segurança e certificações de conformidade da infraestrutura da AWS", "Transferir à AWS toda a responsabilidade pela segurança dos dados e das aplicações executadas na nuvem", "Dispensar a configuração de permissões de acesso, já que a AWS define quem pode usar cada recurso", "Eliminar a necessidade de criptografia, pois toda a rede da AWS já é privada e isolada"],
        "correta": "Herdar controles de segurança e certificações de conformidade da infraestrutura da AWS",
        "explicacao": "O cliente herda os controles físicos e de infraestrutura da AWS, auditados por terceiros, mas continua responsável pela segurança do que coloca na nuvem."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual conceito descreve o compartilhamento da mesma infraestrutura física entre muitos clientes, mantendo cada um isolado dos demais?",
        "alternativas": ["Multilocação (multi-tenancy)", "Locação dedicada", "Colocation", "Hospedagem física exclusiva"],
        "correta": "Multilocação (multi-tenancy)",
        "explicacao": "Na multilocação, vários clientes compartilham recursos físicos com isolamento lógico, o que permite à AWS obter economias de escala e oferecer preços menores."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual tecnologia permite executar várias máquinas virtuais isoladas em um único servidor físico, sendo a base de serviços como o Amazon EC2?",
        "alternativas": ["Virtualização por meio de um hipervisor", "Rede de entrega de conteúdo (CDN) com cache na borda", "Balanceamento de carga", "Replicação entre Regiões com armazenamento compartilhado"],
        "correta": "Virtualização por meio de um hipervisor",
        "explicacao": "O hipervisor divide os recursos de um servidor físico entre várias máquinas virtuais. No EC2, essa função é desempenhada pelo AWS Nitro System."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual prática reduz os riscos de uma migração de muitas aplicações para a AWS?",
        "alternativas": ["Migrar em ondas, começando pelas cargas de trabalho de menor risco", "Migrar todas as aplicações em um único fim de semana", "Pular a fase de avaliação para ganhar tempo", "Migrar sem plano de reversão"],
        "correta": "Migrar em ondas, começando pelas cargas de trabalho de menor risco",
        "explicacao": "Migrar em ondas permite aprender com as primeiras migrações, ajustar processos e ganhar confiança antes de mover as aplicações mais críticas."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Uma equipe automatizou a compilação, os testes e a implantação do código para entregar mudanças pequenas com frequência e segurança. Qual prática é essa?",
        "alternativas": ["Integração e entrega contínuas (CI/CD)", "Desenvolvimento em cascata (waterfall) com testes manuais", "Implantação manual em lote, com aprovação mensal", "Congelamento de mudanças"],
        "correta": "Integração e entrega contínuas (CI/CD)",
        "explicacao": "CI/CD automatiza o caminho do código até a produção, reduzindo erros manuais e permitindo mudanças pequenas, frequentes e reversíveis."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson testou novos tipos de instância baseados em processadores AWS Graviton e obteve melhor relação preço-performance. Qual princípio do pilar Eficiência de performance ela aplicou?",
        "alternativas": ["Experimentar com mais frequência", "Parar de adivinhar a capacidade", "Aplicar segurança em todas as camadas", "Testar procedimentos de recuperação"],
        "correta": "Experimentar com mais frequência",
        "explicacao": "Na nuvem é fácil testar diferentes tipos de instâncias, armazenamento e configurações, o que permite encontrar a opção mais eficiente para cada carga."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer reduzir o tempo para lançar novos produtos no mercado. Qual característica da nuvem contribui mais diretamente para isso?",
        "alternativas": ["Agilidade para provisionar recursos em minutos", "Contratos de hardware de longo prazo", "Data centers próprios maiores", "Processos de compra mais longos"],
        "correta": "Agilidade para provisionar recursos em minutos",
        "explicacao": "A agilidade da nuvem reduz o tempo entre ter uma ideia e colocá-la em produção, pois não é preciso esperar pela compra e instalação de hardware."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Durante a Black Friday, uma loja usa o Amazon EC2 Auto Scaling para dobrar o número de instâncias e depois volta à capacidade normal. Qual vantagem financeira isso traz em relação a um data center próprio?",
        "alternativas": ["Não é preciso comprar e manter hardware ocioso dimensionado para o pico", "Os recursos usados no pico não são cobrados, pois o Auto Scaling é gratuito", "O tráfego de entrada passa a ser cobrado em dobro durante o período de pico", "Não há nenhuma diferença de custo, pois a capacidade de pico é paga o ano todo"],
        "correta": "Não é preciso comprar e manter hardware ocioso dimensionado para o pico",
        "explicacao": "On-premises, seria preciso comprar capacidade para o pico, que ficaria ociosa o resto do ano. Na nuvem, paga-se pela capacidade extra apenas enquanto ela é usada."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual afirmação sobre a infraestrutura global da AWS é verdadeira?",
        "alternativas": ["Cada Região é isolada e independente das demais Regiões", "Todas as Regiões compartilham as mesmas Zonas de Disponibilidade", "Uma Zona de Disponibilidade pode pertencer a várias Regiões", "Os pontos de presença substituem as Regiões"],
        "correta": "Cada Região é isolada e independente das demais Regiões",
        "explicacao": "As Regiões são isoladas para oferecer tolerância a falhas e estabilidade. Cada Região contém várias Zonas de Disponibilidade que pertencem somente a ela."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer padronizar o uso de várias contas, aplicar controles de segurança e criar uma base inicial (landing zone) bem arquitetada antes de migrar suas cargas de trabalho. Qual serviço ajuda nessa preparação?",
        "alternativas": ["AWS Control Tower", "AWS Migration Hub", "AWS DataSync", "Amazon Lightsail"],
        "correta": "AWS Control Tower",
        "explicacao": "O AWS Control Tower configura e governa um ambiente multicontas seguro (landing zone), com controles preventivos e de detecção, sendo útil na fase de mobilização da migração."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual é uma vantagem de usar serviços gerenciados da AWS em vez de instalar e operar o mesmo software em instâncias EC2?",
        "alternativas": ["Menor sobrecarga operacional, pois a AWS cuida de tarefas como escalabilidade e manutenção", "Controle total sobre o hardware físico e o hipervisor usados por trás do serviço gerenciado", "Ausência total de custos", "Possibilidade de acessar fisicamente os data centers e escolher o hardware usado em cada servidor"],
        "correta": "Menor sobrecarga operacional, pois a AWS cuida de tarefas como escalabilidade e manutenção",
        "explicacao": "Serviços gerenciados transferem à AWS grande parte das tarefas operacionais, permitindo que a equipe foque no desenvolvimento das aplicações."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson pretende migrar e quer receber treinamento, orientação de arquitetura e financiamento da AWS para acelerar a jornada. Qual programa foi criado para apoiar migrações em larga escala?",
        "alternativas": ["AWS Migration Acceleration Program (MAP)", "Nível gratuito da AWS (AWS Free Tier)", "AWS Artifact", "AWS Budgets com alertas de orçamento"],
        "correta": "AWS Migration Acceleration Program (MAP)",
        "explicacao": "O AWS MAP é um programa que combina metodologia, ferramentas, especialistas, treinamento e incentivos financeiros para reduzir o custo e a complexidade de migrações."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Por que o uso de várias Zonas de Disponibilidade é considerado uma prática de alta disponibilidade de baixo custo e baixa complexidade?",
        "alternativas": ["As Zonas de Disponibilidade são próximas o bastante para replicação síncrona com baixa latência, mas isoladas fisicamente", "As Zonas de Disponibilidade ficam em continentes diferentes", "As Zonas de Disponibilidade compartilham a mesma fonte de energia, o que simplifica e barateia a replicação síncrona dos dados entre elas", "As Zonas de Disponibilidade são gratuitas para transferência de dados em qualquer cenário e não exigem nenhuma configuração de rede adicional"],
        "correta": "As Zonas de Disponibilidade são próximas o bastante para replicação síncrona com baixa latência, mas isoladas fisicamente",
        "explicacao": "As Zonas de Disponibilidade de uma Região ficam a uma distância significativa umas das outras, com energia e rede independentes, mas conectadas por links de baixa latência."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual afirmação descreve uma Região da AWS?",
        "alternativas": ["Uma localização física no mundo composta por várias Zonas de Disponibilidade isoladas", "Um único data center localizado em uma cidade, com energia e rede redundantes dentro do prédio", "Um ponto de presença usado apenas para cache", "Um rack de servidores da AWS instalado no escritório do cliente para atender requisitos de baixa latência"],
        "correta": "Uma localização física no mundo composta por várias Zonas de Disponibilidade isoladas",
        "explicacao": "Cada Região é uma área geográfica separada com várias Zonas de Disponibilidade, normalmente pelo menos três, isoladas e fisicamente separadas."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer reduzir o custo de ambientes de teste que ficam ligados mesmo quando ninguém os usa, sem perder a capacidade de recriá-los rapidamente. Qual prática da nuvem atende a esse objetivo?",
        "alternativas": ["Criar os ambientes com infraestrutura como código e excluí-los quando não forem necessários", "Comprar instâncias reservadas de três anos para os testes e mantê-las ligadas o tempo todo para evitar esperas", "Manter os ambientes sempre ligados para evitar o trabalho de reconfigurá-los manualmente a cada uso", "Mover os testes para hardware on-premises já comprado, que não gera custo adicional na nuvem"],
        "correta": "Criar os ambientes com infraestrutura como código e excluí-los quando não forem necessários",
        "explicacao": "Com IaC, é possível recriar ambientes inteiros em minutos, então não há motivo para mantê-los ligados e pagando quando ninguém os está usando."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer se beneficiar do modelo de nuvem para lidar com uma demanda que cresce de forma imprevisível. Qual abordagem é a mais adequada?",
        "alternativas": ["Usar escalabilidade automática para ajustar a capacidade conforme a demanda real", "Comprar hoje toda a capacidade estimada para os próximos cinco anos", "Limitar o número de usuários da aplicação", "Escolher sempre o maior tipo de instância disponível"],
        "correta": "Usar escalabilidade automática para ajustar a capacidade conforme a demanda real",
        "explicacao": "A escalabilidade automática evita tanto o excesso quanto a falta de capacidade, acompanhando a demanda e cobrando apenas pelo que é usado."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "Qual é a principal diferença entre alta disponibilidade e tolerância a falhas?",
        "alternativas": ["Tolerância a falhas busca zero interrupção, enquanto alta disponibilidade aceita um tempo mínimo de inatividade", "Alta disponibilidade só existe on-premises, enquanto a tolerância a falhas só existe em ambientes de nuvem pública", "Tolerância a falhas não usa redundância, enquanto a alta disponibilidade exige componentes duplicados em várias Regiões", "Não há diferença entre os dois conceitos"],
        "correta": "Tolerância a falhas busca zero interrupção, enquanto alta disponibilidade aceita um tempo mínimo de inatividade",
        "explicacao": "Um sistema altamente disponível minimiza o tempo de inatividade. Um sistema tolerante a falhas continua operando sem interrupção perceptível, normalmente com mais redundância e custo."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson com pouca experiência em nuvem quer orientações prescritivas, padrões e guias passo a passo da AWS para migrar e modernizar aplicações. Qual recurso oferece esse conteúdo?",
        "alternativas": ["AWS Prescriptive Guidance", "AWS Artifact", "AWS Budgets", "AWS Health Dashboard"],
        "correta": "AWS Prescriptive Guidance",
        "explicacao": "O AWS Prescriptive Guidance reúne estratégias, guias e padrões testados por especialistas da AWS e parceiros para acelerar migrações e modernizações."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer saber se pode migrar cargas de trabalho Windows e SQL Server para a AWS mantendo o uso de suas licenças Microsoft. Qual fator do custo total de propriedade ela está avaliando?",
        "alternativas": ["Estratégia de licenciamento de software", "Escolha da Zona de Disponibilidade", "Política de senhas do IAM", "Configuração de DNS"],
        "correta": "Estratégia de licenciamento de software",
        "explicacao": "O licenciamento impacta bastante o TCO. É preciso avaliar se é possível usar BYOL, se é melhor usar licença incluída ou se compensa migrar para alternativas de código aberto."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson reduziu a equipe dedicada a trocar discos, atualizar firmware e substituir servidores após migrar para a AWS. Que tipo de redução de custo é essa?",
        "alternativas": ["Redução de custos operacionais com infraestrutura física", "Redução de custos com licenças de aplicativos SaaS", "Redução de impostos sobre transferência de dados", "Redução do custo de treinamento em nuvem"],
        "correta": "Redução de custos operacionais com infraestrutura física",
        "explicacao": "Como a AWS é responsável pelo hardware, tarefas como manutenção física e substituição de equipamentos deixam de ser responsabilidade do cliente."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer modernizar uma aplicação legada para obter benefícios como escalabilidade automática e menor manutenção. Qual abordagem de modernização normalmente traz esses benefícios?",
        "alternativas": ["Adotar serviços gerenciados, contêineres ou arquiteturas serverless", "Mover a aplicação para um servidor físico maior e mais moderno no data center atual", "Congelar a aplicação e não fazer mais mudanças", "Adicionar mais discos locais e memória ao servidor físico atual da aplicação"],
        "correta": "Adotar serviços gerenciados, contêineres ou arquiteturas serverless",
        "explicacao": "Modernizar com serviços gerenciados, contêineres ou serverless reduz a manutenção da infraestrutura e permite escalar automaticamente conforme a demanda."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "O que significa dizer que a AWS oferece recursos 'sob demanda'?",
        "alternativas": ["Os recursos podem ser provisionados quando necessários e liberados quando não forem mais usados", "Os recursos só podem ser solicitados por meio de contrato anual assinado com a equipe comercial da AWS", "Os recursos são entregues fisicamente no endereço do cliente, que instala os servidores no próprio escritório", "Os recursos ficam disponíveis apenas em horário comercial e precisam ser agendados com antecedência"],
        "correta": "Os recursos podem ser provisionados quando necessários e liberados quando não forem mais usados",
        "explicacao": "O autoatendimento sob demanda permite criar e encerrar recursos em minutos, pelo console, CLI ou APIs, sem interação humana com o provedor."
    },
]

QUESTOES += [
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson está comparando o modelo de nuvem com seu data center. Qual afirmação sobre o planejamento de capacidade na nuvem está correta?",
        "alternativas": ["A capacidade pode ser ajustada a qualquer momento, reduzindo o risco de errar a previsão de demanda", "É preciso prever a demanda com cinco anos de antecedência e comprar a capacidade, como em um data center tradicional", "A capacidade só pode ser alterada uma vez por ano", "A capacidade é fixa e definida na criação da conta, sem possibilidade de alteração posterior pelo cliente"],
        "correta": "A capacidade pode ser ajustada a qualquer momento, reduzindo o risco de errar a previsão de demanda",
        "explicacao": "Na nuvem, erros de previsão têm baixo impacto, porque é possível aumentar ou reduzir a capacidade rapidamente conforme a demanda real."
    },
    {
        "dominio_id": 1,
        "template_pergunta": "A lojinha do Alyson quer expandir para um novo país e precisa de infraestrutura local em poucos dias, sem negociar a construção de um data center. Qual benefício da AWS torna isso possível?",
        "alternativas": ["Infraestrutura global disponível sob demanda em várias Regiões", "Contratos de colocation de longo prazo em data centers locais do novo país", "Compra de servidores com entrega expressa e instalação no país de destino", "Licenças de software gratuitas para cada novo país em que a empresa passar a operar"],
        "correta": "Infraestrutura global disponível sob demanda em várias Regiões",
        "explicacao": "Como a AWS já mantém Regiões em diversos países, uma empresa pode implantar sua aplicação em outra parte do mundo em minutos, sem investir em instalações físicas."
    },
]

# =========================================================================
# AMPLIAÇÃO: DOMÍNIO 2 - SEGURANÇA E CONFORMIDADE
# =========================================================================
QUESTOES += [
    {
        "dominio_id": 2,
        "template_pergunta": "Ao usar o AWS Lambda, qual item é responsabilidade do cliente segundo o Modelo de Responsabilidade Compartilhada?",
        "alternativas": ["O código da função e as permissões do IAM concedidas a ela", "A aplicação de patches no sistema operacional que executa as funções", "A segurança física dos servidores e dos data centers que executam as funções", "A manutenção da infraestrutura de rede da AWS usada pelo Lambda"],
        "correta": "O código da função e as permissões do IAM concedidas a ela",
        "explicacao": "Em serviços serverless como o Lambda, a AWS gerencia a infraestrutura e o sistema operacional. O cliente continua responsável pelo código, pelos dados e pelas permissões."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Ao usar o Amazon S3, qual tarefa é responsabilidade do cliente?",
        "alternativas": ["Configurar as políticas de bucket e decidir quem pode acessar os objetos", "Garantir a durabilidade dos discos físicos que armazenam os objetos", "Substituir o hardware com defeito nos data centers", "Manter o software de armazenamento distribuído do S3"],
        "correta": "Configurar as políticas de bucket e decidir quem pode acessar os objetos",
        "explicacao": "A AWS opera a infraestrutura do S3. O cliente define o acesso aos dados, as configurações de criptografia, o versionamento e o bloqueio de acesso público."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Ao usar o Amazon EC2, qual destas tarefas é responsabilidade do cliente?",
        "alternativas": ["Configurar os security groups e atualizar o sistema operacional convidado", "Manter e atualizar o hipervisor que executa as instâncias nos servidores físicos", "Proteger fisicamente os data centers", "Substituir os servidores físicos com defeito e os discos que armazenam os volumes EBS"],
        "correta": "Configurar os security groups e atualizar o sistema operacional convidado",
        "explicacao": "No EC2 (IaaS), o cliente gerencia o sistema operacional, as aplicações, os dados e as regras de firewall. A AWS gerencia o hardware e a virtualização."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Ao usar o Amazon DynamoDB, qual destas tarefas é responsabilidade da AWS?",
        "alternativas": ["Aplicar patches e manter a infraestrutura e o software do banco de dados", "Definir quais usuários e funções do IAM podem ler e gravar itens nas tabelas", "Decidir quais dados serão armazenados nas tabelas", "Classificar a sensibilidade dos dados armazenados e definir quem pode acessá-los"],
        "correta": "Aplicar patches e manter a infraestrutura e o software do banco de dados",
        "explicacao": "O DynamoDB é totalmente gerenciado: a AWS cuida da infraestrutura, do software e da escalabilidade. O cliente gerencia os dados e o controle de acesso a eles."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "No Modelo de Responsabilidade Compartilhada, qual destes é um exemplo de controle compartilhado, aplicado tanto pela AWS quanto pelo cliente em suas respectivas camadas?",
        "alternativas": ["Gerenciamento de patches", "Proteção física dos data centers", "Controles ambientais, como refrigeração e energia", "Proteção de dados dentro das aplicações do cliente"],
        "correta": "Gerenciamento de patches",
        "explicacao": "Controles compartilhados incluem gerenciamento de patches, gerenciamento de configuração e conscientização e treinamento: a AWS os aplica à infraestrutura e o cliente aos seus sistemas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "No Modelo de Responsabilidade Compartilhada, os controles físicos e ambientais dos data centers são exemplos de qual tipo de controle para o cliente?",
        "alternativas": ["Controles herdados", "Controles compartilhados", "Controles específicos do cliente", "Controles opcionais"],
        "correta": "Controles herdados",
        "explicacao": "Controles herdados são aqueles que o cliente herda totalmente da AWS, como os controles físicos e ambientais, sem precisar implementá-los."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Como a divisão de responsabilidades de segurança muda conforme o tipo de serviço usado?",
        "alternativas": ["Quanto mais gerenciado o serviço, menos tarefas de segurança ficam com o cliente", "A divisão é sempre a mesma, independentemente do serviço ou do modelo de implantação", "Em serviços gerenciados, o cliente assume a segurança física dos servidores usados pelo serviço", "Em IaaS, a AWS gerencia o sistema operacional do cliente e as aplicações instaladas nele"],
        "correta": "Quanto mais gerenciado o serviço, menos tarefas de segurança ficam com o cliente",
        "explicacao": "No EC2 o cliente gerencia o sistema operacional; no RDS a AWS assume essa parte; no Lambda e no DynamoDB a AWS gerencia ainda mais. Os dados e o acesso continuam sendo do cliente."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "De quem é a responsabilidade de treinar os funcionários de uma empresa sobre boas práticas de segurança no uso da AWS?",
        "alternativas": ["Do cliente, para os seus funcionários", "Exclusivamente da AWS", "Do AWS Support, automaticamente", "De nenhuma das partes"],
        "correta": "Do cliente, para os seus funcionários",
        "explicacao": "Conscientização e treinamento é um controle compartilhado: a AWS treina seus funcionários e o cliente deve treinar os seus."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson armazena dados de clientes em instâncias EC2. Segundo o Modelo de Responsabilidade Compartilhada, quem é responsável por classificar e proteger esses dados?",
        "alternativas": ["O cliente", "A AWS", "O fornecedor do sistema operacional", "O AWS Support"],
        "correta": "O cliente",
        "explicacao": "Os dados são sempre responsabilidade do cliente, que decide como classificá-los, criptografá-los e quem pode acessá-los."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual tarefa só pode ser realizada pelo usuário raiz (root) da conta da AWS?",
        "alternativas": ["Fechar a conta da AWS", "Criar uma instância EC2", "Criar um bucket do S3", "Criar um usuário do IAM"],
        "correta": "Fechar a conta da AWS",
        "explicacao": "Algumas tarefas exigem o usuário raiz, como fechar a conta, alterar as configurações da conta e restaurar permissões de um administrador do IAM. As demais podem ser feitas com identidades do IAM."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson acabou de criar sua conta da AWS. Qual é a ação recomendada antes de começar a usar os serviços?",
        "alternativas": ["Proteger o usuário raiz com MFA e criar identidades administrativas separadas para o dia a dia", "Criar chaves de acesso para o usuário raiz", "Compartilhar a senha do usuário raiz com toda a equipe para facilitar a administração diária da conta", "Desativar o AWS CloudTrail e o AWS Config para economizar até que existam cargas de trabalho em produção"],
        "correta": "Proteger o usuário raiz com MFA e criar identidades administrativas separadas para o dia a dia",
        "explicacao": "A AWS recomenda proteger o usuário raiz com MFA e uma senha forte e usar identidades do IAM ou do IAM Identity Center para as tarefas diárias."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "O que é a autenticação multifator (MFA) na AWS?",
        "alternativas": ["Uma camada extra de segurança que exige, além da senha, um código ou dispositivo de autenticação", "Um tipo de criptografia aplicada aos buckets do S3 com várias chaves de criptografia diferentes ao mesmo tempo", "Um recurso que permite usar a mesma senha em várias contas da AWS sem precisar decorar outras senhas", "Um serviço de backup das credenciais dos usuários do IAM, usado para recuperar senhas esquecidas no console"],
        "correta": "Uma camada extra de segurança que exige, além da senha, um código ou dispositivo de autenticação",
        "explicacao": "A MFA exige um segundo fator, como um aplicativo autenticador, uma chave de segurança FIDO ou um token de hardware, dificultando o acesso com uma senha roubada."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual destes dispositivos pode ser usado como fator de MFA para usuários da AWS?",
        "alternativas": ["Chave de segurança FIDO, como uma chave física USB", "Certificado SSL/TLS de um site", "Par de chaves SSH gerado para acessar uma instância EC2 Linux", "Endereço IP fixo do escritório cadastrado como segundo fator"],
        "correta": "Chave de segurança FIDO, como uma chave física USB",
        "explicacao": "A AWS aceita como MFA chaves de acesso e chaves de segurança FIDO (passkeys), aplicativos autenticadores virtuais e tokens TOTP de hardware."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Um desenvolvedor precisa usar a AWS CLI em seu computador com um usuário do IAM. Que tipo de credencial ele deve usar?",
        "alternativas": ["Chave de acesso (ID da chave de acesso e chave de acesso secreta)", "Par de chaves SSH", "Senha do console do usuário raiz, digitada a cada comando executado na CLI", "Certificado SSL/TLS emitido pelo AWS Certificate Manager para o usuário"],
        "correta": "Chave de acesso (ID da chave de acesso e chave de acesso secreta)",
        "explicacao": "Chaves de acesso são usadas para acesso programático pela CLI, SDKs e APIs. A AWS recomenda preferir credenciais temporárias, como as do IAM Identity Center, sempre que possível."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer exigir que todos os usuários do IAM usem senhas com no mínimo 14 caracteres, incluindo números e símbolos. O que deve ser configurado?",
        "alternativas": ["Uma política de senhas do IAM para a conta", "Uma política de bucket do S3", "Uma regra de security group", "Uma SCP do AWS Organizations que defina senhas"],
        "correta": "Uma política de senhas do IAM para a conta",
        "explicacao": "A política de senhas da conta define requisitos de complexidade, expiração e reutilização das senhas dos usuários do IAM."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer gerar um relatório com todos os usuários do IAM da conta e o status de suas credenciais, como senhas, chaves de acesso e MFA. Qual recurso deve ser usado?",
        "alternativas": ["Relatório de credenciais do IAM", "AWS Cost and Usage Report", "AWS Artifact", "Amazon Inspector"],
        "correta": "Relatório de credenciais do IAM",
        "explicacao": "O relatório de credenciais lista os usuários da conta e o status de suas senhas, chaves de acesso e dispositivos de MFA, ajudando em auditorias."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Um administrador quer descobrir quais serviços um usuário do IAM realmente acessou recentemente, para remover permissões que não são usadas. Qual informação do IAM ajuda nessa tarefa?",
        "alternativas": ["Informações de último acesso (último acesso a serviços)", "Relatório de custos e uso do AWS Cost Explorer por usuário", "Logs de fluxo da VPC", "Métricas de uso do Amazon CloudWatch para cada usuário do IAM"],
        "correta": "Informações de último acesso (último acesso a serviços)",
        "explicacao": "As informações de último acesso do IAM mostram quando uma identidade usou cada serviço pela última vez, ajudando a aplicar o privilégio mínimo."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma política do IAM permite a ação s3:GetObject, mas outra política anexada ao mesmo usuário nega explicitamente essa ação. Qual será o resultado?",
        "alternativas": ["O acesso é negado, porque uma negação explícita sempre prevalece", "O acesso é permitido, porque a permissão foi concedida", "O acesso é permitido apenas em horário comercial", "Prevalece a política criada por último"],
        "correta": "O acesso é negado, porque uma negação explícita sempre prevalece",
        "explicacao": "Na avaliação de políticas da AWS, uma negação explícita (Deny) sempre se sobrepõe a qualquer permissão (Allow)."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Um novo usuário do IAM foi criado e nenhuma política foi anexada a ele. Quais ações ele pode executar na AWS?",
        "alternativas": ["Nenhuma, porque por padrão todas as ações são negadas implicitamente", "Todas, porque usuários novos recebem permissões de administrador por padrão", "Apenas ações de leitura em todos os serviços, até que uma política seja anexada", "As mesmas ações do usuário raiz, exceto fechar a conta e alterar o plano de suporte"],
        "correta": "Nenhuma, porque por padrão todas as ações são negadas implicitamente",
        "explicacao": "No IAM, tudo é negado por padrão. Uma identidade só pode executar ações que forem explicitamente permitidas por uma política."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual afirmação sobre o AWS IAM está correta?",
        "alternativas": ["É um serviço global e não tem custo adicional", "É cobrado por usuário criado e por política anexada", "Precisa ser configurado separadamente em cada Região", "Só pode ser usado pelo usuário raiz da conta de gerenciamento"],
        "correta": "É um serviço global e não tem custo adicional",
        "explicacao": "O IAM é um recurso da conta oferecido sem custo adicional, e suas identidades e políticas são globais, valendo para todas as Regiões."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual é a diferença entre uma política baseada em identidade e uma política baseada em recurso?",
        "alternativas": ["A baseada em identidade é anexada a usuários, grupos ou funções; a baseada em recurso é anexada ao recurso, como um bucket do S3", "As duas são anexadas apenas ao usuário raiz e valem somente para recursos criados por ele na conta de gerenciamento da organização", "A baseada em recurso só pode negar acessos, enquanto a baseada em identidade só pode permitir acessos a serviços globais, como o IAM e o Route 53", "A baseada em identidade só funciona no console"],
        "correta": "A baseada em identidade é anexada a usuários, grupos ou funções; a baseada em recurso é anexada ao recurso, como um bucket do S3",
        "explicacao": "Políticas baseadas em identidade definem o que a identidade pode fazer. Políticas baseadas em recurso, como políticas de bucket, definem quem pode acessar aquele recurso."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer usar políticas de permissão prontas, criadas e mantidas pela AWS para funções de trabalho comuns, como acesso somente leitura. Que tipo de política deve ser usado?",
        "alternativas": ["Políticas gerenciadas pela AWS", "Políticas em linha (inline)", "Políticas de bucket", "Listas de controle de acesso de rede"],
        "correta": "Políticas gerenciadas pela AWS",
        "explicacao": "Políticas gerenciadas pela AWS são criadas e atualizadas pela AWS. O cliente também pode criar políticas gerenciadas próprias para necessidades específicas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Um auditor externo precisa de acesso temporário, somente leitura, a uma conta da AWS da empresa a partir da conta da AWS dele. Qual é a forma recomendada de conceder esse acesso?",
        "alternativas": ["Criar uma função do IAM que a conta do auditor possa assumir", "Compartilhar a senha do usuário raiz", "Criar chaves de acesso permanentes e enviá-las por e-mail", "Tornar todos os buckets públicos"],
        "correta": "Criar uma função do IAM que a conta do auditor possa assumir",
        "explicacao": "Funções do IAM permitem acesso entre contas com credenciais temporárias, sem compartilhar senhas ou chaves de longo prazo."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual serviço emite as credenciais temporárias usadas quando uma identidade assume uma função do IAM?",
        "alternativas": ["AWS Security Token Service (AWS STS)", "AWS Key Management Service (AWS KMS)", "AWS Certificate Manager", "Amazon Cognito Sync"],
        "correta": "AWS Security Token Service (AWS STS)",
        "explicacao": "O AWS STS gera credenciais temporárias com validade limitada, usadas por funções do IAM, acesso entre contas e federação de identidades."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer que seus funcionários acessem a AWS com as mesmas credenciais do diretório corporativo, sem criar usuários do IAM para cada um. Qual conceito descreve essa abordagem?",
        "alternativas": ["Federação de identidades", "Criptografia de envelope", "Multilocação", "Replicação entre Regiões"],
        "correta": "Federação de identidades",
        "explicacao": "Com a federação, um provedor de identidade externo (como Active Directory, Okta ou Microsoft Entra ID) autentica os usuários, que recebem acesso temporário à AWS."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "No AWS IAM Identity Center, qual recurso define o conjunto de permissões que um usuário ou grupo recebe ao acessar uma conta da AWS?",
        "alternativas": ["Conjunto de permissões (permission set)", "Security group", "Lista de controle de acesso de rede (Network ACL)", "Política de bucket"],
        "correta": "Conjunto de permissões (permission set)",
        "explicacao": "Um conjunto de permissões é um modelo de políticas que o IAM Identity Center aplica nas contas atribuídas, criando as funções correspondentes automaticamente."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "No AWS Organizations, como se chama o agrupamento de contas que permite aplicar políticas, como SCPs, a várias contas ao mesmo tempo?",
        "alternativas": ["Unidade organizacional (OU)", "Grupo do IAM", "Security group", "Zona de Disponibilidade"],
        "correta": "Unidade organizacional (OU)",
        "explicacao": "As OUs organizam as contas em uma hierarquia. Políticas aplicadas a uma OU valem para todas as contas que ela contém."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Por que a AWS recomenda usar várias contas, organizadas com o AWS Organizations, em vez de colocar todas as cargas de trabalho em uma única conta?",
        "alternativas": ["Para isolar ambientes e limitar o impacto de incidentes de segurança", "Porque cada conta tem desconto automático de 50%", "Porque uma conta só pode ter uma instância EC2", "Porque o IAM não funciona em contas com muitos recursos"],
        "correta": "Para isolar ambientes e limitar o impacto de incidentes de segurança",
        "explicacao": "A conta da AWS é um limite de isolamento. Separar produção, desenvolvimento e segurança em contas diferentes reduz o raio de impacto de problemas e facilita a governança."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer configurar rapidamente um ambiente multicontas seguro, com controles (guardrails) preventivos e de detecção já aplicados. Qual serviço deve ser usado?",
        "alternativas": ["AWS Control Tower", "AWS Artifact", "Amazon Inspector", "AWS Shield"],
        "correta": "AWS Control Tower",
        "explicacao": "O AWS Control Tower cria uma landing zone com boas práticas e aplica controles que usam recursos como SCPs e regras do AWS Config para governar as contas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer compartilhar sub-redes e outros recursos de uma conta com outras contas da mesma organização, sem duplicá-los. Qual serviço permite isso?",
        "alternativas": ["AWS Resource Access Manager (AWS RAM)", "AWS Directory Service (Microsoft AD gerenciado)", "AWS Secrets Manager", "Amazon Macie"],
        "correta": "AWS Resource Access Manager (AWS RAM)",
        "explicacao": "O AWS RAM permite compartilhar recursos, como sub-redes da VPC e Transit Gateways, com outras contas ou com toda a organização."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson precisa de um Microsoft Active Directory gerenciado na AWS para suas aplicações Windows, sem manter controladores de domínio em instâncias EC2. Qual serviço deve ser usado?",
        "alternativas": ["AWS Directory Service for Microsoft Active Directory", "Amazon Cognito", "AWS IAM Identity Center com o diretório nativo do Identity Center", "AWS Secrets Manager"],
        "correta": "AWS Directory Service for Microsoft Active Directory",
        "explicacao": "O AWS Managed Microsoft AD é um Active Directory real, gerenciado pela AWS, que pode se integrar a cargas Windows e a diretórios on-premises."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson, que atua na área de saúde, precisa assinar o Business Associate Addendum (BAA) com a AWS para atender à HIPAA. Onde ela pode revisar e aceitar esse acordo?",
        "alternativas": ["AWS Artifact", "AWS Organizations", "AWS Config", "AWS Trusted Advisor"],
        "correta": "AWS Artifact",
        "explicacao": "Além de relatórios de conformidade, o AWS Artifact permite revisar, aceitar e gerenciar acordos com a AWS, como o BAA, para uma conta ou para toda a organização."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer automatizar a coleta de evidências do uso da AWS para preparar auditorias com base em frameworks como PCI DSS e GDPR. Qual serviço deve ser usado?",
        "alternativas": ["AWS Audit Manager", "AWS Artifact", "AWS Cost Explorer", "Amazon Detective"],
        "correta": "AWS Audit Manager",
        "explicacao": "O AWS Audit Manager coleta evidências continuamente e as organiza de acordo com frameworks de conformidade, simplificando a preparação para auditorias."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual é a diferença entre o AWS Artifact e o AWS Audit Manager?",
        "alternativas": ["O Artifact fornece relatórios de conformidade da própria AWS; o Audit Manager coleta evidências sobre o uso que o cliente faz da AWS", "Os dois fornecem apenas faturas", "O Artifact detecta ameaças em tempo real nas contas; o Audit Manager bloqueia ataques DDoS e aplica regras de firewall automaticamente", "O Audit Manager substitui o CloudTrail no registro das chamadas de API, e o Artifact substitui o AWS Config na avaliação de recursos"],
        "correta": "O Artifact fornece relatórios de conformidade da própria AWS; o Audit Manager coleta evidências sobre o uso que o cliente faz da AWS",
        "explicacao": "O Artifact mostra a conformidade da infraestrutura da AWS. O Audit Manager ajuda o cliente a demonstrar a conformidade das suas próprias cargas de trabalho."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson precisa obter informações sobre os programas de conformidade da AWS, como ISO 27001, SOC e PCI DSS, e entender como a AWS os atende. Qual recurso oferece essa visão geral?",
        "alternativas": ["Página de programas de conformidade da AWS (AWS Compliance Programs)", "Página de status dos serviços da AWS no AWS Health Dashboard", "Amazon CloudWatch", "Página de preços dos serviços da AWS (AWS Pricing)"],
        "correta": "Página de programas de conformidade da AWS (AWS Compliance Programs)",
        "explicacao": "A AWS publica a lista de programas de conformidade atendidos e os serviços incluídos em cada um. Os relatórios de auditoria detalhados ficam no AWS Artifact."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer verificar se um serviço da AWS faz parte do escopo de uma certificação específica, como PCI DSS, antes de usá-lo para dados de cartão. Onde ela deve consultar?",
        "alternativas": ["Na página 'Serviços da AWS no escopo por programa de conformidade'", "No relatório de custos por serviço do AWS Cost Explorer", "Na página de produtos de segurança do AWS Marketplace", "No Amazon CloudWatch"],
        "correta": "Na página 'Serviços da AWS no escopo por programa de conformidade'",
        "explicacao": "A AWS mantém uma lista atualizada dos serviços incluídos no escopo de cada programa de conformidade, como PCI DSS, HIPAA, SOC e ISO."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer avaliar várias regras do AWS Config de uma só vez, como um pacote alinhado a um padrão de segurança, e implantá-lo em várias contas. Qual recurso deve ser usado?",
        "alternativas": ["Pacotes de conformidade (conformance packs) do AWS Config", "Relatórios de conformidade baixados mensalmente do AWS Artifact", "Políticas de senha do IAM", "Alarmes compostos do Amazon CloudWatch combinando várias métricas"],
        "correta": "Pacotes de conformidade (conformance packs) do AWS Config",
        "explicacao": "Os conformance packs agrupam regras do AWS Config e ações de correção, podendo ser implantados em toda a organização para avaliar a conformidade de forma padronizada."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual é a diferença entre criptografia em repouso e criptografia em trânsito?",
        "alternativas": ["Em repouso protege dados armazenados; em trânsito protege dados enquanto trafegam pela rede", "Em repouso protege dados enquanto trafegam pela rede; em trânsito protege dados gravados em disco", "As duas só se aplicam a bancos de dados relacionais, como o Amazon RDS, o Amazon Aurora e o Redshift", "Não há diferença entre elas, pois os dois termos descrevem a criptografia aplicada aos backups"],
        "correta": "Em repouso protege dados armazenados; em trânsito protege dados enquanto trafegam pela rede",
        "explicacao": "Criptografia em repouso protege dados em discos, buckets e bancos. Criptografia em trânsito, normalmente com TLS, protege dados que se movem entre sistemas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual protocolo é normalmente usado para criptografar dados em trânsito entre o navegador do usuário e uma aplicação web hospedada na AWS?",
        "alternativas": ["TLS (HTTPS)", "FTP", "Telnet", "HTTP sem criptografia"],
        "correta": "TLS (HTTPS)",
        "explicacao": "O TLS, usado pelo HTTPS, criptografa a comunicação na rede. Certificados para TLS podem ser emitidos e renovados com o AWS Certificate Manager."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer criptografar automaticamente os volumes Amazon EBS das suas instâncias EC2. Qual afirmação está correta?",
        "alternativas": ["A criptografia do EBS usa chaves do AWS KMS e pode ser ativada por padrão para novos volumes", "Volumes EBS não podem ser criptografados, apenas os snapshots que são armazenados no Amazon S3", "A criptografia do EBS exige instalar software de terceiros em cada instância que usa o volume", "Somente volumes de instâncias Windows podem ser criptografados, usando o BitLocker configurado pela AWS"],
        "correta": "A criptografia do EBS usa chaves do AWS KMS e pode ser ativada por padrão para novos volumes",
        "explicacao": "A criptografia do EBS protege dados em repouso, snapshots e dados em trânsito entre a instância e o volume, usando chaves do AWS KMS, e pode ser ativada por padrão na Região."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer controlar quem pode usar suas chaves de criptografia, rotacioná-las automaticamente e auditar cada uso no AWS CloudTrail. Que tipo de chave do AWS KMS deve usar?",
        "alternativas": ["Chave gerenciada pelo cliente", "Chave gerenciada pela AWS sem nenhuma configuração", "Senha do usuário raiz", "Par de chaves SSH do EC2"],
        "correta": "Chave gerenciada pelo cliente",
        "explicacao": "Chaves gerenciadas pelo cliente oferecem controle total sobre políticas de chave, rotação e desativação. Todo uso das chaves do KMS fica registrado no CloudTrail."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer criptografar os dados antes mesmo de enviá-los à AWS, mantendo o controle total do processo de criptografia. Qual abordagem é essa?",
        "alternativas": ["Criptografia no lado do cliente", "Criptografia no lado do servidor com SSE-S3", "Criptografia em trânsito com TLS", "Bloqueio de acesso público do S3"],
        "correta": "Criptografia no lado do cliente",
        "explicacao": "Na criptografia no lado do cliente, os dados são criptografados pela própria aplicação antes do envio, e a AWS armazena apenas dados já criptografados."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer garantir que nenhum bucket do S3 da conta possa ser exposto publicamente por engano. Qual recurso deve ser ativado?",
        "alternativas": ["Bloqueio de acesso público do S3 (S3 Block Public Access)", "Políticas de ciclo de vida do S3 aplicadas a todos os buckets", "S3 Transfer Acceleration", "Classe de armazenamento S3 Standard-IA com acesso infrequente"],
        "correta": "Bloqueio de acesso público do S3 (S3 Block Public Access)",
        "explicacao": "O S3 Block Public Access impede que políticas ou ACLs concedam acesso público, podendo ser aplicado a toda a conta. Ele vem ativado por padrão em novos buckets."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Por exigência regulatória, uma empresa precisa garantir que certos objetos do S3 não possam ser excluídos nem alterados durante 7 anos (modelo WORM). Qual recurso atende a esse requisito?",
        "alternativas": ["S3 Object Lock", "S3 Intelligent-Tiering", "S3 Transfer Acceleration", "Políticas de ciclo de vida do S3"],
        "correta": "S3 Object Lock",
        "explicacao": "O S3 Object Lock armazena objetos no modelo WORM (write once, read many), impedindo exclusão ou alteração durante o período de retenção definido."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer se proteger contra a exclusão ou a substituição acidental de objetos no S3, podendo recuperar versões anteriores. Qual recurso deve ser ativado?",
        "alternativas": ["Versionamento do S3", "S3 Transfer Acceleration", "Hospedagem de site estático", "S3 Select"],
        "correta": "Versionamento do S3",
        "explicacao": "Com o versionamento, o S3 mantém várias versões de cada objeto. Se um objeto for sobrescrito ou excluído, é possível restaurar uma versão anterior."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma aplicação precisa permitir que um cliente baixe um arquivo privado do S3 por tempo limitado, sem tornar o objeto público nem criar credenciais para o cliente. Qual recurso deve ser usado?",
        "alternativas": ["URL pré-assinada (presigned URL)", "Política de bucket pública", "Desativar o bloqueio de acesso público", "Criar um usuário do IAM para o cliente"],
        "correta": "URL pré-assinada (presigned URL)",
        "explicacao": "Uma URL pré-assinada concede acesso temporário a um objeto específico usando as permissões de quem a gerou, com prazo de expiração definido."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer gerenciar de forma centralizada as regras do AWS WAF, as proteções do AWS Shield Advanced e os security groups em todas as contas da organização. Qual serviço deve ser usado?",
        "alternativas": ["AWS Firewall Manager", "AWS Network Firewall", "Amazon GuardDuty", "AWS Config"],
        "correta": "AWS Firewall Manager",
        "explicacao": "O AWS Firewall Manager aplica e gerencia de forma centralizada regras de firewall em várias contas e recursos do AWS Organizations."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson precisa de um firewall de rede gerenciado, com inspeção de tráfego e filtragem de pacotes com estado, para proteger suas VPCs. Qual serviço deve ser usado?",
        "alternativas": ["AWS Network Firewall", "AWS WAF", "AWS Shield Standard", "Amazon Macie"],
        "correta": "AWS Network Firewall",
        "explicacao": "O AWS Network Firewall protege as VPCs com regras de filtragem stateful e stateless e prevenção de intrusões, enquanto o WAF atua na camada de aplicação web (HTTP)."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson assinou o AWS Shield Advanced. Qual benefício adicional ela recebe em relação ao Shield Standard?",
        "alternativas": ["Acesso à equipe de resposta do Shield e proteção de custos em picos de uso causados por ataques DDoS", "Proteção automática contra vírus e malware nos computadores e celulares dos funcionários e dos parceiros da empresa", "Criptografia automática de todos os buckets do S3 e dos volumes EBS com chaves dedicadas gerenciadas pela AWS para cada cliente", "Descontos em instâncias EC2"],
        "correta": "Acesso à equipe de resposta do Shield e proteção de custos em picos de uso causados por ataques DDoS",
        "explicacao": "O Shield Advanced oferece detecção aprimorada, suporte da Shield Response Team (SRT) 24x7, visibilidade de ataques e proteção contra cobranças causadas por ataques DDoS."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Em quais serviços o AWS WAF pode ser implantado para proteger aplicações web?",
        "alternativas": ["Amazon CloudFront, Application Load Balancer e Amazon API Gateway", "Somente instâncias EC2 individuais, por meio de um agente instalado no sistema", "Somente volumes Amazon EBS", "Somente buckets do S3 Glacier usados para arquivar logs de acesso"],
        "correta": "Amazon CloudFront, Application Load Balancer e Amazon API Gateway",
        "explicacao": "O AWS WAF se integra a serviços que recebem tráfego HTTP/HTTPS, como CloudFront, ALB, API Gateway, AWS AppSync e Amazon Cognito."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma equipe quer registrar informações sobre o tráfego IP que entra e sai das interfaces de rede da VPC, para investigar conexões rejeitadas. Qual recurso deve ser ativado?",
        "alternativas": ["Logs de fluxo da VPC (VPC Flow Logs)", "AWS CloudTrail", "Relatório de credenciais do IAM", "AWS Artifact"],
        "correta": "Logs de fluxo da VPC (VPC Flow Logs)",
        "explicacao": "Os VPC Flow Logs capturam metadados do tráfego IP, como origem, destino, porta e se a conexão foi aceita ou rejeitada, e podem ser enviados ao CloudWatch Logs ou ao S3."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer acessar suas instâncias EC2 sem abrir a porta SSH nem manter bastion hosts, com registro de todas as sessões. Qual recurso deve ser usado?",
        "alternativas": ["AWS Systems Manager Session Manager", "Abrir a porta 22 para 0.0.0.0/0", "AWS Direct Connect", "Amazon CloudFront"],
        "correta": "AWS Systems Manager Session Manager",
        "explicacao": "O Session Manager oferece acesso seguro às instâncias pelo console ou pela CLI, sem portas de entrada abertas, com controle via IAM e registro das sessões."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Instâncias em uma sub-rede privada precisam acessar o Amazon S3 sem que o tráfego passe pela internet. Qual recurso deve ser usado?",
        "alternativas": ["Um endpoint da VPC (VPC endpoint) para o S3", "Um internet gateway", "Um IP elástico em cada instância", "Uma distribuição do Amazon CloudFront"],
        "correta": "Um endpoint da VPC (VPC endpoint) para o S3",
        "explicacao": "Os endpoints da VPC permitem conectar a VPC a serviços da AWS de forma privada, sem internet gateway, NAT ou IPs públicos. Para o S3 e o DynamoDB existem endpoints de gateway."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual afirmação sobre o security group padrão de uma VPC está correta?",
        "alternativas": ["Ele não permite tráfego de entrada vindo da internet e permite todo o tráfego de saída", "Ele permite todo o tráfego de entrada da internet e bloqueia todo o tráfego de saída por padrão", "Ele bloqueia todo o tráfego de saída e permite apenas a entrada de conexões pela porta 22 (SSH)", "Ele aceita regras de negação explícita para bloquear endereços IP específicos da internet"],
        "correta": "Ele não permite tráfego de entrada vindo da internet e permite todo o tráfego de saída",
        "explicacao": "Por padrão, security groups não permitem entrada (exceto entre membros do mesmo grupo padrão) e permitem toda a saída. Não existem regras de negação em security groups."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Por que, em uma Network ACL, é preciso criar regras tanto para o tráfego de entrada quanto para o tráfego de resposta?",
        "alternativas": ["Porque as Network ACLs são stateless e não liberam automaticamente o tráfego de retorno", "Porque as Network ACLs só funcionam com IPv6", "Porque as Network ACLs são aplicadas apenas a instâncias individuais", "Porque as Network ACLs negam todo tráfego de saída por padrão em qualquer VPC"],
        "correta": "Porque as Network ACLs são stateless e não liberam automaticamente o tráfego de retorno",
        "explicacao": "Como as Network ACLs não guardam estado, o tráfego de resposta precisa ser permitido explicitamente. Já os security groups são stateful e liberam a resposta automaticamente."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer aplicar defesa em profundidade na VPC. Qual combinação de recursos de rede representa essa abordagem?",
        "alternativas": ["Network ACLs no nível da sub-rede e security groups no nível da instância", "Apenas um internet gateway com rotas públicas para todas as sub-redes da VPC", "Apenas tabelas de rotas bem configuradas, sem nenhum outro controle de acesso", "Apenas IPs elásticos"],
        "correta": "Network ACLs no nível da sub-rede e security groups no nível da instância",
        "explicacao": "Defesa em profundidade é aplicar segurança em várias camadas. Na VPC, isso inclui Network ACLs, security groups, WAF e outros controles combinados."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual tipo de evento o AWS CloudTrail registra por padrão no histórico de eventos, sem nenhuma configuração adicional?",
        "alternativas": ["Eventos de gerenciamento dos últimos 90 dias", "Todo o conteúdo dos objetos do S3", "Métricas de CPU das instâncias", "Os pacotes de rede trafegados na VPC"],
        "correta": "Eventos de gerenciamento dos últimos 90 dias",
        "explicacao": "O histórico de eventos do CloudTrail mostra 90 dias de eventos de gerenciamento sem custo. Para retenção maior, cria-se uma trilha que envia os logs ao S3 ou usa-se o CloudTrail Lake."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson precisa guardar os registros de atividade de API de todas as contas da organização por 7 anos para auditoria. O que deve ser configurado?",
        "alternativas": ["Uma trilha organizacional do AWS CloudTrail entregando os logs em um bucket do S3", "Alarmes do Amazon CloudWatch", "O AWS Artifact", "O histórico de eventos padrão do CloudTrail, que guarda os registros de cada conta automaticamente"],
        "correta": "Uma trilha organizacional do AWS CloudTrail entregando os logs em um bucket do S3",
        "explicacao": "Uma trilha da organização registra eventos de todas as contas e os entrega no S3, onde podem ser retidos pelo tempo necessário com políticas de ciclo de vida e Object Lock."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "O AWS Config detectou que um bucket do S3 ficou público. A empresa quer que isso seja corrigido automaticamente. Qual recurso do AWS Config permite essa ação?",
        "alternativas": ["Ações de correção (remediação) automática", "Relatórios de conformidade gerados pelo AWS Artifact", "Logs de fluxo da VPC", "Planos do AWS Support"],
        "correta": "Ações de correção (remediação) automática",
        "explicacao": "As regras do AWS Config podem acionar ações de correção, executadas por documentos de automação do Systems Manager, para corrigir recursos fora de conformidade."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer armazenar parâmetros de configuração e alguns valores sensíveis de forma hierárquica, com integração ao IAM e ao KMS, sem precisar de rotação automática de credenciais. Qual recurso é uma opção econômica?",
        "alternativas": ["AWS Systems Manager Parameter Store", "AWS CloudHSM com HSMs dedicados", "AWS Certificate Manager (ACM)", "AWS Key Management Service (AWS KMS)"],
        "correta": "AWS Systems Manager Parameter Store",
        "explicacao": "O Parameter Store armazena configurações e segredos (como SecureString criptografado com KMS). O Secrets Manager é indicado quando se precisa de rotação automática de credenciais."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual é a diferença entre os grupos de usuários e os grupos de identidades do Amazon Cognito?",
        "alternativas": ["Grupos de usuários autenticam os usuários; grupos de identidades fornecem credenciais temporárias da AWS a eles", "Grupos de usuários criptografam os dados dos aplicativos; grupos de identidades bloqueiam ataques DDoS na borda da rede", "Os dois servem apenas para funcionários internos acessarem o console da AWS com o login corporativo e permissões de administrador", "Grupos de identidades substituem o AWS IAM"],
        "correta": "Grupos de usuários autenticam os usuários; grupos de identidades fornecem credenciais temporárias da AWS a eles",
        "explicacao": "Os grupos de usuários (user pools) são diretórios para cadastro e login. Os grupos de identidades (identity pools) trocam essa identidade por credenciais temporárias para acessar serviços da AWS."
    },
]

QUESTOES += [
    {
        "dominio_id": 2,
        "template_pergunta": "O Amazon GuardDuty gerou um alerta indicando que uma instância EC2 está se comunicando com um endereço IP conhecido por mineração de criptomoedas. Como se chama esse alerta no GuardDuty?",
        "alternativas": ["Descoberta (finding)", "Regra de conformidade", "Relatório de auditoria", "Política de controle de serviço"],
        "correta": "Descoberta (finding)",
        "explicacao": "O GuardDuty gera descobertas (findings) com o tipo de ameaça, a gravidade e os recursos afetados, que podem acionar respostas automáticas via Amazon EventBridge."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual afirmação sobre a ativação do Amazon GuardDuty está correta?",
        "alternativas": ["Ele é ativado com poucos cliques e analisa fontes de dados sem exigir a instalação de agentes nas instâncias", "Ele exige instalar um agente em cada instância antes de funcionar e só analisa instâncias Linux com o agente atualizado", "Ele só funciona em contas com o plano de suporte Enterprise", "Ele precisa de um appliance físico instalado no data center do cliente para inspecionar todo o tráfego de rede da conta"],
        "correta": "Ele é ativado com poucos cliques e analisa fontes de dados sem exigir a instalação de agentes nas instâncias",
        "explicacao": "O GuardDuty consome diretamente fontes como CloudTrail, VPC Flow Logs e logs de DNS, sem impacto na performance das cargas de trabalho."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual é a diferença entre o Amazon Inspector e o Amazon GuardDuty?",
        "alternativas": ["O Inspector procura vulnerabilidades em softwares e configurações; o GuardDuty detecta atividades maliciosas e comportamentos suspeitos", "O Inspector detecta e bloqueia ataques DDoS na borda; o GuardDuty emite e renova certificados SSL/TLS para os sites e aplicações da conta", "Os dois servem apenas para analisar custos e recomendar Instâncias Reservadas com base no histórico de uso da conta", "O GuardDuty substitui o IAM"],
        "correta": "O Inspector procura vulnerabilidades em softwares e configurações; o GuardDuty detecta atividades maliciosas e comportamentos suspeitos",
        "explicacao": "O Inspector avalia o que pode ser explorado (vulnerabilidades). O GuardDuty identifica ameaças que estão acontecendo, como acessos incomuns ou comunicação com IPs maliciosos."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual é a diferença entre o Amazon Macie e o Amazon GuardDuty?",
        "alternativas": ["O Macie descobre e classifica dados sensíveis no S3; o GuardDuty detecta ameaças na conta e nas cargas de trabalho", "O Macie bloqueia o tráfego de rede suspeito nas VPCs; o GuardDuty criptografa automaticamente os dados armazenados no S3", "Os dois são ferramentas de estimativa de custos", "O Macie gerencia usuários e grupos do IAM; o GuardDuty gerencia senhas, rotação e chaves de acesso de todos os usuários"],
        "correta": "O Macie descobre e classifica dados sensíveis no S3; o GuardDuty detecta ameaças na conta e nas cargas de trabalho",
        "explicacao": "O Macie foca na proteção de dados sensíveis armazenados no S3. O GuardDuty foca na detecção contínua de ameaças e atividades maliciosas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer centralizar dados de segurança de várias contas e fontes em um data lake próprio, usando o formato padronizado OCSF. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Security Lake", "Amazon Athena", "Amazon OpenSearch Service", "AWS Backup"],
        "correta": "Amazon Security Lake",
        "explicacao": "O Amazon Security Lake centraliza automaticamente dados de segurança da AWS, de ambientes on-premises e de terceiros em um data lake na conta do cliente, normalizados no padrão OCSF."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer realizar testes de intrusão (pentest) em seus próprios recursos na AWS. Qual afirmação está correta?",
        "alternativas": ["É permitido testar uma lista de serviços aprovados sem autorização prévia, seguindo a política da AWS", "É proibido realizar qualquer teste de intrusão na AWS", "É preciso contratar o plano Enterprise e pedir autorização por escrito antes de qualquer teste em qualquer serviço", "É permitido testar qualquer serviço, inclusive a infraestrutura física e a rede interna da AWS, sem aviso"],
        "correta": "É permitido testar uma lista de serviços aprovados sem autorização prévia, seguindo a política da AWS",
        "explicacao": "A política de testes de intrusão da AWS permite testar sem aprovação prévia serviços como EC2, RDS, Lambda e outros listados, mas proíbe atividades como ataques DDoS ou testes na infraestrutura da AWS."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson percebeu que endereços IP da AWS estão sendo usados para enviar spam e ataques contra seus sistemas. A quem ela deve reportar esse uso indevido?",
        "alternativas": ["À equipe AWS Trust & Safety, por meio do formulário de denúncia de abuso", "Ao AWS Marketplace", "À equipe de faturamento da AWS, por meio de um caso de suporte de conta e faturamento", "Ao AWS Partner Network, por meio do portal de parceiros e do formulário de contato"],
        "correta": "À equipe AWS Trust & Safety, por meio do formulário de denúncia de abuso",
        "explicacao": "Atividades abusivas originadas de recursos da AWS, como spam, varreduras de portas e ataques, devem ser reportadas à equipe AWS Trust & Safety."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Um desenvolvedor publicou por engano as chaves de acesso de um usuário do IAM em um repositório público. Qual deve ser a primeira ação?",
        "alternativas": ["Desativar e excluir as chaves expostas e criar novas, se necessário", "Aguardar para ver se alguém usa as chaves antes de tomar qualquer providência", "Apenas mudar a senha do console do usuário dono das chaves expostas", "Tornar o repositório privado e não fazer mais nada, pois as chaves deixam de ser visíveis"],
        "correta": "Desativar e excluir as chaves expostas e criar novas, se necessário",
        "explicacao": "Credenciais expostas devem ser revogadas imediatamente. Em seguida, deve-se revisar o CloudTrail em busca de uso não autorizado e remover recursos criados indevidamente."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Por que a AWS recomenda rotacionar periodicamente as chaves de acesso de longo prazo dos usuários do IAM?",
        "alternativas": ["Para reduzir o tempo em que uma chave comprometida pode ser usada", "Para reduzir o custo da conta, já que chaves antigas são cobradas por mês", "Para aumentar o limite de instâncias EC2 que o usuário pode criar na conta", "Porque as chaves de acesso deixam de funcionar automaticamente após 24 horas"],
        "correta": "Para reduzir o tempo em que uma chave comprometida pode ser usada",
        "explicacao": "Rotacionar credenciais limita a janela de exposição. Melhor ainda é substituir chaves de longo prazo por credenciais temporárias, como funções do IAM."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson precisa emitir certificados privados para comunicação interna entre microsserviços, criando sua própria autoridade certificadora gerenciada. Qual serviço deve ser usado?",
        "alternativas": ["AWS Private Certificate Authority", "AWS Key Management Service (AWS KMS)", "Amazon Cognito", "AWS Artifact"],
        "correta": "AWS Private Certificate Authority",
        "explicacao": "O AWS Private CA permite criar uma hierarquia de autoridades certificadoras privadas gerenciadas, para emitir certificados de uso interno."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma função AWS Lambda precisa gravar itens em uma tabela do DynamoDB. Como as permissões devem ser concedidas a ela?",
        "alternativas": ["Por meio de uma função de execução do IAM com permissão para a tabela", "Gravando as chaves de acesso do usuário raiz nas variáveis de ambiente da função", "Tornando a tabela pública para que qualquer função possa gravar itens nela", "Criando um usuário do IAM para cada execução da função, com chaves de acesso próprias"],
        "correta": "Por meio de uma função de execução do IAM com permissão para a tabela",
        "explicacao": "Cada função Lambda assume uma função de execução do IAM, que fornece credenciais temporárias com as permissões necessárias, seguindo o privilégio mínimo."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer impedir que um administrador delegue a um usuário do IAM mais permissões do que um limite definido, mesmo que anexe políticas amplas. Qual recurso do IAM define esse teto para uma identidade?",
        "alternativas": ["Limite de permissões (permissions boundary)", "Grupo do IAM com uma política gerenciada pela AWS", "Política de senhas", "Relatório de credenciais do IAM"],
        "correta": "Limite de permissões (permissions boundary)",
        "explicacao": "Um permissions boundary define as permissões máximas que uma política baseada em identidade pode conceder a um usuário ou função do IAM."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual afirmação sobre as políticas de controle de serviço (SCPs) do AWS Organizations está correta?",
        "alternativas": ["Elas limitam as permissões máximas nas contas, mas não concedem permissões por si só", "Elas concedem permissões de administrador a todos os usuários", "Elas substituem a necessidade de políticas do IAM", "Elas só podem ser aplicadas ao usuário raiz da conta de gerenciamento"],
        "correta": "Elas limitam as permissões máximas nas contas, mas não concedem permissões por si só",
        "explicacao": "As SCPs funcionam como um filtro: uma ação só é permitida se for autorizada pela SCP e também por uma política do IAM. As SCPs não afetam a conta de gerenciamento."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer bloquear, em todas as contas da organização, a criação de recursos fora das Regiões de São Paulo e do Norte da Virgínia. Qual é a forma mais eficaz?",
        "alternativas": ["Criar uma SCP que negue ações fora das Regiões permitidas", "Pedir aos usuários que escolham a Região correta", "Criar um alarme do CloudWatch", "Configurar um security group restritivo"],
        "correta": "Criar uma SCP que negue ações fora das Regiões permitidas",
        "explicacao": "Uma SCP com a condição aws:RequestedRegion pode negar ações em Regiões não aprovadas, garantindo o requisito em todas as contas da organização."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer que um bucket do S3 aceite somente requisições feitas por HTTPS. Como isso pode ser garantido?",
        "alternativas": ["Com uma política de bucket que negue requisições quando aws:SecureTransport for falso", "Ativando o S3 Transfer Acceleration, que usa somente conexões criptografadas pela rede de borda", "Mudando a classe de armazenamento para S3 Standard-IA, que só aceita conexões feitas por HTTPS", "Ativando o versionamento"],
        "correta": "Com uma política de bucket que negue requisições quando aws:SecureTransport for falso",
        "explicacao": "A condição aws:SecureTransport em uma política de bucket permite negar acessos sem TLS, garantindo a criptografia em trânsito."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual afirmação sobre a criptografia de dados no Amazon DynamoDB está correta?",
        "alternativas": ["Todos os dados do DynamoDB são criptografados em repouso por padrão", "O DynamoDB não oferece criptografia em repouso", "A criptografia só está disponível com o plano Enterprise", "É preciso instalar um agente para criptografar as tabelas"],
        "correta": "Todos os dados do DynamoDB são criptografados em repouso por padrão",
        "explicacao": "O DynamoDB criptografa todas as tabelas em repouso usando chaves do AWS KMS, com opção de chave pertencente à AWS, gerenciada pela AWS ou gerenciada pelo cliente."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer garantir que uma instância de banco de dados do Amazon RDS tenha seus dados criptografados em repouso. Quando essa opção deve ser escolhida?",
        "alternativas": ["Ao criar a instância de banco de dados", "Somente após um ano de uso", "A criptografia é ativada automaticamente apenas ao trocar de Região", "O RDS não permite criptografia em repouso"],
        "correta": "Ao criar a instância de banco de dados",
        "explicacao": "A criptografia do RDS é definida na criação. Para criptografar um banco existente, é preciso criar um snapshot, copiá-lo com criptografia e restaurá-lo."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Quais são as principais diferenças entre o AWS KMS e o AWS CloudHSM?",
        "alternativas": ["O KMS é um serviço gerenciado multilocatário integrado a muitos serviços; o CloudHSM oferece HSMs dedicados, de inquilino único, controlados pelo cliente", "O KMS é totalmente gratuito e só armazena senhas; o CloudHSM é usado apenas para emitir certificados SSL/TLS públicos para sites", "O CloudHSM é integrado nativamente a todos os serviços da AWS; o KMS só funciona com aplicações on-premises e exige um appliance de hardware instalado pelo cliente", "Não há diferenças entre eles"],
        "correta": "O KMS é um serviço gerenciado multilocatário integrado a muitos serviços; o CloudHSM oferece HSMs dedicados, de inquilino único, controlados pelo cliente",
        "explicacao": "O KMS atende à maioria dos casos de criptografia com facilidade. O CloudHSM é indicado quando há exigência de hardware dedicado e controle exclusivo das chaves."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Um auditor quer saber quem usou uma chave do AWS KMS para descriptografar dados e quando isso ocorreu. Onde essa informação pode ser encontrada?",
        "alternativas": ["Nos logs do AWS CloudTrail", "No AWS Artifact", "No AWS Cost Explorer", "No AWS Health Dashboard"],
        "correta": "Nos logs do AWS CloudTrail",
        "explicacao": "Todas as chamadas de API ao AWS KMS, como Encrypt e Decrypt, ficam registradas no CloudTrail, permitindo auditar o uso das chaves."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer exigir MFA para que qualquer usuário possa excluir permanentemente versões de objetos em um bucket do S3 com versionamento. Qual recurso deve ser configurado?",
        "alternativas": ["MFA Delete do S3", "S3 Transfer Acceleration", "S3 Intelligent-Tiering", "Hospedagem de site estático"],
        "correta": "MFA Delete do S3",
        "explicacao": "O MFA Delete exige autenticação multifator para excluir versões de objetos ou alterar o estado do versionamento, adicionando uma camada de proteção."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer bloquear o acesso à sua aplicação web vindo de determinados países. Qual serviço permite criar essa regra de bloqueio geográfico?",
        "alternativas": ["AWS WAF", "AWS Artifact", "Amazon Macie", "AWS Budgets"],
        "correta": "AWS WAF",
        "explicacao": "O AWS WAF permite criar regras de correspondência geográfica para bloquear ou permitir requisições conforme o país de origem. O CloudFront também oferece restrição geográfica."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma aplicação está recebendo milhares de requisições por minuto de um mesmo endereço IP, em uma tentativa de força bruta no login. Qual recurso do AWS WAF ajuda a mitigar isso?",
        "alternativas": ["Regras baseadas em taxa (rate-based rules)", "Pacotes de conformidade (conformance packs)", "Políticas de ciclo de vida de objetos do S3", "Tags de alocação de custos"],
        "correta": "Regras baseadas em taxa (rate-based rules)",
        "explicacao": "Regras baseadas em taxa bloqueiam temporariamente origens que excedem um número definido de requisições em um intervalo de tempo."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer proteger rapidamente sua aplicação contra ameaças comuns, como as do OWASP Top 10, sem escrever todas as regras do zero. Qual recurso do AWS WAF pode ser usado?",
        "alternativas": ["Grupos de regras gerenciadas", "Políticas de senha do IAM", "Pacotes de conformidade do AWS Config", "Logs de fluxo da VPC"],
        "correta": "Grupos de regras gerenciadas",
        "explicacao": "O AWS WAF oferece grupos de regras gerenciadas pela AWS e por vendedores do AWS Marketplace, que protegem contra vulnerabilidades comuns e são atualizados automaticamente."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Contra quais tipos de ataque o AWS Shield Standard protege automaticamente?",
        "alternativas": ["Ataques DDoS comuns nas camadas de rede e transporte, como inundações SYN e UDP", "Injeção de SQL e cross-site scripting nas aplicações web, na camada 7 do modelo OSI", "Roubo de senhas por phishing", "Vazamento de dados sensíveis armazenados em buckets do S3 configurados com acesso público"],
        "correta": "Ataques DDoS comuns nas camadas de rede e transporte, como inundações SYN e UDP",
        "explicacao": "O Shield Standard protege contra os ataques DDoS de infraestrutura mais frequentes (camadas 3 e 4). Ataques de aplicação, como injeção de SQL, são tratados pelo AWS WAF."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual arquitetura aumenta a resiliência de uma aplicação web contra ataques DDoS?",
        "alternativas": ["Usar Amazon CloudFront e Amazon Route 53 na frente da aplicação, com AWS WAF e AWS Shield", "Expor as instâncias EC2 diretamente com IPs elásticos e deixar cada instância absorver o tráfego do ataque", "Usar uma única instância EC2 grande o bastante para absorver qualquer volume de tráfego do ataque", "Desativar o balanceador de carga"],
        "correta": "Usar Amazon CloudFront e Amazon Route 53 na frente da aplicação, com AWS WAF e AWS Shield",
        "explicacao": "Serviços de borda como CloudFront e Route 53 absorvem e distribuem o tráfego pela rede global da AWS, reduzindo a superfície de ataque da origem."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma equipe quer que apenas as instâncias do security group do servidor web possam acessar o banco de dados na porta 3306. Como isso pode ser configurado de forma simples?",
        "alternativas": ["Criar uma regra no security group do banco que referencie o security group do servidor web como origem", "Abrir a porta 3306 para 0.0.0.0/0 no security group do banco e confiar na senha do usuário do banco de dados", "Desativar o security group do banco e controlar o acesso somente pela senha e pelo usuário configurados no banco de dados", "Criar uma política de bucket do S3"],
        "correta": "Criar uma regra no security group do banco que referencie o security group do servidor web como origem",
        "explicacao": "Security groups podem usar outros security groups como origem, permitindo acesso apenas às instâncias associadas a eles, sem depender de endereços IP."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer automatizar a aplicação de patches de segurança no sistema operacional de centenas de instâncias EC2, seguindo janelas de manutenção. Qual recurso deve ser usado?",
        "alternativas": ["AWS Systems Manager Patch Manager", "AWS Artifact", "Amazon Macie", "AWS Systems Manager Session Manager"],
        "correta": "AWS Systems Manager Patch Manager",
        "explicacao": "O Patch Manager automatiza a aplicação de patches em instâncias gerenciadas, de acordo com linhas de base e janelas de manutenção definidas pelo cliente."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer proteger seus backups contra exclusão, inclusive por administradores, para se defender de ransomware. Qual recurso pode ser usado?",
        "alternativas": ["AWS Backup Vault Lock", "S3 Transfer Acceleration", "Amazon CloudFront", "Amazon EC2 Auto Scaling"],
        "correta": "AWS Backup Vault Lock",
        "explicacao": "O AWS Backup Vault Lock aplica proteção WORM aos cofres de backup, impedindo que os backups sejam excluídos ou que suas configurações de retenção sejam alteradas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson, no Brasil, armazena dados pessoais na AWS. Quem é responsável por garantir que o tratamento desses dados atenda à LGPD?",
        "alternativas": ["O cliente, que controla como os dados são coletados, usados e protegidos", "A AWS, por ser a responsável pela segurança da nuvem e dos data centers", "O AWS Marketplace", "O governo brasileiro, por meio da ANPD, que fiscaliza o uso dos dados"],
        "correta": "O cliente, que controla como os dados são coletados, usados e protegidos",
        "explicacao": "A AWS fornece infraestrutura segura e recursos que ajudam na conformidade, mas o cliente é responsável por cumprir as leis de proteção de dados no uso que faz da nuvem."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson obteve, no AWS Artifact, o relatório que mostra que a infraestrutura da AWS está em conformidade com o PCI DSS. Isso significa que a aplicação de pagamentos da empresa também está automaticamente em conformidade?",
        "alternativas": ["Não: o cliente também precisa garantir a conformidade da sua própria aplicação e configuração", "Sim: a conformidade da AWS cobre automaticamente qualquer aplicação executada na infraestrutura certificada", "Sim, desde que a aplicação use instâncias EC2", "Não, porque a AWS não possui certificação PCI DSS e não pode ser usada para dados de cartão de crédito"],
        "correta": "Não: o cliente também precisa garantir a conformidade da sua própria aplicação e configuração",
        "explicacao": "A conformidade é compartilhada: o cliente herda os controles da infraestrutura da AWS, mas precisa implementar e comprovar os controles das suas próprias cargas de trabalho."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer receber avisos sobre vulnerabilidades e problemas de segurança que afetem os serviços da AWS. Onde a AWS publica esse tipo de comunicado?",
        "alternativas": ["Nos boletins de segurança da AWS (AWS Security Bulletins)", "No AWS Cost Explorer", "No AWS Pricing Calculator", "No relatório de faturamento mensal do AWS Billing and Cost Management"],
        "correta": "Nos boletins de segurança da AWS (AWS Security Bulletins)",
        "explicacao": "A AWS publica boletins de segurança sobre vulnerabilidades e as ações recomendadas. Eventos específicos da conta também aparecem no AWS Health Dashboard."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma equipe quer aprender boas práticas de segurança na AWS com artigos técnicos, novidades e soluções de referência publicados pela própria AWS. Qual recurso é adequado?",
        "alternativas": ["AWS Security Blog e AWS Security Center", "AWS Budgets", "AWS Cost and Usage Report", "Portal de vendedores do AWS Marketplace (Seller Portal)"],
        "correta": "AWS Security Blog e AWS Security Center",
        "explicacao": "A AWS disponibiliza documentação, blogs, whitepapers e o centro de segurança com orientações e boas práticas para proteger cargas de trabalho."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer encontrar e comprar soluções de segurança de terceiros, como firewalls de próxima geração e antivírus, já prontas para implantar na AWS. Onde ela deve procurar?",
        "alternativas": ["AWS Marketplace", "AWS Artifact", "AWS Config", "IAM Access Analyzer"],
        "correta": "AWS Marketplace",
        "explicacao": "O AWS Marketplace oferece milhares de produtos de segurança de fornecedores independentes, que podem ser implantados rapidamente e cobrados na fatura da AWS."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Em qual plano do AWS Support o cliente tem acesso a todas as verificações de segurança do AWS Trusted Advisor, e não apenas às verificações principais?",
        "alternativas": ["Business ou superior", "Basic", "Developer", "Todos os planos têm acesso completo"],
        "correta": "Business ou superior",
        "explicacao": "Os planos Basic e Developer incluem as verificações principais do Trusted Advisor. Os planos Business, Enterprise On-Ramp e Enterprise dão acesso ao conjunto completo de verificações."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "O IAM Access Analyzer pode ajudar a aplicar o privilégio mínimo de que forma, além de identificar acessos externos?",
        "alternativas": ["Gerando políticas com base na atividade de acesso registrada no CloudTrail", "Criando automaticamente um usuário do IAM para cada funcionário do diretório corporativo", "Bloqueando ataques DDoS", "Criptografando automaticamente os volumes EBS e os buckets do S3 de toda a conta"],
        "correta": "Gerando políticas com base na atividade de acesso registrada no CloudTrail",
        "explicacao": "O IAM Access Analyzer pode gerar políticas a partir da atividade real, validar políticas contra boas práticas e identificar acessos não utilizados."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer definir quais recursos da AWS podem ser criados e quais configurações são obrigatórias, oferecendo às equipes um catálogo de produtos aprovados. Qual serviço deve ser usado?",
        "alternativas": ["AWS Service Catalog", "AWS Artifact", "Amazon Inspector", "AWS Shield"],
        "correta": "AWS Service Catalog",
        "explicacao": "O AWS Service Catalog permite criar e gerenciar catálogos de produtos aprovados, ajudando a manter a governança e a conformidade nas implantações."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual é a diferença entre o AWS CloudTrail e o Amazon CloudWatch?",
        "alternativas": ["O CloudTrail registra quem fez cada chamada de API; o CloudWatch monitora métricas, logs e alarmes de desempenho", "O CloudTrail monitora o uso de CPU e memória das instâncias; o CloudWatch registra quem fez cada chamada de API na conta", "Os dois servem apenas para faturamento, mostrando o custo das chamadas de API e das métricas coletadas em cada conta", "O CloudWatch substitui o IAM"],
        "correta": "O CloudTrail registra quem fez cada chamada de API; o CloudWatch monitora métricas, logs e alarmes de desempenho",
        "explicacao": "O CloudTrail é voltado à auditoria das ações na conta. O CloudWatch é voltado ao monitoramento operacional de recursos e aplicações."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual é a diferença entre o AWS CloudTrail e o AWS Config?",
        "alternativas": ["O CloudTrail registra as ações (chamadas de API); o Config registra o estado e as mudanças de configuração dos recursos ao longo do tempo", "O CloudTrail avalia os custos de cada chamada de API; o Config cria usuários e grupos do IAM automaticamente para cada equipe da empresa", "O Config bloqueia ataques DDoS na borda da rede; o CloudTrail emite e renova automaticamente os certificados SSL/TLS das aplicações", "Não há diferença entre eles"],
        "correta": "O CloudTrail registra as ações (chamadas de API); o Config registra o estado e as mudanças de configuração dos recursos ao longo do tempo",
        "explicacao": "O CloudTrail responde 'quem fez o quê e quando'. O Config responde 'como este recurso estava configurado e se ele está em conformidade'."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson precisa armazenar os logs das suas aplicações, definir por quanto tempo serão retidos e pesquisá-los durante investigações. Qual serviço deve ser usado?",
        "alternativas": ["Amazon CloudWatch Logs", "AWS Artifact", "AWS Budgets", "AWS Cost Explorer"],
        "correta": "Amazon CloudWatch Logs",
        "explicacao": "O CloudWatch Logs centraliza logs de aplicações e serviços, permite definir a retenção e consultá-los com o CloudWatch Logs Insights."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer registrar todas as requisições feitas aos objetos de um bucket do S3, como quem acessou e quando, para fins de auditoria. Quais recursos podem ser usados?",
        "alternativas": ["Logs de acesso ao servidor do S3 ou eventos de dados do CloudTrail", "Somente o histórico de eventos padrão do CloudTrail, sem nenhuma configuração", "AWS Budgets", "Métricas de requisições do S3 no Amazon CloudWatch, que mostram o total por bucket"],
        "correta": "Logs de acesso ao servidor do S3 ou eventos de dados do CloudTrail",
        "explicacao": "Os eventos de gerenciamento não registram operações nos objetos. Para isso, ativam-se os logs de acesso do S3 ou os eventos de dados do CloudTrail."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual afirmação sobre a responsabilidade pela criptografia de dados na AWS está correta?",
        "alternativas": ["A AWS fornece as ferramentas de criptografia, e o cliente decide quando e como usá-las", "A AWS é sempre a única responsável por criptografar os dados do cliente", "A criptografia é proibida em alguns serviços", "A criptografia só pode ser feita on-premises"],
        "correta": "A AWS fornece as ferramentas de criptografia, e o cliente decide quando e como usá-las",
        "explicacao": "A proteção dos dados é responsabilidade do cliente, que escolhe usar recursos como KMS, criptografia do S3, EBS e RDS e TLS para dados em trânsito."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Um usuário do IAM precisa acessar a conta somente pelo console. Qual prática é recomendada para suas credenciais?",
        "alternativas": ["Criar apenas uma senha de console com MFA, sem chaves de acesso", "Criar chaves de acesso e senha mesmo sem necessidade", "Compartilhar um único usuário entre várias pessoas", "Usar o usuário raiz com uma senha fácil de lembrar"],
        "correta": "Criar apenas uma senha de console com MFA, sem chaves de acesso",
        "explicacao": "Seguindo o privilégio mínimo, cada pessoa deve receber somente os tipos de credencial de que precisa. Credenciais desnecessárias aumentam a superfície de ataque."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Por que não se deve compartilhar um mesmo usuário do IAM entre vários funcionários?",
        "alternativas": ["Porque perde-se a rastreabilidade individual das ações e fica difícil revogar o acesso de uma só pessoa", "Porque a AWS cobra uma taxa adicional por usuário compartilhado entre várias pessoas da mesma equipe de trabalho", "Porque usuários compartilhados não podem usar o console nem a CLI ao mesmo tempo em computadores diferentes", "Porque o IAM permite apenas um login por dia em cada usuário, bloqueando o acesso dos demais funcionários até o dia seguinte"],
        "correta": "Porque perde-se a rastreabilidade individual das ações e fica difícil revogar o acesso de uma só pessoa",
        "explicacao": "Identidades individuais permitem auditar quem fez cada ação no CloudTrail e conceder ou remover permissões de forma específica para cada pessoa."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer que os desenvolvedores tenham acesso temporário de administrador apenas durante um incidente. Qual abordagem segue as boas práticas?",
        "alternativas": ["Permitir que assumam uma função do IAM com permissões elevadas, com credenciais temporárias e registro no CloudTrail", "Conceder permissão de administrador permanente a todos os desenvolvedores, para que estejam prontos para qualquer incidente", "Compartilhar a senha do usuário raiz durante o incidente e trocá-la imediatamente assim que o problema for resolvido pela equipe", "Desativar o CloudTrail durante o incidente"],
        "correta": "Permitir que assumam uma função do IAM com permissões elevadas, com credenciais temporárias e registro no CloudTrail",
        "explicacao": "Funções do IAM fornecem acesso temporário e auditável. Isso evita permissões elevadas permanentes, seguindo o princípio do privilégio mínimo."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual destas é uma boa prática para proteger dados sensíveis armazenados no Amazon S3?",
        "alternativas": ["Manter o bloqueio de acesso público ativado, usar criptografia e conceder acesso com o privilégio mínimo", "Tornar o bucket público para facilitar o acesso e proteger os objetos apenas com nomes difíceis de adivinhar", "Usar o mesmo bucket para dados públicos e confidenciais sem controles, para simplificar a gestão das políticas de acesso", "Desativar o versionamento e os logs"],
        "correta": "Manter o bloqueio de acesso público ativado, usar criptografia e conceder acesso com o privilégio mínimo",
        "explicacao": "A combinação de bloqueio de acesso público, criptografia, políticas restritivas, versionamento e monitoramento (por exemplo, com o Macie) reduz o risco de exposição."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A AWS descarta com segurança os dispositivos de armazenamento que chegam ao fim da vida útil. Segundo o Modelo de Responsabilidade Compartilhada, de quem é essa responsabilidade?",
        "alternativas": ["Da AWS", "Do cliente", "Do fornecedor do sistema operacional", "Do AWS Partner que fez a migração"],
        "correta": "Da AWS",
        "explicacao": "O descarte de mídias faz parte da segurança da nuvem. A AWS segue procedimentos para destruir os dados antes de descartar os dispositivos."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson precisa que funcionários acessem aplicações internas pela internet sem VPN, com acesso verificado a cada requisição com base na identidade e no dispositivo. Qual serviço da AWS atende a essa abordagem de confiança zero?",
        "alternativas": ["AWS Verified Access", "AWS Site-to-Site VPN", "Amazon CloudFront", "AWS Direct Connect"],
        "correta": "AWS Verified Access",
        "explicacao": "O AWS Verified Access concede acesso seguro a aplicações corporativas sem VPN, avaliando cada requisição com base em políticas de identidade e postura do dispositivo."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer avaliar se suas contas seguem as boas práticas de segurança da AWS, recebendo uma pontuação de conformidade com base em padrões como o AWS Foundational Security Best Practices. Qual serviço oferece isso?",
        "alternativas": ["AWS Security Hub", "AWS Cost Explorer", "Amazon Lightsail", "AWS Transfer Family"],
        "correta": "AWS Security Hub",
        "explicacao": "O Security Hub executa verificações automáticas com base em padrões como AWS Foundational Security Best Practices e CIS AWS Foundations Benchmark e mostra a pontuação de segurança."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer que o Amazon GuardDuty e o AWS Security Hub sejam ativados e administrados de forma centralizada para todas as contas da organização. O que ela deve usar?",
        "alternativas": ["A integração desses serviços com o AWS Organizations, usando uma conta de administrador delegado", "Um usuário do IAM em cada conta, todos com a mesma senha, para que a equipe de segurança acesse uma conta por vez", "Ativar cada serviço manualmente em cada conta, com uma equipe de segurança diferente para cada uma", "Um bucket do S3 público"],
        "correta": "A integração desses serviços com o AWS Organizations, usando uma conta de administrador delegado",
        "explicacao": "Muitos serviços de segurança se integram ao AWS Organizations, permitindo que uma conta de administrador delegado gerencie e veja as descobertas de todas as contas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Uma aplicação precisa acessar uma API de terceiros com uma chave secreta. Qual é a forma recomendada de armazenar essa chave?",
        "alternativas": ["No AWS Secrets Manager, recuperando-a em tempo de execução", "Em texto puro no código-fonte, em um arquivo de configuração versionado", "Em uma variável de ambiente definida em um repositório público de código", "No nome da instância EC2, para que a aplicação o leia facilmente"],
        "correta": "No AWS Secrets Manager, recuperando-a em tempo de execução",
        "explicacao": "Armazenar segredos em um serviço dedicado evita expor credenciais no código e permite controlar o acesso por IAM, auditar o uso e rotacionar os valores."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual afirmação sobre a segurança física dos data centers da AWS está correta?",
        "alternativas": ["O acesso é rigorosamente controlado e os clientes não podem visitar os data centers", "Qualquer cliente pode agendar uma visita para inspecionar seus servidores", "Os clientes são responsáveis pela vigilância dos data centers", "Os data centers não passam por auditorias externas"],
        "correta": "O acesso é rigorosamente controlado e os clientes não podem visitar os data centers",
        "explicacao": "A AWS controla o acesso físico com várias camadas de segurança. Em vez de visitas, os clientes podem consultar os relatórios de auditoria de terceiros no AWS Artifact."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer impedir que dados confidenciais armazenados em uma conta sejam copiados para contas da AWS fora da organização. Qual combinação de controles ajuda nesse objetivo?",
        "alternativas": ["Políticas de recurso e SCPs com condições que restrinjam o acesso a identidades da própria organização", "Apenas tags de alocação de custos aplicadas aos buckets, identificando quais dados são confidenciais e quem é o dono", "Apenas alarmes de faturamento que avisam quando há aumento na transferência de dados para fora da conta", "Apenas o AWS Pricing Calculator"],
        "correta": "Políticas de recurso e SCPs com condições que restrinjam o acesso a identidades da própria organização",
        "explicacao": "Condições como aws:PrincipalOrgID em políticas de recurso e SCPs ajudam a criar um perímetro de dados, limitando o acesso a identidades e recursos da organização."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer receber uma notificação imediata sempre que o usuário raiz da conta fizer login no console. Qual combinação de serviços permite isso?",
        "alternativas": ["AWS CloudTrail com uma regra do Amazon EventBridge que envia um alerta pelo Amazon SNS", "AWS Budgets com um alerta de orçamento enviado por e-mail sempre que houver login do usuário raiz", "Amazon S3 com o S3 Transfer Acceleration enviando os logs de login para a equipe de segurança", "AWS Artifact com o AWS Marketplace"],
        "correta": "AWS CloudTrail com uma regra do Amazon EventBridge que envia um alerta pelo Amazon SNS",
        "explicacao": "O CloudTrail registra o login do usuário raiz, o EventBridge detecta o evento e o SNS envia a notificação por e-mail ou SMS."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer verificar se as funções Lambda e as imagens de contêiner no Amazon ECR possuem bibliotecas com vulnerabilidades conhecidas. Qual serviço deve ser ativado?",
        "alternativas": ["Amazon Inspector", "Amazon Macie", "AWS Artifact", "AWS Budgets"],
        "correta": "Amazon Inspector",
        "explicacao": "O Amazon Inspector verifica continuamente instâncias EC2, imagens no ECR e funções Lambda em busca de vulnerabilidades de software e as prioriza por risco."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson precisa demonstrar a um órgão regulador que um determinado controle de segurança está sendo cumprido continuamente pela sua configuração na AWS. Qual serviço ajuda a avaliar e registrar isso automaticamente?",
        "alternativas": ["AWS Config", "AWS Pricing Calculator", "Amazon Polly", "AWS Snowball Edge"],
        "correta": "AWS Config",
        "explicacao": "As regras do AWS Config avaliam continuamente a configuração dos recursos e mantêm o histórico de conformidade, servindo como evidência para auditorias."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual afirmação sobre os grupos do IAM está correta?",
        "alternativas": ["Um grupo contém usuários do IAM e não pode ser usado como identidade para fazer login", "Um grupo pode conter outros grupos aninhados, formando uma hierarquia de permissões entre as equipes", "Um grupo pode assumir funções do IAM e fazer login no console da AWS como se fosse um usuário comum", "Um grupo substitui as políticas de bucket do S3 ao definir o acesso aos objetos armazenados"],
        "correta": "Um grupo contém usuários do IAM e não pode ser usado como identidade para fazer login",
        "explicacao": "Grupos servem para atribuir permissões a vários usuários. Não é possível fazer login como um grupo, e grupos não podem conter outros grupos."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual é a melhor forma de conceder a um serviço da AWS, como o AWS CloudFormation, permissão para criar recursos em nome do usuário?",
        "alternativas": ["Usar uma função de serviço do IAM que o serviço possa assumir", "Fornecer ao serviço a senha do usuário raiz", "Criar chaves de acesso permanentes e colá-las no template", "Desativar todas as políticas do IAM"],
        "correta": "Usar uma função de serviço do IAM que o serviço possa assumir",
        "explicacao": "Funções de serviço permitem que serviços da AWS executem ações em nome do cliente com permissões controladas e credenciais temporárias."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "A lojinha do Alyson quer garantir que somente imagens de máquina (AMIs) aprovadas e com as configurações de segurança corretas sejam usadas para lançar instâncias. Qual prática ajuda nesse objetivo?",
        "alternativas": ["Criar AMIs padronizadas e reforçadas (hardened) e restringir o uso por meio de políticas", "Permitir que qualquer usuário use AMIs públicas da comunidade, mesmo de fornecedores desconhecidos", "Desativar as atualizações do sistema operacional para manter todas as instâncias com a mesma configuração", "Compartilhar AMIs publicamente"],
        "correta": "Criar AMIs padronizadas e reforçadas (hardened) e restringir o uso por meio de políticas",
        "explicacao": "Imagens 'douradas' com configurações seguras reduzem vulnerabilidades. O EC2 Image Builder ajuda a criar e manter essas imagens atualizadas."
    },
    {
        "dominio_id": 2,
        "template_pergunta": "Qual princípio de segurança recomenda usar vários controles independentes em diferentes camadas, para que a falha de um não comprometa todo o ambiente?",
        "alternativas": ["Defesa em profundidade", "Privilégio máximo", "Segurança por obscuridade", "Confiança implícita"],
        "correta": "Defesa em profundidade",
        "explicacao": "Defesa em profundidade combina controles em várias camadas, como borda da rede, VPC, sub-rede, instância, aplicação e dados."
    },
]

# =========================================================================
# AMPLIAÇÃO: DOMÍNIO 3 - TECNOLOGIA E SERVIÇOS
# =========================================================================
QUESTOES += [
    {
        "dominio_id": 3,
        "template_pergunta": "Quais são as formas de interagir com os serviços da AWS para criar e gerenciar recursos?",
        "alternativas": ["Console de Gerenciamento da AWS, AWS CLI, SDKs e ferramentas de infraestrutura como código", "Apenas o Console de Gerenciamento da AWS, já que as APIs são de uso exclusivo da própria AWS", "Apenas ligações para o AWS Support, que cria os recursos solicitados em nome do cliente após aprovação", "Apenas formulários enviados por e-mail para a equipe de provisionamento da AWS em cada Região"],
        "correta": "Console de Gerenciamento da AWS, AWS CLI, SDKs e ferramentas de infraestrutura como código",
        "explicacao": "Todos os serviços da AWS são acessados por APIs, que podem ser usadas pelo console web, pela linha de comando (CLI), por SDKs em diversas linguagens ou por ferramentas como CloudFormation e CDK."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um administrador quer automatizar tarefas executando comandos em scripts no terminal para criar e gerenciar recursos da AWS. Qual ferramenta deve usar?",
        "alternativas": ["AWS Command Line Interface (AWS CLI)", "Console de Gerenciamento da AWS", "AWS Pricing Calculator", "AWS Artifact"],
        "correta": "AWS Command Line Interface (AWS CLI)",
        "explicacao": "A AWS CLI permite controlar os serviços da AWS pela linha de comando e automatizar tarefas por meio de scripts."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um desenvolvedor quer chamar serviços da AWS diretamente do código de sua aplicação em Python, com bibliotecas que cuidam da autenticação e das requisições. O que ele deve usar?",
        "alternativas": ["Um SDK da AWS, como o Boto3 para Python", "O AWS Pricing Calculator", "O AWS Artifact", "Somente o Console de Gerenciamento da AWS"],
        "correta": "Um SDK da AWS, como o Boto3 para Python",
        "explicacao": "Os SDKs da AWS estão disponíveis para várias linguagens, como Python, Java, JavaScript, .NET e Go, e simplificam o uso das APIs da AWS no código."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma equipe quer definir sua infraestrutura na AWS usando linguagens de programação conhecidas, como TypeScript e Python, em vez de escrever templates em YAML. Qual ferramenta deve ser usada?",
        "alternativas": ["AWS Cloud Development Kit (AWS CDK)", "AWS Artifact", "AWS Systems Manager Automation", "AWS Elastic Beanstalk"],
        "correta": "AWS Cloud Development Kit (AWS CDK)",
        "explicacao": "O AWS CDK permite modelar infraestrutura com linguagens de programação e gera templates do AWS CloudFormation para provisionar os recursos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um usuário quer executar comandos da AWS CLI diretamente no navegador, já autenticado com suas credenciais do console, sem instalar nada no computador. Qual recurso deve ser usado?",
        "alternativas": ["AWS CloudShell", "Amazon WorkSpaces", "AWS Systems Manager Patch Manager", "Amazon Lightsail"],
        "correta": "AWS CloudShell",
        "explicacao": "O AWS CloudShell é um shell baseado em navegador, sem custo adicional, com a AWS CLI e outras ferramentas pré-instaladas e as credenciais do usuário do console."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "O que é uma Amazon Machine Image (AMI)?",
        "alternativas": ["Um modelo com o sistema operacional e o software usados para lançar instâncias EC2", "Uma imagem de contêiner armazenada no S3 Glacier para uso no Amazon ECS e no Amazon EKS", "Um certificado de segurança usado para habilitar HTTPS nos sites hospedados em instâncias EC2", "Um tipo de volume de armazenamento em bloco anexado a apenas uma instância por vez"],
        "correta": "Um modelo com o sistema operacional e o software usados para lançar instâncias EC2",
        "explicacao": "A AMI contém as informações necessárias para iniciar uma instância, como o sistema operacional, aplicações e configurações. Podem ser fornecidas pela AWS, pela comunidade, pelo Marketplace ou criadas pelo cliente."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson vai executar um banco de dados em memória que exige grande quantidade de RAM. Qual família de instâncias EC2 é a mais indicada?",
        "alternativas": ["Otimizada para memória", "Otimizada para computação", "Otimizada para armazenamento", "Computação acelerada"],
        "correta": "Otimizada para memória",
        "explicacao": "As instâncias otimizadas para memória, como as famílias R e X, oferecem alta proporção de memória e são indicadas para bancos em memória e análises de grandes volumes de dados."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson vai executar processamento em lote com uso intenso de CPU, como codificação de vídeo e modelagem científica. Qual família de instâncias EC2 é a mais indicada?",
        "alternativas": ["Otimizada para computação", "Otimizada para memória", "Uso geral", "Otimizada para armazenamento"],
        "correta": "Otimizada para computação",
        "explicacao": "As instâncias otimizadas para computação, como a família C, oferecem processadores de alto desempenho para cargas de trabalho que dependem muito de CPU."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação de treinamento de modelos de machine learning precisa de GPUs. Qual família de instâncias EC2 é a mais indicada?",
        "alternativas": ["Computação acelerada", "Uso geral", "Otimizada para memória", "Otimizada para armazenamento"],
        "correta": "Computação acelerada",
        "explicacao": "As instâncias de computação acelerada, como as famílias P, G e Trn, usam GPUs ou chips especializados para machine learning, gráficos e computação de alto desempenho."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson precisa de instâncias com alto desempenho de leitura e gravação sequencial em grandes conjuntos de dados em discos locais, como em data warehouses distribuídos. Qual família de instâncias EC2 é a mais indicada?",
        "alternativas": ["Otimizada para armazenamento", "Computação acelerada", "Otimizada para computação", "Instâncias com desempenho expansível (burstable)"],
        "correta": "Otimizada para armazenamento",
        "explicacao": "As instâncias otimizadas para armazenamento, como as famílias I e D, oferecem armazenamento local de alto desempenho para cargas com muitas operações de E/S."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson vai hospedar um servidor web com uso equilibrado de CPU, memória e rede. Qual família de instâncias EC2 é a mais indicada?",
        "alternativas": ["Uso geral", "Computação acelerada", "Otimizada para armazenamento", "Otimizada para memória"],
        "correta": "Uso geral",
        "explicacao": "As instâncias de uso geral, como as famílias M e T, equilibram recursos de computação, memória e rede e atendem bem servidores web e repositórios de código."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um pequeno empreendedor quer hospedar um site WordPress com um servidor virtual simples, por um preço mensal previsível que já inclui armazenamento e transferência de dados. Qual serviço é o mais indicado?",
        "alternativas": ["Amazon Lightsail", "Amazon EKS", "AWS Outposts", "Amazon EMR"],
        "correta": "Amazon Lightsail",
        "explicacao": "O Amazon Lightsail oferece servidores virtuais, bancos de dados e redes em pacotes simples e com preço mensal previsível, ideal para aplicações e sites simples."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson precisa executar milhares de trabalhos de computação em lote, com a AWS provisionando automaticamente a quantidade e o tipo ideais de recursos. Qual serviço deve ser usado?",
        "alternativas": ["AWS Batch", "Amazon Lightsail", "AWS Elastic Beanstalk", "Amazon AppStream 2.0"],
        "correta": "AWS Batch",
        "explicacao": "O AWS Batch planeja, agenda e executa trabalhos em lote, provisionando os recursos de computação conforme a quantidade e os requisitos dos trabalhos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é o tempo máximo de execução de uma única invocação de uma função AWS Lambda?",
        "alternativas": ["15 minutos", "1 minuto", "24 horas", "Ilimitado"],
        "correta": "15 minutos",
        "explicacao": "Uma invocação do Lambda pode durar até 15 minutos. Tarefas mais longas devem usar serviços como AWS Fargate, AWS Batch ou AWS Step Functions."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma equipe precisa de um registro privado e gerenciado para armazenar e versionar suas imagens de contêiner Docker. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Elastic Container Registry (Amazon ECR)", "Amazon S3 Glacier Flexible Retrieval", "AWS CodeArtifact", "Amazon Elastic File System (Amazon EFS)"],
        "correta": "Amazon Elastic Container Registry (Amazon ECR)",
        "explicacao": "O Amazon ECR é um registro de contêineres totalmente gerenciado, integrado ao ECS, ao EKS e ao Lambda, com verificação de vulnerabilidades das imagens."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer orquestrar contêineres usando uma solução própria da AWS, simples e totalmente gerenciada, sem usar Kubernetes. Qual serviço deve ser escolhido?",
        "alternativas": ["Amazon Elastic Container Service (Amazon ECS)", "Amazon Elastic Kubernetes Service (Amazon EKS)", "Amazon EMR", "AWS Outposts"],
        "correta": "Amazon Elastic Container Service (Amazon ECS)",
        "explicacao": "O Amazon ECS é o serviço de orquestração de contêineres da AWS, que pode executar as tarefas em instâncias EC2 ou no AWS Fargate (serverless)."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um desenvolvedor quer implantar uma aplicação web em contêiner a partir do código-fonte ou de uma imagem, com balanceamento, escalabilidade e HTTPS configurados automaticamente, sem gerenciar infraestrutura. Qual serviço é o mais simples?",
        "alternativas": ["AWS App Runner", "Amazon EC2", "AWS Outposts", "Amazon EMR"],
        "correta": "AWS App Runner",
        "explicacao": "O AWS App Runner implanta aplicações web e APIs em contêineres de forma totalmente gerenciada, cuidando de build, implantação, escalabilidade e balanceamento."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação precisa rotear requisições HTTP com base no caminho da URL, enviando /api para um grupo de servidores e /imagens para outro. Qual tipo de balanceador de carga é o mais indicado?",
        "alternativas": ["Application Load Balancer", "Network Load Balancer", "Gateway Load Balancer", "Classic Load Balancer"],
        "correta": "Application Load Balancer",
        "explicacao": "O Application Load Balancer opera na camada 7 (HTTP/HTTPS) e permite roteamento avançado por caminho, cabeçalho e nome do host."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação de jogos precisa de balanceamento de tráfego TCP e UDP com latência ultrabaixa e capacidade de lidar com milhões de requisições por segundo. Qual tipo de balanceador de carga é o mais indicado?",
        "alternativas": ["Network Load Balancer", "Application Load Balancer", "Gateway Load Balancer", "Amazon CloudFront"],
        "correta": "Network Load Balancer",
        "explicacao": "O Network Load Balancer opera na camada 4 (TCP/UDP/TLS), oferecendo desempenho muito alto e baixa latência, além de IPs estáticos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer implantar e escalar appliances virtuais de terceiros, como firewalls e sistemas de detecção de intrusão, de forma transparente no caminho do tráfego. Qual tipo de balanceador de carga deve ser usado?",
        "alternativas": ["Gateway Load Balancer", "Application Load Balancer", "Network Load Balancer", "Amazon Route 53"],
        "correta": "Gateway Load Balancer",
        "explicacao": "O Gateway Load Balancer facilita a implantação, a escalabilidade e o gerenciamento de appliances virtuais de rede e segurança."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é a durabilidade para a qual o Amazon S3 foi projetado?",
        "alternativas": ["99,999999999% (11 noves)", "99,9% (3 noves)", "99,99% (4 noves)", "100% (garantia contratual)"],
        "correta": "99,999999999% (11 noves)",
        "explicacao": "O S3 foi projetado para 11 noves de durabilidade, armazenando os objetos de forma redundante em vários dispositivos e, na maioria das classes, em várias Zonas de Disponibilidade."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Que tipo de armazenamento o Amazon S3 oferece?",
        "alternativas": ["Armazenamento de objetos", "Armazenamento em bloco", "Sistema de arquivos compartilhado NFS", "Armazenamento em fita física"],
        "correta": "Armazenamento de objetos",
        "explicacao": "O S3 armazena dados como objetos dentro de buckets, cada um com uma chave, dados e metadados, com capacidade praticamente ilimitada."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é o tamanho máximo de um único objeto armazenado no Amazon S3?",
        "alternativas": ["5 TB", "5 GB", "100 MB", "Não há limite de tamanho por objeto"],
        "correta": "5 TB",
        "explicacao": "Um objeto do S3 pode ter até 5 TB. Para objetos maiores que 100 MB, recomenda-se o upload em várias partes (multipart upload)."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer mover automaticamente os objetos do S3 para classes mais baratas depois de 30 dias e excluí-los depois de um ano. Qual recurso deve ser configurado?",
        "alternativas": ["Políticas de ciclo de vida do S3", "S3 Transfer Acceleration", "Bloqueio de acesso público", "S3 Object Lock"],
        "correta": "Políticas de ciclo de vida do S3",
        "explicacao": "As regras de ciclo de vida automatizam a transição de objetos entre classes de armazenamento e a expiração (exclusão) após um período definido."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer manter automaticamente uma cópia dos objetos de um bucket em outra Região da AWS para recuperação de desastres. Qual recurso deve ser usado?",
        "alternativas": ["Replicação entre Regiões do S3 (S3 Cross-Region Replication)", "S3 Transfer Acceleration entre os pontos de presença", "Políticas de ciclo de vida com transição para outra Região", "Versionamento do S3 com cópia automática das versões"],
        "correta": "Replicação entre Regiões do S3 (S3 Cross-Region Replication)",
        "explicacao": "A replicação entre Regiões copia automaticamente novos objetos para um bucket em outra Região, ajudando em requisitos de conformidade, latência e recuperação de desastres."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer hospedar um site institucional composto apenas por HTML, CSS, imagens e JavaScript, sem servidores. Qual opção é a mais simples e econômica?",
        "alternativas": ["Hospedagem de site estático no Amazon S3, opcionalmente com o Amazon CloudFront", "Um cluster do Amazon EKS com vários nós em três Zonas de Disponibilidade diferentes", "Instâncias EC2 com Auto Scaling atrás de um Application Load Balancer em várias zonas", "Um banco de dados Amazon RDS"],
        "correta": "Hospedagem de site estático no Amazon S3, opcionalmente com o Amazon CloudFront",
        "explicacao": "O S3 pode servir sites estáticos diretamente. Usar o CloudFront na frente melhora a performance e permite HTTPS com domínio próprio."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Usuários de vários continentes enviam arquivos grandes para um bucket do S3 e reclamam da lentidão. Qual recurso pode acelerar esses uploads usando a rede de borda da AWS?",
        "alternativas": ["S3 Transfer Acceleration", "S3 Intelligent-Tiering", "S3 Object Lock", "Versionamento do S3"],
        "correta": "S3 Transfer Acceleration",
        "explicacao": "O S3 Transfer Acceleration direciona os uploads pelos pontos de presença do CloudFront e pela rede global da AWS, acelerando transferências de longa distância."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer armazenar cópias secundárias de dados que podem ser recriados facilmente, com acesso infrequente e o menor custo possível, aceitando que os dados fiquem em uma única Zona de Disponibilidade. Qual classe do S3 é a mais indicada?",
        "alternativas": ["S3 One Zone-IA", "S3 Standard", "S3 Standard-IA", "S3 Glacier Deep Archive"],
        "correta": "S3 One Zone-IA",
        "explicacao": "O S3 One Zone-IA armazena os dados em uma única Zona de Disponibilidade, custando menos que o Standard-IA, mas sem resistir à perda daquela zona."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson precisa arquivar imagens médicas acessadas cerca de uma vez por trimestre, mas que devem estar disponíveis em milissegundos quando solicitadas. Qual classe do S3 é a mais indicada?",
        "alternativas": ["S3 Glacier Instant Retrieval", "S3 Glacier Deep Archive", "S3 Glacier Flexible Retrieval", "S3 Standard"],
        "correta": "S3 Glacier Instant Retrieval",
        "explicacao": "O S3 Glacier Instant Retrieval oferece o menor custo para dados de longa duração raramente acessados que precisam de recuperação em milissegundos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson precisa arquivar backups acessados uma ou duas vezes por ano, aceitando recuperação em minutos ou horas e recuperações em massa gratuitas. Qual classe do S3 é a mais indicada?",
        "alternativas": ["S3 Glacier Flexible Retrieval", "S3 Glacier Instant Retrieval", "S3 Standard", "S3 Express One Zone"],
        "correta": "S3 Glacier Flexible Retrieval",
        "explicacao": "O S3 Glacier Flexible Retrieval é indicado para arquivamento com recuperação de minutos a horas, com opção de recuperação em massa sem custo."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Como funcionam os snapshots do Amazon EBS?",
        "alternativas": ["São backups incrementais do volume, armazenados de forma durável no Amazon S3", "São cópias completas, armazenadas no próprio volume, de todos os blocos de dados", "São cópias completas e temporárias, perdidas quando a instância é desligada ou encerrada", "São usados apenas para volumes de instance store, já que o EBS não oferece backups"],
        "correta": "São backups incrementais do volume, armazenados de forma durável no Amazon S3",
        "explicacao": "Os snapshots salvam apenas os blocos alterados desde o último snapshot. Podem ser usados para criar novos volumes, inclusive em outras Zonas de Disponibilidade e Regiões."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual tipo de volume Amazon EBS é a opção de SSD de uso geral, indicada para a maioria das cargas de trabalho, como volumes de inicialização e aplicações?",
        "alternativas": ["gp3 (SSD de uso geral)", "st1 (HDD otimizado para throughput)", "sc1 (HDD frio)", "Instance store"],
        "correta": "gp3 (SSD de uso geral)",
        "explicacao": "Os volumes gp3 equilibram preço e desempenho e permitem configurar IOPS e throughput independentemente do tamanho do volume."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um banco de dados crítico exige IOPS altas e consistentes com latência muito baixa. Qual tipo de volume Amazon EBS é o mais indicado?",
        "alternativas": ["io2 Block Express (SSD de IOPS provisionadas)", "sc1 (HDD frio)", "st1 (HDD otimizado para throughput)", "gp2 (SSD de uso geral) com o menor tamanho possível"],
        "correta": "io2 Block Express (SSD de IOPS provisionadas)",
        "explicacao": "Os volumes de IOPS provisionadas (io1 e io2) são indicados para bancos de dados críticos que precisam de desempenho de E/S alto e previsível."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "O que acontece com os dados armazenados no instance store de uma instância EC2 quando ela é interrompida (stopped)?",
        "alternativas": ["Os dados são perdidos", "Os dados são copiados automaticamente para o S3", "Os dados são mantidos indefinidamente", "Os dados são movidos para um volume EBS"],
        "correta": "Os dados são perdidos",
        "explicacao": "O instance store é armazenamento temporário em discos físicos do host. É ideal para cache e dados temporários, mas não para dados que precisam persistir."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson precisa de um sistema de arquivos compartilhado e totalmente gerenciado, compatível com o protocolo SMB e o Active Directory, para servidores Windows. Qual serviço deve ser usado?",
        "alternativas": ["Amazon FSx for Windows File Server", "Amazon Elastic File System (Amazon EFS)", "Amazon S3", "Amazon EBS"],
        "correta": "Amazon FSx for Windows File Server",
        "explicacao": "O Amazon FSx for Windows File Server oferece armazenamento de arquivos baseado em Windows Server, com SMB, NTFS e integração ao Active Directory."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson executa simulações de computação de alto desempenho (HPC) e precisa de um sistema de arquivos paralelo com throughput muito alto, integrado ao S3. Qual serviço deve ser usado?",
        "alternativas": ["Amazon FSx for Lustre", "Amazon FSx for Windows File Server", "Amazon S3 Glacier", "AWS Storage Gateway"],
        "correta": "Amazon FSx for Lustre",
        "explicacao": "O Amazon FSx for Lustre é um sistema de arquivos de alto desempenho para HPC, machine learning e processamento de mídia, que pode se integrar a buckets do S3."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer gerenciar e automatizar de forma centralizada os backups de EC2, EBS, RDS, DynamoDB e EFS, com políticas de retenção. Qual serviço deve ser usado?",
        "alternativas": ["AWS Backup", "AWS DataSync", "Amazon S3 Transfer Acceleration", "AWS Snowball Edge"],
        "correta": "AWS Backup",
        "explicacao": "O AWS Backup centraliza e automatiza a proteção de dados de diversos serviços da AWS e de cargas híbridas, com planos de backup e políticas de retenção."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer replicar continuamente seus servidores on-premises para a AWS para recuperá-los em minutos em caso de desastre, pagando pouco enquanto não há incidente. Qual serviço deve ser usado?",
        "alternativas": ["AWS Elastic Disaster Recovery", "AWS Backup Audit Manager", "Amazon S3 Glacier Deep Archive", "AWS Artifact"],
        "correta": "AWS Elastic Disaster Recovery",
        "explicacao": "O AWS Elastic Disaster Recovery replica servidores para uma área de preparação de baixo custo na AWS e permite iniciá-los rapidamente durante um desastre."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Quais são os tipos de gateway oferecidos pelo AWS Storage Gateway?",
        "alternativas": ["Gateway de arquivos, gateway de volumes e gateway de fitas", "Gateway de internet, gateway NAT e gateway de trânsito", "Gateway de API, gateway de pagamento e gateway de e-mail", "Gateway de DNS, gateway de CDN e gateway de VPN"],
        "correta": "Gateway de arquivos, gateway de volumes e gateway de fitas",
        "explicacao": "O gateway de arquivos usa NFS/SMB com dados no S3; o de volumes oferece volumes iSCSI com backup na nuvem; e o de fitas substitui bibliotecas de fitas físicas por fitas virtuais."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer substituir sua biblioteca de fitas físicas de backup por armazenamento na nuvem, sem mudar o software de backup existente. Qual opção atende a esse requisito?",
        "alternativas": ["Gateway de fitas do AWS Storage Gateway", "Amazon EFS", "Gateway de volumes do AWS Storage Gateway", "Amazon EBS"],
        "correta": "Gateway de fitas do AWS Storage Gateway",
        "explicacao": "O Tape Gateway apresenta uma biblioteca de fitas virtual ao software de backup e armazena as fitas no S3 e nas classes Glacier."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é a diferença entre o Multi-AZ e as réplicas de leitura do Amazon RDS?",
        "alternativas": ["O Multi-AZ oferece alta disponibilidade com failover automático; as réplicas de leitura aumentam a capacidade de leitura", "O Multi-AZ aumenta a capacidade de gravação; as réplicas de leitura fazem backup automático dos dados em outra Região a cada hora", "Os dois servem apenas para reduzir custos", "As réplicas de leitura só existem no DynamoDB, e o Multi-AZ só está disponível para clusters do Amazon Aurora Serverless v2 em produção"],
        "correta": "O Multi-AZ oferece alta disponibilidade com failover automático; as réplicas de leitura aumentam a capacidade de leitura",
        "explicacao": "No Multi-AZ, uma instância em espera em outra zona assume em caso de falha. As réplicas de leitura distribuem consultas de leitura e podem ficar em outras Regiões."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação tem uso de banco de dados relacional intermitente e imprevisível, e a empresa quer que a capacidade se ajuste automaticamente, sem gerenciar instâncias. Qual opção é a mais indicada?",
        "alternativas": ["Amazon Aurora Serverless", "Amazon RDS com instância fixa de grande porte", "Amazon Redshift", "Amazon ElastiCache"],
        "correta": "Amazon Aurora Serverless",
        "explicacao": "O Aurora Serverless ajusta automaticamente a capacidade do banco conforme a demanda, sendo indicado para cargas variáveis ou imprevisíveis."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação global precisa de uma tabela do DynamoDB replicada automaticamente em várias Regiões, com leitura e gravação locais em cada uma. Qual recurso deve ser usado?",
        "alternativas": ["Tabelas globais do DynamoDB", "Réplicas de leitura do RDS", "S3 Cross-Region Replication", "Amazon ElastiCache"],
        "correta": "Tabelas globais do DynamoDB",
        "explicacao": "As tabelas globais do DynamoDB oferecem replicação multirregião e multiativa, permitindo baixa latência local e resiliência a falhas de Região."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação que usa o DynamoDB precisa reduzir a latência de leitura de milissegundos para microssegundos, com um cache totalmente compatível com a API do DynamoDB. Qual recurso deve ser usado?",
        "alternativas": ["Amazon DynamoDB Accelerator (DAX)", "Amazon Redshift", "Amazon S3 Glacier", "Amazon CloudFront com cache de API"],
        "correta": "Amazon DynamoDB Accelerator (DAX)",
        "explicacao": "O DAX é um cache em memória gerenciado para o DynamoDB, que melhora o desempenho de leitura sem exigir grandes mudanças na aplicação."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson usa MongoDB e quer um banco de dados de documentos totalmente gerenciado e compatível com a API do MongoDB. Qual serviço deve ser escolhido?",
        "alternativas": ["Amazon DocumentDB", "Amazon Neptune", "Amazon Redshift", "Amazon Keyspaces"],
        "correta": "Amazon DocumentDB",
        "explicacao": "O Amazon DocumentDB (compatível com MongoDB) é um banco de documentos JSON gerenciado, escalável e altamente disponível."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma rede social precisa armazenar e consultar relacionamentos complexos entre usuários, como 'amigos de amigos', e um motor de recomendações. Qual banco de dados é o mais indicado?",
        "alternativas": ["Amazon Neptune", "Amazon RDS for MySQL", "Amazon Redshift", "Amazon S3"],
        "correta": "Amazon Neptune",
        "explicacao": "O Amazon Neptune é um banco de dados de grafos gerenciado, otimizado para armazenar e navegar por relacionamentos altamente conectados."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer migrar suas cargas de trabalho Apache Cassandra para um serviço gerenciado e serverless. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Keyspaces (for Apache Cassandra)", "Amazon DocumentDB (compatível com MongoDB)", "Amazon Neptune", "Amazon Aurora"],
        "correta": "Amazon Keyspaces (for Apache Cassandra)",
        "explicacao": "O Amazon Keyspaces é um serviço de banco de dados compatível com Apache Cassandra, serverless e totalmente gerenciado."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson coleta medições de sensores IoT a cada segundo e precisa armazenar e analisar esses dados ao longo do tempo. Qual banco de dados é otimizado para esse tipo de dado?",
        "alternativas": ["Amazon Timestream", "Amazon Neptune", "Amazon DocumentDB", "Amazon RDS for Oracle"],
        "correta": "Amazon Timestream",
        "explicacao": "O Amazon Timestream é um banco de dados de séries temporais gerenciado, indicado para dados de IoT, métricas operacionais e telemetria."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação precisa de um banco de dados em memória compatível com Redis que também ofereça durabilidade dos dados, podendo ser usado como banco principal. Qual serviço deve ser usado?",
        "alternativas": ["Amazon MemoryDB", "Amazon S3 Glacier", "Amazon Redshift", "Amazon Athena"],
        "correta": "Amazon MemoryDB",
        "explicacao": "O Amazon MemoryDB é um banco de dados em memória durável, compatível com Valkey e Redis OSS, com latência de microssegundos e armazenamento em log multi-AZ."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Em qual situação faz sentido instalar e gerenciar um banco de dados em uma instância EC2, em vez de usar o Amazon RDS?",
        "alternativas": ["Quando é necessário acesso total ao sistema operacional ou uma configuração que o RDS não suporta", "Quando se quer o menor esforço de administração possível, sem precisar cuidar de patches, backups ou réplicas", "Quando se quer que a AWS aplique automaticamente os patches do sistema operacional e do banco de dados", "Quando se precisa de backups automáticos sem nenhuma configuração e com restauração em qualquer ponto no tempo"],
        "correta": "Quando é necessário acesso total ao sistema operacional ou uma configuração que o RDS não suporta",
        "explicacao": "Bancos autogerenciados no EC2 dão controle total, mas o cliente assume tarefas como patches, backups e alta disponibilidade, que o RDS automatiza."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é a diferença entre uma sub-rede pública e uma sub-rede privada em uma VPC?",
        "alternativas": ["A sub-rede pública tem rota para um internet gateway; a privada não tem rota direta para a internet", "A sub-rede pública é gratuita e a privada é cobrada por hora, conforme o número de instâncias executadas nela", "A sub-rede privada fica fora da VPC, em um data center separado que a AWS reserva para cada cliente", "Não há diferença entre elas, pois todas as sub-redes de uma VPC têm acesso direto à internet por padrão"],
        "correta": "A sub-rede pública tem rota para um internet gateway; a privada não tem rota direta para a internet",
        "explicacao": "A tabela de rotas define se a sub-rede é pública. Recursos como bancos de dados costumam ficar em sub-redes privadas, protegidos do acesso direto pela internet."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual componente permite que recursos de uma VPC se comuniquem com a internet nos dois sentidos?",
        "alternativas": ["Internet gateway", "NAT gateway", "Endpoint da VPC", "Virtual private gateway"],
        "correta": "Internet gateway",
        "explicacao": "O internet gateway é um componente escalável e redundante anexado à VPC, que permite a comunicação entre a VPC e a internet para recursos com IP público."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual componente da VPC determina para onde o tráfego de rede de uma sub-rede é direcionado?",
        "alternativas": ["Tabela de rotas", "Security group", "Network ACL", "Endpoint da VPC"],
        "correta": "Tabela de rotas",
        "explicacao": "A tabela de rotas contém regras que definem o destino do tráfego, como enviar 0.0.0.0/0 para um internet gateway ou para um NAT gateway."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer conectar duas VPCs para que se comuniquem usando endereços IP privados, como se estivessem na mesma rede. Qual recurso é o mais simples para isso?",
        "alternativas": ["Emparelhamento de VPC (VPC peering)", "Internet gateway em cada VPC com IPs públicos", "Amazon CloudFront", "AWS Direct Connect"],
        "correta": "Emparelhamento de VPC (VPC peering)",
        "explicacao": "O VPC peering conecta duas VPCs de forma privada, inclusive entre contas e Regiões. Ele não é transitivo: cada par de VPCs precisa de sua própria conexão."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson tem dezenas de VPCs e várias conexões on-premises e quer interligá-las por meio de um hub central, evitando uma malha de conexões ponto a ponto. Qual serviço deve ser usado?",
        "alternativas": ["AWS Transit Gateway", "VPC peering entre todas as VPCs", "Internet gateway", "Amazon Route 53"],
        "correta": "AWS Transit Gateway",
        "explicacao": "O AWS Transit Gateway funciona como um roteador central que conecta VPCs e redes on-premises, simplificando a topologia de rede."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer oferecer um serviço da sua VPC para clientes em outras contas, de forma privada, sem expor o tráfego à internet nem fazer peering de VPCs. Qual tecnologia deve ser usada?",
        "alternativas": ["AWS PrivateLink", "Internet gateway", "Amazon CloudFront", "Elastic IP"],
        "correta": "AWS PrivateLink",
        "explicacao": "O AWS PrivateLink oferece conectividade privada entre VPCs, serviços da AWS e redes on-premises, usando endpoints de interface, sem expor o tráfego à internet."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação precisa de um endereço IPv4 público fixo que possa ser movido rapidamente para outra instância em caso de falha. Qual recurso deve ser usado?",
        "alternativas": ["Endereço IP elástico (Elastic IP)", "Endereço IP privado secundário", "Um nome de DNS privado do Route 53", "Uma tabela de rotas"],
        "correta": "Endereço IP elástico (Elastic IP)",
        "explicacao": "Um Elastic IP é um IPv4 público estático associado à conta, que pode ser remapeado entre instâncias. A AWS cobra por todos os endereços IPv4 públicos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer que o Amazon Route 53 direcione cada usuário para a Região da AWS que oferece a menor latência para ele. Qual política de roteamento deve ser usada?",
        "alternativas": ["Roteamento baseado em latência", "Roteamento por geolocalização", "Roteamento ponderado", "Roteamento de failover"],
        "correta": "Roteamento baseado em latência",
        "explicacao": "O roteamento baseado em latência responde às consultas DNS com o recurso da Região que oferece a menor latência para o usuário."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer que o Amazon Route 53 direcione o tráfego para um site de recuperação somente quando o site principal não passar nas verificações de saúde. Qual política de roteamento deve ser usada?",
        "alternativas": ["Roteamento de failover", "Roteamento ponderado", "Roteamento por geolocalização", "Roteamento simples"],
        "correta": "Roteamento de failover",
        "explicacao": "O roteamento de failover usa verificações de saúde para enviar o tráfego ao recurso secundário quando o primário fica indisponível."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma equipe quer testar uma nova versão da aplicação enviando 10% do tráfego para ela e 90% para a versão atual, usando o DNS. Qual política de roteamento do Route 53 deve ser usada?",
        "alternativas": ["Roteamento ponderado", "Roteamento de failover", "Roteamento baseado em latência", "Roteamento simples"],
        "correta": "Roteamento ponderado",
        "explicacao": "O roteamento ponderado distribui o tráfego entre vários recursos de acordo com pesos definidos, útil para testes e implantações graduais."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Por questões de licenciamento de conteúdo, uma empresa precisa direcionar usuários de cada país para versões diferentes do seu site. Qual política de roteamento do Route 53 deve ser usada?",
        "alternativas": ["Roteamento por geolocalização", "Roteamento ponderado", "Roteamento baseado em latência", "Roteamento simples"],
        "correta": "Roteamento por geolocalização",
        "explicacao": "O roteamento por geolocalização responde conforme a localização geográfica de origem da consulta DNS, como continente, país ou estado."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação global precisa de dois endereços IP estáticos (anycast) que direcionem os usuários pela rede da AWS até o endpoint saudável mais próximo, melhorando a performance de tráfego TCP e UDP. Qual serviço deve ser usado?",
        "alternativas": ["AWS Global Accelerator", "Amazon CloudFront", "Amazon Route 53 com roteamento simples", "AWS Direct Connect"],
        "correta": "AWS Global Accelerator",
        "explicacao": "O AWS Global Accelerator fornece IPs estáticos anycast e roteia o tráfego pela rede global da AWS, com failover rápido entre endpoints em diferentes Regiões."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer criar, publicar e proteger APIs REST e WebSocket que acionam funções Lambda, com controle de limites de requisições. Qual serviço deve ser usado?",
        "alternativas": ["Amazon API Gateway", "Amazon CloudFront", "Elastic Load Balancing", "AWS Direct Connect"],
        "correta": "Amazon API Gateway",
        "explicacao": "O Amazon API Gateway é um serviço gerenciado para criar, publicar, monitorar e proteger APIs em qualquer escala, com autenticação, limitação de taxa e cache."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Funcionários remotos precisam acessar com segurança recursos de uma VPC a partir de seus notebooks, usando um cliente VPN. Qual serviço deve ser usado?",
        "alternativas": ["AWS Client VPN", "AWS Site-to-Site VPN", "AWS Direct Connect", "Amazon CloudFront"],
        "correta": "AWS Client VPN",
        "explicacao": "O AWS Client VPN é um serviço gerenciado de VPN para usuários individuais. O Site-to-Site VPN conecta redes inteiras, como um escritório, à VPC."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer processar grandes volumes de dados com frameworks como Apache Spark e Hadoop em clusters gerenciados. Qual serviço deve ser usado?",
        "alternativas": ["Amazon EMR", "Amazon RDS", "Amazon Lightsail", "Amazon Polly"],
        "correta": "Amazon EMR",
        "explicacao": "O Amazon EMR é uma plataforma gerenciada de big data para executar Apache Spark, Hadoop, Hive e outros frameworks em grande escala."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer preparar e transformar dados para análise (ETL) com um serviço serverless, além de manter um catálogo central de metadados dos seus dados. Qual serviço deve ser usado?",
        "alternativas": ["AWS Glue", "Amazon EMR com instâncias fixas", "Amazon Lightsail", "AWS Batch"],
        "correta": "AWS Glue",
        "explicacao": "O AWS Glue é um serviço de integração de dados serverless que descobre, prepara e transforma dados e mantém o AWS Glue Data Catalog."
    },
]

QUESTOES += [
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson precisa coletar e processar em tempo real milhões de eventos por segundo, como cliques em um site, com várias aplicações consumindo os mesmos dados. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Kinesis Data Streams", "Amazon Simple Queue Service (Amazon SQS)", "Amazon RDS", "AWS Batch"],
        "correta": "Amazon Kinesis Data Streams",
        "explicacao": "O Amazon Kinesis Data Streams captura e armazena fluxos de dados em tempo real, permitindo que várias aplicações consumam e processem os eventos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer carregar automaticamente fluxos de dados de streaming no Amazon S3 e no Amazon Redshift, sem escrever aplicações consumidoras nem gerenciar servidores. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Data Firehose", "Amazon Kinesis Video Streams", "Amazon SQS", "AWS DataSync"],
        "correta": "Amazon Data Firehose",
        "explicacao": "O Amazon Data Firehose (antes Kinesis Data Firehose) captura, transforma e entrega dados de streaming em destinos como S3, Redshift e OpenSearch."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A diretoria quer painéis interativos de business intelligence com os indicadores de vendas, acessíveis pelo navegador. Qual serviço da AWS deve ser usado?",
        "alternativas": ["Amazon QuickSight", "Amazon Athena", "AWS Glue", "Amazon EMR"],
        "correta": "Amazon QuickSight",
        "explicacao": "O Amazon QuickSight é um serviço de business intelligence serverless para criar painéis e visualizações interativas a partir de diversas fontes de dados."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer pesquisar e analisar logs de aplicações em tempo quase real, com busca de texto completo e painéis de visualização. Qual serviço é o mais indicado?",
        "alternativas": ["Amazon OpenSearch Service", "Amazon Redshift Serverless", "Amazon Neptune", "AWS Glue"],
        "correta": "Amazon OpenSearch Service",
        "explicacao": "O Amazon OpenSearch Service facilita a implantação de clusters OpenSearch para busca, análise de logs, monitoramento e observabilidade."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer construir um data lake no S3 e gerenciar de forma centralizada as permissões detalhadas de acesso aos dados, por banco, tabela e coluna. Qual serviço deve ser usado?",
        "alternativas": ["AWS Lake Formation", "Amazon EFS", "AWS Backup", "Amazon Lightsail"],
        "correta": "AWS Lake Formation",
        "explicacao": "O AWS Lake Formation simplifica a criação de data lakes seguros e centraliza a governança e as permissões de acesso aos dados catalogados."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson usa Apache Kafka on-premises e quer migrar para um serviço gerenciado e totalmente compatível na AWS. Qual serviço deve ser escolhido?",
        "alternativas": ["Amazon Managed Streaming for Apache Kafka (Amazon MSK)", "Amazon Simple Queue Service (Amazon SQS)", "Amazon Kinesis Data Streams", "Amazon MQ (para Apache ActiveMQ e RabbitMQ)"],
        "correta": "Amazon Managed Streaming for Apache Kafka (Amazon MSK)",
        "explicacao": "O Amazon MSK executa clusters Apache Kafka totalmente gerenciados, compatíveis com as aplicações e ferramentas Kafka existentes."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer reagir automaticamente a eventos de serviços da AWS, de aplicações SaaS e de suas próprias aplicações, roteando-os para alvos como funções Lambda. Qual serviço deve ser usado?",
        "alternativas": ["Amazon EventBridge", "Amazon CloudFront", "AWS Direct Connect", "Amazon Redshift"],
        "correta": "Amazon EventBridge",
        "explicacao": "O Amazon EventBridge é um barramento de eventos serverless que conecta aplicações por meio de eventos, com regras de filtragem e roteamento para diversos alvos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer executar uma função Lambda automaticamente todos os dias às 2h da manhã. Qual serviço permite agendar essa execução?",
        "alternativas": ["Amazon EventBridge Scheduler", "Amazon SQS", "AWS Direct Connect", "Amazon CloudWatch Logs Insights"],
        "correta": "Amazon EventBridge Scheduler",
        "explicacao": "O EventBridge Scheduler e as regras agendadas do EventBridge permitem acionar alvos, como funções Lambda, em horários definidos ou em intervalos regulares."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer coordenar várias funções Lambda em um fluxo de trabalho visual com etapas, tratamento de erros, novas tentativas e aprovações. Qual serviço deve ser usado?",
        "alternativas": ["AWS Step Functions", "Amazon SNS", "Amazon CloudWatch", "AWS Batch"],
        "correta": "AWS Step Functions",
        "explicacao": "O AWS Step Functions orquestra serviços em fluxos de trabalho visuais (máquinas de estado), com controle de erros, novas tentativas e execução paralela."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma loja virtual precisa enviar e-mails transacionais, como confirmações de pedido, em grande volume e com boa entregabilidade. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Simple Email Service (Amazon SES)", "Amazon Simple Notification Service (Amazon SNS)", "Amazon Connect", "AWS Direct Connect"],
        "correta": "Amazon Simple Email Service (Amazon SES)",
        "explicacao": "O Amazon SES é um serviço de envio de e-mails escalável para mensagens transacionais e de marketing, com ferramentas para melhorar a entregabilidade."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson usa Apache ActiveMQ on-premises e quer migrar suas filas para a AWS sem reescrever o código das aplicações. Qual serviço é o mais indicado?",
        "alternativas": ["Amazon MQ", "Amazon SQS", "Amazon Kinesis Data Streams", "Amazon SES"],
        "correta": "Amazon MQ",
        "explicacao": "O Amazon MQ é um serviço gerenciado de message broker para Apache ActiveMQ e RabbitMQ, compatível com protocolos e APIs padrão do mercado."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação de pedidos precisa que as mensagens de uma fila sejam processadas exatamente na ordem em que foram enviadas e sem duplicação. Que tipo de fila do Amazon SQS deve ser usado?",
        "alternativas": ["Fila FIFO", "Fila padrão", "Tópico do SNS", "Fluxo do Kinesis Video Streams"],
        "correta": "Fila FIFO",
        "explicacao": "As filas FIFO do SQS garantem ordenação e processamento exatamente uma vez. As filas padrão oferecem throughput quase ilimitado, com ordenação de melhor esforço."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um evento de novo pedido precisa ser entregue simultaneamente a várias filas do SQS, cada uma processada por um sistema diferente. Qual padrão de arquitetura deve ser usado?",
        "alternativas": ["Fan-out com um tópico do Amazon SNS assinado pelas filas do SQS", "Uma única fila FIFO compartilhada, consumida por todos os sistemas ao mesmo tempo", "Polling direto no banco de dados por todos os sistemas a cada segundo", "Cópia manual das mensagens de uma fila para as outras por um operador"],
        "correta": "Fan-out com um tópico do Amazon SNS assinado pelas filas do SQS",
        "explicacao": "No padrão fan-out, uma mensagem publicada em um tópico do SNS é entregue a todas as filas assinantes, que a processam de forma independente."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma equipe quer um serviço gerenciado que compile o código-fonte, execute os testes e gere pacotes prontos para implantação, cobrando apenas pelos minutos de build. Qual serviço deve ser usado?",
        "alternativas": ["AWS CodeBuild", "AWS CodeDeploy", "Amazon CloudWatch", "AWS Artifact"],
        "correta": "AWS CodeBuild",
        "explicacao": "O AWS CodeBuild é um serviço de integração contínua totalmente gerenciado que compila código, executa testes e produz artefatos, sem servidores de build para manter."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer automatizar a implantação de novas versões da aplicação em instâncias EC2, servidores on-premises e funções Lambda, com reversão automática em caso de falha. Qual serviço deve ser usado?",
        "alternativas": ["AWS CodeDeploy", "AWS CodeBuild", "AWS CodeArtifact", "Amazon Inspector"],
        "correta": "AWS CodeDeploy",
        "explicacao": "O AWS CodeDeploy automatiza implantações em EC2, ECS, Lambda e servidores on-premises, com estratégias como implantação gradual e azul/verde."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma equipe quer modelar e automatizar todo o fluxo de entrega de software, da alteração no repositório até a produção, passando por build, testes e implantação. Qual serviço deve ser usado?",
        "alternativas": ["AWS CodePipeline", "AWS CodeArtifact", "Amazon CloudWatch", "AWS X-Ray"],
        "correta": "AWS CodePipeline",
        "explicacao": "O AWS CodePipeline é um serviço de entrega contínua que orquestra as etapas de liberação de software, integrando-se a serviços como CodeBuild e CodeDeploy."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer um repositório gerenciado para armazenar e compartilhar pacotes de software, como bibliotecas npm, Maven e PyPI, usados no desenvolvimento. Qual serviço deve ser usado?",
        "alternativas": ["AWS CodeArtifact", "Amazon ECR", "Amazon S3 Glacier", "AWS CodePipeline"],
        "correta": "AWS CodeArtifact",
        "explicacao": "O AWS CodeArtifact é um repositório de artefatos gerenciado, compatível com gerenciadores de pacotes populares como npm, pip, Maven e NuGet."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação de microsserviços está lenta e a equipe precisa rastrear as requisições de ponta a ponta para identificar qual serviço causa o gargalo. Qual serviço deve ser usado?",
        "alternativas": ["AWS X-Ray", "AWS CloudTrail", "AWS Config", "AWS Artifact"],
        "correta": "AWS X-Ray",
        "explicacao": "O AWS X-Ray faz rastreamento distribuído, mostrando o caminho e o tempo de cada requisição entre os serviços, o que ajuda a encontrar gargalos e erros."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um administrador precisa executar o mesmo comando ou script em centenas de instâncias EC2 ao mesmo tempo, sem acessar cada uma por SSH. Qual recurso deve ser usado?",
        "alternativas": ["AWS Systems Manager Run Command", "Amazon CloudFront", "AWS CodeArtifact", "AWS Systems Manager Parameter Store"],
        "correta": "AWS Systems Manager Run Command",
        "explicacao": "O Run Command executa comandos e scripts remotamente em frotas de instâncias gerenciadas, com controle de acesso pelo IAM e registro dos resultados."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer ser avisada sobre manutenções programadas e problemas nos serviços da AWS que afetem especificamente os recursos da sua conta. Qual recurso deve consultar?",
        "alternativas": ["AWS Health Dashboard", "AWS Pricing Calculator", "AWS Marketplace", "AWS Artifact"],
        "correta": "AWS Health Dashboard",
        "explicacao": "O AWS Health Dashboard mostra o status geral dos serviços e eventos personalizados que afetam a conta, com orientações e notificações sobre o impacto."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer controlar o uso de licenças de software, como Microsoft e Oracle, em instâncias EC2 e servidores on-premises, evitando exceder os limites contratados. Qual serviço deve ser usado?",
        "alternativas": ["AWS License Manager", "AWS Artifact", "AWS Trusted Advisor", "Amazon Macie"],
        "correta": "AWS License Manager",
        "explicacao": "O AWS License Manager ajuda a gerenciar licenças de software de fornecedores, definindo regras de uso e alertando sobre possíveis violações."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson sem equipe de operações quer que a AWS opere a infraestrutura em seu nome, cuidando de monitoramento, patches, backups e gerenciamento de incidentes. Qual serviço atende a essa necessidade?",
        "alternativas": ["AWS Managed Services (AMS)", "AWS Artifact", "AWS Pricing Calculator", "Amazon Lightsail"],
        "correta": "AWS Managed Services (AMS)",
        "explicacao": "O AWS Managed Services oferece operação contínua da infraestrutura AWS pela própria AWS, seguindo boas práticas de segurança e operação."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer analisar avaliações de clientes para identificar automaticamente o sentimento (positivo ou negativo) e as entidades mencionadas no texto. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Comprehend", "Amazon Polly", "Amazon Rekognition", "Amazon Transcribe"],
        "correta": "Amazon Comprehend",
        "explicacao": "O Amazon Comprehend é um serviço de processamento de linguagem natural que extrai sentimentos, entidades, frases-chave e tópicos de textos."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer criar um chatbot de voz e texto para atendimento automatizado, com reconhecimento de intenção do usuário. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Lex", "Amazon Polly", "Amazon Textract", "Amazon Kendra"],
        "correta": "Amazon Lex",
        "explicacao": "O Amazon Lex permite criar interfaces conversacionais com reconhecimento de fala e compreensão de linguagem natural, a mesma tecnologia usada pela Alexa."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma central de atendimento quer converter automaticamente as gravações das ligações em texto para análise. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Transcribe", "Amazon Polly", "Amazon Translate", "Amazon Rekognition"],
        "correta": "Amazon Transcribe",
        "explicacao": "O Amazon Transcribe converte fala em texto automaticamente e oferece recursos como identificação de quem está falando e vocabulário personalizado."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma loja virtual quer traduzir automaticamente as descrições dos seus produtos do português para inglês e espanhol. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Translate", "Amazon Transcribe", "Amazon Comprehend", "Amazon Lex"],
        "correta": "Amazon Translate",
        "explicacao": "O Amazon Translate é um serviço de tradução automática neural que oferece traduções rápidas e de alta qualidade entre diversos idiomas."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson recebe milhares de notas fiscais e formulários digitalizados e quer extrair automaticamente textos, tabelas e campos desses documentos. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Textract", "Amazon Polly", "Amazon Rekognition Video", "Amazon Translate"],
        "correta": "Amazon Textract",
        "explicacao": "O Amazon Textract extrai automaticamente texto impresso e manuscrito, tabelas e dados de formulários de documentos digitalizados, indo além do OCR simples."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer oferecer aos funcionários um mecanismo de busca inteligente que encontre respostas em documentos internos armazenados em várias fontes. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Kendra", "Amazon Athena", "Amazon Route 53", "Amazon Polly"],
        "correta": "Amazon Kendra",
        "explicacao": "O Amazon Kendra é um serviço de busca corporativa com machine learning, que entende perguntas em linguagem natural e encontra respostas em diversas fontes de conteúdo."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma loja virtual quer recomendar produtos personalizados a cada cliente, usando a mesma tecnologia de machine learning da Amazon.com, sem experiência prévia em ML. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Personalize", "Amazon Comprehend", "Amazon Textract", "Amazon Lex"],
        "correta": "Amazon Personalize",
        "explicacao": "O Amazon Personalize cria modelos de recomendação personalizados em tempo real a partir dos dados de interação dos usuários."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer criar aplicações de IA generativa usando modelos de base (foundation models) de diferentes fornecedores, acessados por uma única API e sem gerenciar infraestrutura. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Bedrock", "Amazon Polly", "Amazon Redshift", "AWS Glue"],
        "correta": "Amazon Bedrock",
        "explicacao": "O Amazon Bedrock oferece acesso a modelos de base de empresas como Anthropic, Meta, Mistral e Amazon por uma API única, com recursos para personalização e segurança."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Desenvolvedores querem um assistente de IA generativa que sugira código, explique trechos e ajude a resolver problemas na AWS diretamente na IDE e no console. Qual serviço atende a essa necessidade?",
        "alternativas": ["Amazon Q Developer", "Amazon Polly", "Amazon Inspector", "AWS CodeArtifact"],
        "correta": "Amazon Q Developer",
        "explicacao": "O Amazon Q Developer é um assistente de IA generativa para desenvolvimento de software e operações na AWS, disponível em IDEs, no console e na linha de comando."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer fornecer desktops virtuais Windows ou Linux gerenciados para funcionários em home office, acessíveis de qualquer dispositivo. Qual serviço deve ser usado?",
        "alternativas": ["Amazon WorkSpaces", "Amazon Lightsail", "AWS Outposts", "Amazon EC2 Auto Scaling"],
        "correta": "Amazon WorkSpaces",
        "explicacao": "O Amazon WorkSpaces é um serviço gerenciado de desktops virtuais (DaaS) que permite provisionar desktops na nuvem para os usuários."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson, que trabalha com engenharia, quer transmitir aplicações desktop pesadas, como softwares de CAD, para o navegador dos usuários, sem instalar nada nos computadores deles. Qual serviço deve ser usado?",
        "alternativas": ["Amazon AppStream 2.0", "Amazon WorkSpaces", "Amazon CloudFront", "AWS Amplify"],
        "correta": "Amazon AppStream 2.0",
        "explicacao": "O Amazon AppStream 2.0 transmite aplicações desktop da AWS para o navegador, sem precisar entregar um desktop completo ao usuário."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Desenvolvedores front-end querem criar, implantar e hospedar rapidamente aplicações web e móveis full-stack, com autenticação e back-end integrados. Qual serviço é o mais indicado?",
        "alternativas": ["AWS Amplify", "Amazon EMR", "AWS Outposts", "AWS Direct Connect"],
        "correta": "AWS Amplify",
        "explicacao": "O AWS Amplify oferece ferramentas e hospedagem para criar e implantar aplicações web e móveis full-stack, integradas a serviços da AWS."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação móvel precisa de uma API GraphQL gerenciada, com atualizações de dados em tempo real para os usuários conectados. Qual serviço deve ser usado?",
        "alternativas": ["AWS AppSync", "Amazon SQS", "AWS Direct Connect", "Amazon Route 53"],
        "correta": "AWS AppSync",
        "explicacao": "O AWS AppSync é um serviço gerenciado de APIs GraphQL e Pub/Sub, com suporte a atualizações em tempo real e acesso a várias fontes de dados."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer testar seu aplicativo móvel em centenas de celulares e tablets reais na nuvem, sem comprar os aparelhos. Qual serviço deve ser usado?",
        "alternativas": ["AWS Device Farm", "Amazon WorkSpaces", "AWS Amplify Hosting", "Amazon AppStream 2.0"],
        "correta": "AWS Device Farm",
        "explicacao": "O AWS Device Farm permite testar aplicativos web e móveis em dispositivos físicos reais hospedados pela AWS."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma fábrica quer conectar milhares de sensores à nuvem de forma segura para coletar e processar seus dados. Qual serviço deve ser usado?",
        "alternativas": ["AWS IoT Core", "Amazon Connect", "Amazon WorkSpaces", "AWS Batch"],
        "correta": "AWS IoT Core",
        "explicacao": "O AWS IoT Core conecta dispositivos IoT à nuvem com segurança, usando protocolos como MQTT, e roteia as mensagens para outros serviços da AWS."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer executar funções Lambda e modelos de machine learning localmente em dispositivos IoT, mesmo quando eles estão sem conexão com a internet. Qual serviço deve ser usado?",
        "alternativas": ["AWS IoT Greengrass", "AWS IoT Core apenas", "Amazon Kinesis Data Streams", "AWS Outposts"],
        "correta": "AWS IoT Greengrass",
        "explicacao": "O AWS IoT Greengrass leva recursos de computação, mensagens e ML para dispositivos de borda, permitindo que operem localmente e sincronizem com a nuvem."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer montar uma central de atendimento omnicanal na nuvem, com telefonia, chat e roteamento inteligente de clientes, pagando apenas pelo uso. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Connect", "Amazon SES", "Amazon SNS", "Amazon Lex sozinho"],
        "correta": "Amazon Connect",
        "explicacao": "O Amazon Connect é uma central de contato na nuvem, que pode ser configurada em minutos e se integra a recursos de IA, como Amazon Lex e Contact Lens."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson, que produz efeitos visuais em uma grande cidade, precisa de latência de milissegundos de um dígito para usuários dessa região metropolitana, longe da Região da AWS mais próxima. Qual opção de infraestrutura atende a esse requisito?",
        "alternativas": ["AWS Local Zones", "Pontos de presença do CloudFront", "AWS Snowball Edge", "Uma Região em outro continente"],
        "correta": "AWS Local Zones",
        "explicacao": "As AWS Local Zones colocam computação, armazenamento e banco de dados perto de grandes centros populacionais, oferecendo latência muito baixa para aplicações locais."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer executar aplicações com latência ultrabaixa para dispositivos móveis conectados a redes 5G, dentro da infraestrutura das operadoras de telecomunicações. Qual opção da AWS atende a esse requisito?",
        "alternativas": ["AWS Wavelength Zones", "AWS Local Zones", "AWS Outposts", "AWS Direct Connect"],
        "correta": "AWS Wavelength Zones",
        "explicacao": "As AWS Wavelength Zones incorporam computação e armazenamento da AWS nas redes 5G das operadoras, reduzindo a latência para dispositivos móveis."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma equipe de pesquisa em um navio, sem conexão estável com a internet, precisa coletar e processar dados localmente e depois enviá-los à AWS. Qual serviço é o mais indicado?",
        "alternativas": ["AWS Snowball Edge com capacidade de computação", "AWS Direct Connect com link dedicado no porto", "Amazon CloudFront", "AWS Site-to-Site VPN via conexão por satélite"],
        "correta": "AWS Snowball Edge com capacidade de computação",
        "explicacao": "O Snowball Edge pode executar instâncias EC2 e funções localmente em ambientes desconectados ou remotos e, depois, ser enviado à AWS para importar os dados."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é a base de hardware e software das instâncias EC2 modernas, que transfere funções de virtualização, rede e armazenamento para componentes dedicados, melhorando desempenho e segurança?",
        "alternativas": ["AWS Nitro System", "AWS Outposts", "AWS Snowball Edge", "AWS Wavelength"],
        "correta": "AWS Nitro System",
        "explicacao": "O AWS Nitro System combina hardware dedicado e um hipervisor leve, oferecendo quase todo o poder do servidor para as instâncias e isolamento reforçado."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer reduzir custos e melhorar a relação preço-desempenho das instâncias EC2 usando processadores projetados pela própria AWS com arquitetura Arm. Qual opção deve ser escolhida?",
        "alternativas": ["Instâncias baseadas em AWS Graviton", "Instâncias Dedicated Hosts com x86", "AWS Outposts", "Amazon Lightsail com Windows"],
        "correta": "Instâncias baseadas em AWS Graviton",
        "explicacao": "Os processadores AWS Graviton oferecem melhor relação preço-desempenho para muitas cargas e consomem menos energia, também contribuindo para a sustentabilidade."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma loja sabe que o tráfego aumenta todos os dias às 18h e quer adicionar instâncias automaticamente pouco antes desse horário. Qual tipo de ajuste do Amazon EC2 Auto Scaling é o mais adequado?",
        "alternativas": ["Escalabilidade programada (scheduled scaling)", "Escalabilidade manual", "Escalabilidade vertical", "Nenhum: o Auto Scaling não permite agendamento"],
        "correta": "Escalabilidade programada (scheduled scaling)",
        "explicacao": "A escalabilidade programada ajusta a capacidade em horários definidos. Também há escalabilidade dinâmica, baseada em métricas, e preditiva, baseada em machine learning."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer que o Amazon EC2 Auto Scaling mantenha a utilização média de CPU do grupo em torno de 50%, adicionando ou removendo instâncias automaticamente. Que tipo de política deve ser usada?",
        "alternativas": ["Política de rastreamento de destino (target tracking)", "Política de ciclo de vida do S3", "Política de senhas do IAM", "Política de controle de serviço (SCP) do AWS Organizations"],
        "correta": "Política de rastreamento de destino (target tracking)",
        "explicacao": "Com o rastreamento de destino, define-se um valor-alvo para uma métrica e o Auto Scaling ajusta a capacidade para mantê-la próxima desse valor."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer automatizar a criação, os testes e a atualização de imagens de servidor (AMIs) seguras e padronizadas. Qual serviço deve ser usado?",
        "alternativas": ["EC2 Image Builder", "AWS CodeArtifact", "Amazon ECR", "AWS Artifact"],
        "correta": "EC2 Image Builder",
        "explicacao": "O EC2 Image Builder automatiza pipelines para criar, testar e distribuir imagens de máquinas virtuais e de contêineres atualizadas e seguras."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma equipe quer reunir em uma só tela os gráficos de métricas de vários serviços, como CPU das instâncias, erros do balanceador e latência do banco. Qual recurso deve ser usado?",
        "alternativas": ["Painéis (dashboards) do Amazon CloudWatch", "AWS Artifact", "Relatórios do AWS Cost Explorer por serviço", "Políticas de ciclo de vida do S3"],
        "correta": "Painéis (dashboards) do Amazon CloudWatch",
        "explicacao": "Os painéis do CloudWatch são páginas personalizáveis que mostram métricas e alarmes de vários recursos, inclusive de diferentes Regiões e contas."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Um alarme do Amazon CloudWatch pode executar qual destas ações automaticamente quando uma métrica ultrapassa o limite definido?",
        "alternativas": ["Enviar uma notificação pelo Amazon SNS ou acionar uma ação do EC2 Auto Scaling", "Excluir automaticamente a conta da AWS para evitar novas cobranças", "Alterar automaticamente o plano de suporte para Enterprise durante o incidente", "Gerar uma fatura extra com o custo excedente e enviá-la ao responsável pela conta"],
        "correta": "Enviar uma notificação pelo Amazon SNS ou acionar uma ação do EC2 Auto Scaling",
        "explicacao": "Os alarmes do CloudWatch podem notificar via SNS, ajustar grupos do Auto Scaling, executar ações no EC2 (como reiniciar) ou criar itens no Systems Manager."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer implantar o mesmo template do AWS CloudFormation em várias contas e Regiões de uma só vez. Qual recurso deve ser usado?",
        "alternativas": ["AWS CloudFormation StackSets", "AWS Artifact", "Amazon CloudWatch Logs", "AWS Budgets"],
        "correta": "AWS CloudFormation StackSets",
        "explicacao": "O CloudFormation StackSets permite criar, atualizar e excluir pilhas em várias contas e Regiões com uma única operação."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual afirmação sobre o custo do AWS CloudFormation está correta?",
        "alternativas": ["Não há cobrança adicional pelo CloudFormation ao gerenciar recursos da AWS; paga-se pelos recursos criados", "Cada template custa um valor fixo por linha", "O CloudFormation é cobrado por usuário do IAM que cria ou atualiza pilhas na conta, com um valor fixo mensal por usuário", "O CloudFormation só pode ser usado por clientes com o plano de suporte Enterprise, que inclui o custo do serviço"],
        "correta": "Não há cobrança adicional pelo CloudFormation ao gerenciar recursos da AWS; paga-se pelos recursos criados",
        "explicacao": "O CloudFormation não cobra pelo gerenciamento de recursos da AWS. O cliente paga pelos recursos provisionados, como instâncias EC2 e buckets S3."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual afirmação sobre o AWS Elastic Beanstalk está correta?",
        "alternativas": ["Não há custo adicional pelo Beanstalk; paga-se pelos recursos que ele cria, e o cliente mantém acesso a eles", "O Beanstalk é cobrado por linha de código implantada, além do custo das instâncias EC2 e dos balanceadores que ele cria", "O Beanstalk cobra uma taxa por ambiente e impede que o cliente acesse ou altere as instâncias EC2 criadas por ele", "O Beanstalk só suporta aplicações em Java"],
        "correta": "Não há custo adicional pelo Beanstalk; paga-se pelos recursos que ele cria, e o cliente mantém acesso a eles",
        "explicacao": "O Elastic Beanstalk provisiona recursos como EC2, balanceadores e Auto Scaling para aplicações em várias linguagens, sem cobrar pelo serviço em si."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é a função de um ponto de presença (edge location) no Amazon Route 53?",
        "alternativas": ["Responder às consultas DNS próximo aos usuários, reduzindo a latência", "Executar instâncias EC2 para o cliente com latência menor que nas Regiões", "Armazenar backups dos bancos de dados RDS perto dos usuários para restauração rápida", "Hospedar as Zonas de Disponibilidade de cada Região perto dos usuários"],
        "correta": "Responder às consultas DNS próximo aos usuários, reduzindo a latência",
        "explicacao": "O Route 53 usa a rede global de pontos de presença para responder às consultas DNS com baixa latência e alta disponibilidade."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "No Amazon CloudFront, como se chama o local de onde o conteúdo original é buscado, como um bucket do S3 ou um Application Load Balancer?",
        "alternativas": ["Origem", "Zona de Disponibilidade", "Sub-rede", "Tópico"],
        "correta": "Origem",
        "explicacao": "A origem é a fonte do conteúdo. O CloudFront busca o conteúdo na origem e o armazena em cache nos pontos de presença para atender os usuários."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer executar pequenos trechos de código JavaScript nos pontos de presença do CloudFront para manipular cabeçalhos e redirecionar requisições com latência mínima. Qual recurso deve ser usado?",
        "alternativas": ["CloudFront Functions", "AWS Lambda em uma única Região", "Amazon EMR", "AWS Outposts"],
        "correta": "CloudFront Functions",
        "explicacao": "CloudFront Functions e Lambda@Edge permitem executar código nos pontos de presença para personalizar o conteúdo e o comportamento das requisições perto dos usuários."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson precisa de mais throughput do que uma única conexão do AWS Direct Connect oferece, e também quer criptografar o tráfego pela conexão dedicada. Qual combinação é possível?",
        "alternativas": ["Usar várias conexões Direct Connect e uma VPN site a site sobre o Direct Connect", "Usar apenas um internet gateway", "Usar o Amazon CloudFront como substituto", "Não é possível criptografar tráfego que passa pelo Direct Connect"],
        "correta": "Usar várias conexões Direct Connect e uma VPN site a site sobre o Direct Connect",
        "explicacao": "O Direct Connect não criptografa o tráfego por padrão. É possível combiná-lo com VPN IPsec ou MACsec, e agregar várias conexões para mais capacidade e resiliência."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é uma vantagem de usar o AWS Site-to-Site VPN como backup de uma conexão AWS Direct Connect?",
        "alternativas": ["Manter a conectividade com a AWS pela internet, de forma criptografada, caso a conexão dedicada falhe", "Dobrar a velocidade da conexão dedicada do Direct Connect, somando automaticamente a largura de banda das duas conexões", "Eliminar os custos do Direct Connect, já que a VPN passa a substituí-lo em tempo integral", "Hospedar sites estáticos"],
        "correta": "Manter a conectividade com a AWS pela internet, de forma criptografada, caso a conexão dedicada falhe",
        "explicacao": "Uma VPN site a site pode servir como caminho alternativo de baixo custo para manter a conectividade híbrida quando o Direct Connect fica indisponível."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual serviço permite consultar dados de vários bancos e do S3 com SQL padrão, pagando pela quantidade de dados verificados, sendo indicado para análises ad hoc?",
        "alternativas": ["Amazon Athena", "Amazon ElastiCache", "Amazon Neptune", "Amazon MQ"],
        "correta": "Amazon Athena",
        "explicacao": "O Athena consulta dados no S3 e, com conectores federados, em outras fontes, sem servidores para gerenciar e cobrando por dados verificados."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é a diferença entre o Amazon RDS e o Amazon Redshift quanto ao tipo de carga de trabalho?",
        "alternativas": ["O RDS é indicado para transações (OLTP); o Redshift é indicado para análises de grandes volumes de dados (OLAP)", "O RDS é um banco NoSQL; o Redshift é um cache", "Os dois são usados apenas para armazenar arquivos e imagens enviados pelos usuários das aplicações web e móveis da empresa", "O Redshift é indicado para pequenas transações de e-commerce (OLTP); o RDS é indicado para data warehouses (OLAP)"],
        "correta": "O RDS é indicado para transações (OLTP); o Redshift é indicado para análises de grandes volumes de dados (OLAP)",
        "explicacao": "Bancos OLTP lidam com muitas transações pequenas. Data warehouses como o Redshift armazenam dados em colunas e são otimizados para consultas analíticas complexas."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é a diferença entre bancos de dados relacionais e não relacionais (NoSQL)?",
        "alternativas": ["Os relacionais usam tabelas com esquema fixo e SQL; os NoSQL usam modelos flexíveis, como chave-valor, documentos ou grafos", "Os relacionais não permitem consultas com filtros; os NoSQL usam SQL padrão com esquema fixo, tabelas relacionadas e chaves estrangeiras", "Os NoSQL só armazenam arquivos de imagem e vídeo; os relacionais armazenam apenas números e datas em planilhas", "Não há diferença entre eles"],
        "correta": "Os relacionais usam tabelas com esquema fixo e SQL; os NoSQL usam modelos flexíveis, como chave-valor, documentos ou grafos",
        "explicacao": "RDS e Aurora são relacionais. DynamoDB (chave-valor), DocumentDB (documentos) e Neptune (grafos) são exemplos de bancos NoSQL na AWS."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação web armazena arquivos enviados pelos usuários. Qual serviço é o mais indicado para guardar esses arquivos de forma durável e acessível pela aplicação de qualquer instância?",
        "alternativas": ["Amazon S3", "Instance store", "Memória RAM da instância", "Amazon ElastiCache"],
        "correta": "Amazon S3",
        "explicacao": "O S3 é durável, escalável e acessível por API de qualquer lugar, ideal para armazenar arquivos enviados por usuários de aplicações com várias instâncias."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual afirmação sobre um volume do Amazon EBS e as Zonas de Disponibilidade está correta?",
        "alternativas": ["O volume EBS existe em uma Zona de Disponibilidade e é anexado a instâncias na mesma zona", "Um volume EBS pode ser anexado a qualquer instância em qualquer Região", "O volume EBS é replicado automaticamente para todas as Regiões", "O volume EBS é armazenado no ponto de presença mais próximo"],
        "correta": "O volume EBS existe em uma Zona de Disponibilidade e é anexado a instâncias na mesma zona",
        "explicacao": "O EBS é replicado dentro da sua Zona de Disponibilidade. Para usá-lo em outra zona ou Região, cria-se um snapshot e, a partir dele, um novo volume."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual é a diferença entre o Amazon EFS e o Amazon EBS?",
        "alternativas": ["O EFS é um sistema de arquivos compartilhado por muitas instâncias; o EBS é armazenamento em bloco anexado normalmente a uma instância", "O EFS armazena objetos acessados por API como o S3; o EBS é um sistema de arquivos compartilhado entre várias Regiões", "O EBS é compartilhado automaticamente entre Regiões; o EFS só pode ser montado por uma única instância por vez, em uma única Zona de Disponibilidade da conta", "Não há diferença entre eles"],
        "correta": "O EFS é um sistema de arquivos compartilhado por muitas instâncias; o EBS é armazenamento em bloco anexado normalmente a uma instância",
        "explicacao": "O EFS escala automaticamente e pode ser montado simultaneamente por milhares de instâncias em várias zonas. O EBS funciona como um disco para uma instância."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer coletar métricas e visualizar painéis operacionais usando ferramentas de código aberto conhecidas, mas sem gerenciar os servidores dessas ferramentas. Qual combinação de serviços gerenciados é adequada?",
        "alternativas": ["Amazon Managed Service for Prometheus e Amazon Managed Grafana", "AWS X-Ray e AWS CloudTrail Lake com consultas SQL", "Amazon Polly e Amazon Lex", "Amazon CloudWatch Logs e AWS Systems Manager Run Command"],
        "correta": "Amazon Managed Service for Prometheus e Amazon Managed Grafana",
        "explicacao": "A AWS oferece Prometheus e Grafana gerenciados, que reduzem o esforço operacional de executar essas ferramentas populares de observabilidade."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual modelo de computação a AWS oferece para executar código em resposta a eventos, sem servidores para gerenciar e com cobrança por milissegundo de execução?",
        "alternativas": ["AWS Lambda", "Amazon EC2 Dedicated Hosts", "AWS Outposts", "Amazon Lightsail"],
        "correta": "AWS Lambda",
        "explicacao": "O Lambda cobra pelo número de requisições e pela duração da execução, medida em milissegundos, conforme a memória configurada."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson quer que funções Lambda sejam acionadas automaticamente sempre que um novo item for gravado em uma tabela do DynamoDB. Qual recurso permite isso?",
        "alternativas": ["DynamoDB Streams", "Políticas de ciclo de vida do S3", "Amazon Route 53", "AWS Artifact"],
        "correta": "DynamoDB Streams",
        "explicacao": "O DynamoDB Streams registra as alterações nos itens da tabela, e o Lambda pode processar esses eventos automaticamente."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Qual destes serviços da AWS é global, e não específico de uma Região?",
        "alternativas": ["AWS IAM", "Amazon EC2", "Amazon RDS", "Amazon EBS"],
        "correta": "AWS IAM",
        "explicacao": "Serviços como IAM, Route 53 e CloudFront são globais. Recursos como instâncias EC2, bancos RDS e volumes EBS pertencem a uma Região ou Zona de Disponibilidade."
    },
]

QUESTOES += [
    {
        "dominio_id": 3,
        "template_pergunta": "A lojinha do Alyson, que trabalha com segurança patrimonial, quer transmitir com segurança vídeos de milhares de câmeras para a AWS, para armazenamento, reprodução e análise com machine learning. Qual serviço deve ser usado?",
        "alternativas": ["Amazon Kinesis Video Streams", "Amazon Data Firehose", "Amazon Kinesis Data Streams", "Amazon Polly"],
        "correta": "Amazon Kinesis Video Streams",
        "explicacao": "O Amazon Kinesis Video Streams captura, processa e armazena streams de vídeo de dispositivos conectados para análise, reprodução e machine learning."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação de análise precisa acessar objetos no S3 com latência de milissegundos de um dígito e altíssimo volume de requisições, aceitando que os dados fiquem em uma única Zona de Disponibilidade. Qual classe de armazenamento é a mais indicada?",
        "alternativas": ["S3 Express One Zone", "S3 Glacier Deep Archive", "S3 Standard-IA", "S3 Glacier Flexible Retrieval"],
        "correta": "S3 Express One Zone",
        "explicacao": "O S3 Express One Zone é uma classe de alto desempenho, em uma única zona, criada para aplicações sensíveis à latência e com grande volume de requisições."
    },
    {
        "dominio_id": 3,
        "template_pergunta": "Uma aplicação global precisa de um banco relacional com leituras de baixa latência em várias Regiões e recuperação rápida caso a Região principal fique indisponível. Qual recurso do Amazon Aurora atende a esse requisito?",
        "alternativas": ["Amazon Aurora Global Database", "Réplicas de leitura na mesma Zona de Disponibilidade", "Amazon Aurora com uma única instância", "Snapshots manuais semanais"],
        "correta": "Amazon Aurora Global Database",
        "explicacao": "O Aurora Global Database replica os dados para até várias Regiões secundárias com latência normalmente inferior a um segundo, permitindo leituras locais e recuperação de desastres."
    },
]

# =========================================================================
# AMPLIAÇÃO: DOMÍNIO 4 - FATURAMENTO, PREÇOS E SUPORTE
# =========================================================================
QUESTOES += [
    {
        "dominio_id": 4,
        "template_pergunta": "Qual é a diferença entre as Instâncias Reservadas padrão e as Instâncias Reservadas conversíveis?",
        "alternativas": ["As padrão oferecem desconto maior; as conversíveis permitem trocar a família, o sistema operacional ou a locação durante o prazo", "As conversíveis oferecem desconto maior e não permitem mudanças; as padrão permitem trocar livremente a família e o sistema operacional", "As padrão podem ser canceladas a qualquer momento sem custo, enquanto as conversíveis exigem sempre o pagamento antecipado total do prazo de três anos", "As conversíveis só existem para o Amazon S3"],
        "correta": "As padrão oferecem desconto maior; as conversíveis permitem trocar a família, o sistema operacional ou a locação durante o prazo",
        "explicacao": "As Instâncias Reservadas conversíveis oferecem mais flexibilidade em troca de um desconto um pouco menor que o das padrão."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Ao comprar Instâncias Reservadas, qual opção de pagamento oferece o maior desconto?",
        "alternativas": ["Pagamento adiantado total (All Upfront)", "Pagamento adiantado parcial (Partial Upfront)", "Sem pagamento adiantado (No Upfront)", "Pagamento sob demanda"],
        "correta": "Pagamento adiantado total (All Upfront)",
        "explicacao": "Quanto mais se paga adiantado e quanto maior o prazo (3 anos em vez de 1), maior o desconto das Instâncias Reservadas e dos Savings Plans."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson usa Amazon EC2, AWS Fargate e AWS Lambda e quer um modelo de desconto por compromisso de uso que se aplique automaticamente a todos eles, mesmo que mude a família de instância ou a Região. Qual opção deve ser escolhida?",
        "alternativas": ["Compute Savings Plans", "EC2 Instance Savings Plans", "Instâncias Reservadas padrão", "Instâncias Spot"],
        "correta": "Compute Savings Plans",
        "explicacao": "Os Compute Savings Plans oferecem a maior flexibilidade: o desconto vale para EC2 de qualquer família, tamanho e Região, além de Fargate e Lambda."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson sabe que continuará usando a família de instâncias M7g em uma Região específica pelos próximos 3 anos e quer o maior desconto entre os Savings Plans. Qual opção deve escolher?",
        "alternativas": ["EC2 Instance Savings Plans", "Compute Savings Plans", "Instâncias sob demanda", "Instâncias Spot"],
        "correta": "EC2 Instance Savings Plans",
        "explicacao": "Os EC2 Instance Savings Plans exigem compromisso com uma família de instâncias em uma Região e, em troca, oferecem descontos maiores que os Compute Savings Plans."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Como é definido o compromisso de um Savings Plan?",
        "alternativas": ["Um valor de uso por hora, em dólares, por um prazo de 1 ou 3 anos", "Uma quantidade fixa de instâncias de um mesmo tipo, reservada por mês", "Um número de usuários do IAM", "Um volume de dados armazenados no S3"],
        "correta": "Um valor de uso por hora, em dólares, por um prazo de 1 ou 3 anos",
        "explicacao": "No Savings Plan, o cliente se compromete a gastar um valor por hora (por exemplo, US$ 10/hora) durante o prazo. O uso acima do compromisso é cobrado sob demanda."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson vai executar uma aplicação nova por apenas dois meses, com uso imprevisível e sem tolerar interrupções. Qual opção de compra do EC2 é a mais adequada?",
        "alternativas": ["Instâncias sob demanda", "Instâncias Reservadas de 3 anos", "Instâncias Spot", "Savings Plans de 3 anos"],
        "correta": "Instâncias sob demanda",
        "explicacao": "As instâncias sob demanda não exigem compromisso nem pagamento antecipado e não são interrompidas pela AWS, sendo ideais para cargas curtas e imprevisíveis."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Para qual destas cargas de trabalho as Instâncias Spot NÃO são recomendadas?",
        "alternativas": ["Um banco de dados de produção que não pode ser interrompido", "Processamento de imagens em lote com novas tentativas automáticas", "Testes de integração contínua que podem ser repetidos em caso de falha", "Análise de big data tolerante a falhas e a interrupções das instâncias"],
        "correta": "Um banco de dados de produção que não pode ser interrompido",
        "explicacao": "Instâncias Spot podem ser recuperadas pela AWS com aviso de dois minutos. São ideais para cargas flexíveis e tolerantes a falhas, não para sistemas críticos sem interrupção."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual é a diferença entre Instâncias dedicadas e Hosts dedicados no Amazon EC2?",
        "alternativas": ["Ambos usam hardware exclusivo, mas o Host dedicado dá visibilidade e controle sobre o servidor físico, como soquetes e núcleos", "Instâncias dedicadas são compartilhadas com outros clientes, enquanto os Hosts dedicados são servidores físicos gratuitos para quem usa BYOL", "Hosts dedicados são gratuitos", "Não há diferença entre eles"],
        "correta": "Ambos usam hardware exclusivo, mas o Host dedicado dá visibilidade e controle sobre o servidor físico, como soquetes e núcleos",
        "explicacao": "O Host dedicado é indicado quando há licenças vinculadas ao servidor físico ou requisitos de conformidade que exigem controle sobre o posicionamento das instâncias."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson precisa garantir que terá capacidade EC2 disponível em uma Zona de Disponibilidade específica durante um evento, sem assumir compromisso de 1 ou 3 anos. Qual opção deve ser usada?",
        "alternativas": ["Reservas de capacidade sob demanda (On-Demand Capacity Reservations)", "Instâncias Spot", "Compute Savings Plans com compromisso mínimo de 1 ano", "Instâncias Reservadas regionais com prazo de 1 ano"],
        "correta": "Reservas de capacidade sob demanda (On-Demand Capacity Reservations)",
        "explicacao": "As reservas de capacidade sob demanda garantem capacidade em uma zona pelo tempo que o cliente quiser, cobradas pelo preço sob demanda, e podem ser combinadas com Savings Plans."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson usa o Amazon RDS de forma contínua e previsível. Qual opção pode reduzir o custo desse banco de dados?",
        "alternativas": ["Instâncias de banco de dados reservadas do RDS", "Instâncias Spot do RDS com desconto de até 90%", "Hosts dedicados do S3", "Desativar os backups automáticos"],
        "correta": "Instâncias de banco de dados reservadas do RDS",
        "explicacao": "O RDS oferece instâncias reservadas com prazo de 1 ou 3 anos e desconto significativo em relação ao preço sob demanda."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Quais são os três principais fatores que geram custos na maioria dos serviços da AWS?",
        "alternativas": ["Computação, armazenamento e transferência de dados de saída", "Número de usuários do IAM, de Regiões e de tags", "Quantidade de logins no console, de e-mails e de alarmes", "Tamanho da empresa, número de funcionários e setor de atuação"],
        "correta": "Computação, armazenamento e transferência de dados de saída",
        "explicacao": "Na AWS, os custos são impulsionados principalmente pela computação, pelo armazenamento e pelos dados transferidos para fora da AWS."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual destes recursos não tem custo adicional, sendo cobrados apenas os recursos que ele cria ou gerencia?",
        "alternativas": ["Amazon EC2 Auto Scaling", "Amazon EC2 sob demanda", "Amazon RDS", "NAT gateway"],
        "correta": "Amazon EC2 Auto Scaling",
        "explicacao": "Serviços como EC2 Auto Scaling, AWS CloudFormation, AWS Elastic Beanstalk, AWS IAM e AWS Organizations não têm custo adicional próprio."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual destes itens influencia o custo do Amazon S3?",
        "alternativas": ["Volume armazenado, classe de armazenamento, número de requisições e dados transferidos para fora", "Apenas o número de buckets criados", "Apenas o número de usuários do IAM com acesso aos buckets, cobrado por usuário ativo no mês e por bucket", "Apenas a Região onde a conta foi criada, já que o preço por GB é igual para qualquer volume de requisições"],
        "correta": "Volume armazenado, classe de armazenamento, número de requisições e dados transferidos para fora",
        "explicacao": "O custo do S3 depende do armazenamento por GB-mês, da classe escolhida, das requisições, das recuperações (em classes de arquivamento) e da transferência de saída."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Como é cobrado, em geral, o uso de instâncias EC2 Linux sob demanda?",
        "alternativas": ["Por segundo de uso, com mínimo de 60 segundos", "Por dia completo, mesmo que usadas por uma hora", "Por mês fixo, independentemente do uso real da instância", "Por número de arquivos armazenados no volume da instância"],
        "correta": "Por segundo de uso, com mínimo de 60 segundos",
        "explicacao": "Instâncias EC2 Linux e Windows sob demanda são cobradas por segundo, com mínimo de 60 segundos. Outros sistemas, como algumas distribuições comerciais, podem ser cobrados por hora."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson quer ser avisada automaticamente quando houver um gasto incomum, como um aumento repentino no custo de um serviço, detectado com machine learning. Qual recurso deve ser usado?",
        "alternativas": ["AWS Cost Anomaly Detection", "AWS Pricing Calculator", "AWS Artifact", "AWS Health Dashboard"],
        "correta": "AWS Cost Anomaly Detection",
        "explicacao": "O AWS Cost Anomaly Detection usa machine learning para identificar padrões de gasto incomuns e envia alertas para que a causa seja investigada rapidamente."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Quais tipos de orçamento podem ser criados no AWS Budgets?",
        "alternativas": ["Orçamentos de custo, de uso, de reservas e de Savings Plans", "Somente orçamentos de custo", "Somente orçamentos de número de usuários do IAM e de contas da organização", "Somente orçamentos de chamadas ao suporte"],
        "correta": "Orçamentos de custo, de uso, de reservas e de Savings Plans",
        "explicacao": "O AWS Budgets permite acompanhar custos, quantidade de uso e a utilização e cobertura de Instâncias Reservadas e Savings Plans."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson quer que, ao atingir 100% do orçamento de um projeto, novas instâncias sejam impedidas automaticamente de ser criadas. Qual recurso do AWS Budgets permite isso?",
        "alternativas": ["Ações do AWS Budgets (Budget actions)", "Relatórios do AWS Artifact", "Alarmes do AWS Health Dashboard para a conta", "Tags de alocação de custos"],
        "correta": "Ações do AWS Budgets (Budget actions)",
        "explicacao": "As ações de orçamento podem aplicar automaticamente uma política do IAM ou uma SCP, ou interromper instâncias EC2 e RDS, quando um limite é atingido."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma equipe financeira precisa dos dados de custo e uso mais detalhados possíveis, linha a linha e por recurso, para analisar em suas próprias ferramentas. Qual recurso deve ser usado?",
        "alternativas": ["AWS Cost and Usage Report (via AWS Data Exports)", "Estimativas exportadas do AWS Pricing Calculator", "Painel do AWS Billing and Cost Management", "AWS Artifact"],
        "correta": "AWS Cost and Usage Report (via AWS Data Exports)",
        "explicacao": "O Cost and Usage Report, entregue pelo AWS Data Exports em um bucket do S3, contém o conjunto mais completo de dados de custo e uso, podendo ser analisado com Athena ou QuickSight."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson aplicou a tag 'Projeto' em seus recursos, mas ela não aparece nos relatórios de custos. O que precisa ser feito?",
        "alternativas": ["Ativar a tag como tag de alocação de custos no console de Faturamento", "Excluir e recriar todos os recursos com a tag já aplicada na criação", "Contratar o plano de suporte Enterprise", "Mudar os recursos para a Região do Norte da Virgínia, onde fica o faturamento"],
        "correta": "Ativar a tag como tag de alocação de custos no console de Faturamento",
        "explicacao": "As tags definidas pelo usuário só aparecem nas ferramentas de custo depois de ativadas como tags de alocação de custos pela conta de gerenciamento."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson quer garantir que todos os recursos criados nas contas da organização sigam um padrão de nomes e valores de tags. Qual recurso do AWS Organizations ajuda nisso?",
        "alternativas": ["Políticas de tags (tag policies)", "Políticas de senha do IAM", "Políticas de backup do AWS Organizations", "Grupos de regras do WAF"],
        "correta": "Políticas de tags (tag policies)",
        "explicacao": "As políticas de tags do AWS Organizations padronizam chaves e valores de tags nas contas, facilitando a alocação de custos e a governança."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson quer agrupar seus custos em categorias de negócio, como 'Produto A' e 'Produto B', com base em regras que combinam contas, tags e serviços. Qual recurso deve ser usado?",
        "alternativas": ["AWS Cost Categories", "AWS Artifact", "AWS Pricing Calculator", "Amazon CloudWatch Logs"],
        "correta": "AWS Cost Categories",
        "explicacao": "O AWS Cost Categories permite mapear custos para categorias próprias da empresa, usando regras, e essas categorias aparecem no Cost Explorer, no Budgets e nos relatórios."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson revende serviços da AWS para seus clientes e precisa gerar faturas com taxas personalizadas para cada um (showback e chargeback). Qual serviço deve ser usado?",
        "alternativas": ["AWS Billing Conductor", "AWS Budgets", "AWS Pricing Calculator", "AWS Compute Optimizer"],
        "correta": "AWS Billing Conductor",
        "explicacao": "O AWS Billing Conductor permite agrupar contas e aplicar regras de preços personalizadas, gerando uma visão de faturamento própria para cada grupo."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Onde uma empresa pode obter recomendações de compra de Instâncias Reservadas e Savings Plans com base no seu histórico de uso?",
        "alternativas": ["No AWS Cost Explorer", "No AWS Artifact", "No AWS Health Dashboard", "No Amazon Inspector"],
        "correta": "No AWS Cost Explorer",
        "explicacao": "O Cost Explorer analisa o uso passado e recomenda compras de Instâncias Reservadas e Savings Plans, mostrando a economia estimada."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson tem várias contas em uma organização. Uma delas comprou Instâncias Reservadas que não estão sendo totalmente usadas. O que acontece com esse desconto no faturamento consolidado?",
        "alternativas": ["O desconto pode ser aplicado ao uso correspondente de outras contas da organização", "O desconto é perdido, pois só vale para a conta que fez a compra das Instâncias Reservadas", "O desconto é devolvido em dinheiro ao final do mês para a conta que fez a compra", "O desconto só vale para a conta de gerenciamento, que paga a fatura consolidada da organização"],
        "correta": "O desconto pode ser aplicado ao uso correspondente de outras contas da organização",
        "explicacao": "No faturamento consolidado, os benefícios de Instâncias Reservadas e Savings Plans são compartilhados entre as contas, a menos que esse compartilhamento seja desativado."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "No faturamento consolidado do AWS Organizations, qual conta é responsável por pagar a fatura de toda a organização?",
        "alternativas": ["A conta de gerenciamento", "Cada conta-membro paga sua própria fatura separadamente", "A conta com o maior gasto", "A conta criada mais recentemente"],
        "correta": "A conta de gerenciamento",
        "explicacao": "A conta de gerenciamento recebe e paga a fatura consolidada com as cobranças de todas as contas-membro, mantendo a visibilidade do custo de cada uma."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Quais tipos de recomendações de otimização de custos o AWS Trusted Advisor pode fazer?",
        "alternativas": ["Identificar instâncias EC2 ociosas, volumes EBS subutilizados e IPs elásticos não associados", "Negociar automaticamente descontos por volume com a equipe comercial da AWS em nome do cliente a cada mês", "Cancelar automaticamente a conta", "Mudar o plano de suporte sem autorização para o plano Enterprise sempre que houver economia prevista na fatura"],
        "correta": "Identificar instâncias EC2 ociosas, volumes EBS subutilizados e IPs elásticos não associados",
        "explicacao": "As verificações de otimização de custos do Trusted Advisor ajudam a eliminar recursos ociosos e subutilizados e a aproveitar opções de compra com desconto."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Quais são as categorias de verificações do AWS Trusted Advisor?",
        "alternativas": ["Otimização de custos, performance, segurança, tolerância a falhas, limites de serviço e excelência operacional", "Somente segurança e conformidade, com base nos relatórios do AWS Artifact e nas regras do AWS Config de cada conta da organização", "Somente faturamento, custos por serviço e previsões de gastos futuros", "Rede, DNS, e-mail, faturamento, contratos e licenças de software de terceiros"],
        "correta": "Otimização de custos, performance, segurança, tolerância a falhas, limites de serviço e excelência operacional",
        "explicacao": "O Trusted Advisor avalia o ambiente em seis categorias e mostra recomendações com status de alerta para cada verificação."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Um desenvolvedor quer consultar os preços dos serviços da AWS de forma programática para integrá-los a uma ferramenta interna de estimativas. Qual recurso deve usar?",
        "alternativas": ["AWS Price List API", "AWS Cost Explorer API", "AWS Health API", "AWS CloudTrail"],
        "correta": "AWS Price List API",
        "explicacao": "A AWS Price List API permite consultar programaticamente os preços dos produtos da AWS, com filtros por serviço, Região e atributos."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson quer receber um alarme quando o valor estimado da sua fatura do mês passar de US$ 1.000, usando métricas de faturamento. Qual serviço pode monitorar a métrica de cobranças estimadas?",
        "alternativas": ["Amazon CloudWatch", "AWS Artifact", "AWS Config", "Amazon Inspector"],
        "correta": "Amazon CloudWatch",
        "explicacao": "Com os alertas de faturamento ativados, o CloudWatch publica a métrica EstimatedCharges, que pode disparar alarmes. O AWS Budgets também atende a esse objetivo."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual afirmação sobre o plano Developer do AWS Support está correta?",
        "alternativas": ["Oferece acesso a engenheiros de suporte por e-mail em horário comercial, indicado para testes e desenvolvimento", "Inclui um Technical Account Manager designado", "Oferece resposta em 15 minutos para casos críticos de negócio e acesso 24x7 por telefone e chat aos engenheiros de suporte", "Inclui todas as verificações do Trusted Advisor e um Technical Account Manager designado para acompanhar a conta de perto"],
        "correta": "Oferece acesso a engenheiros de suporte por e-mail em horário comercial, indicado para testes e desenvolvimento",
        "explicacao": "O plano Developer é recomendado para quem está experimentando ou testando na AWS, com suporte técnico por e-mail em horário comercial e orientação geral."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual é o plano do AWS Support mais econômico que oferece acesso 24x7 a engenheiros de suporte por telefone, chat e e-mail, com resposta em menos de 1 hora para sistemas de produção fora do ar?",
        "alternativas": ["Business", "Developer", "Basic", "Enterprise"],
        "correta": "Business",
        "explicacao": "O plano Business é recomendado para cargas de produção, com suporte técnico 24x7, todas as verificações do Trusted Advisor e acesso à AWS Health API."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual plano do AWS Support oferece acesso a um grupo (pool) de Technical Account Managers e resposta em até 30 minutos para casos críticos de negócio?",
        "alternativas": ["Enterprise On-Ramp", "Enterprise", "Business", "Developer"],
        "correta": "Enterprise On-Ramp",
        "explicacao": "O Enterprise On-Ramp oferece um pool de TAMs para orientação proativa e resposta em até 30 minutos para casos críticos. O Enterprise oferece um TAM designado e resposta em 15 minutos."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual equipe do AWS Support, disponível nos planos Enterprise On-Ramp e Enterprise, é especializada em ajudar com questões de faturamento e de conta?",
        "alternativas": ["Equipe de suporte Concierge", "AWS Trust & Safety", "Shield Response Team", "AWS Professional Services"],
        "correta": "Equipe de suporte Concierge",
        "explicacao": "A equipe Concierge é formada por especialistas em faturamento e contas, que ajudam clientes corporativos a resolver dúvidas e otimizar questões financeiras."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson usa apenas o plano Basic do AWS Support e tem uma dúvida sobre uma cobrança na fatura. Ela pode abrir um caso de suporte?",
        "alternativas": ["Sim: todos os planos, inclusive o Basic, incluem suporte para questões de conta e faturamento", "Não: o Basic não permite abrir nenhum tipo de caso, nem mesmo de faturamento, apenas consultar a documentação", "Somente se pagar por um caso avulso de suporte técnico, cobrado à parte na fatura do mês seguinte", "Somente por meio de um AWS Partner"],
        "correta": "Sim: todos os planos, inclusive o Basic, incluem suporte para questões de conta e faturamento",
        "explicacao": "O atendimento ao cliente para questões de conta e faturamento está disponível em todos os planos. O suporte técnico exige o plano Developer ou superior."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual é o plano do AWS Support mais econômico que inclui acesso a suporte técnico por engenheiros da AWS?",
        "alternativas": ["Developer", "Basic", "Business", "Enterprise On-Ramp"],
        "correta": "Developer",
        "explicacao": "O Basic não inclui suporte técnico. O Developer é o primeiro plano pago com acesso a engenheiros de suporte, por e-mail em horário comercial."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Um desenvolvedor quer tirar dúvidas técnicas com a comunidade, especialistas da AWS e outros usuários, em um serviço de perguntas e respostas gerenciado pela AWS. Qual recurso deve usar?",
        "alternativas": ["AWS re:Post", "AWS Artifact", "AWS Marketplace", "AWS Budgets"],
        "correta": "AWS re:Post",
        "explicacao": "O AWS re:Post é uma comunidade de perguntas e respostas da AWS, com conteúdo moderado e respostas de especialistas e da comunidade."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Onde é possível encontrar artigos e vídeos que respondem às perguntas e solicitações mais frequentes recebidas pelo AWS Support?",
        "alternativas": ["AWS Knowledge Center", "AWS Artifact", "AWS Cost Explorer", "AWS Organizations"],
        "correta": "AWS Knowledge Center",
        "explicacao": "O AWS Knowledge Center, hoje integrado ao AWS re:Post, reúne respostas para as dúvidas mais comuns dos clientes, organizadas por serviço."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson quer contratar especialistas da própria AWS para ajudar em um grande projeto de transformação para a nuvem. Qual recurso deve ser procurado?",
        "alternativas": ["AWS Professional Services", "AWS re:Post", "AWS Marketplace", "AWS Partner Network (APN)"],
        "correta": "AWS Professional Services",
        "explicacao": "O AWS Professional Services é uma equipe global de especialistas que trabalha com clientes e parceiros para alcançar resultados de negócio com a nuvem."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma equipe quer se preparar para certificações da AWS com cursos digitais, laboratórios práticos e trilhas de aprendizagem oficiais. Qual recurso deve usar?",
        "alternativas": ["AWS Skill Builder", "AWS Artifact", "AWS Budgets", "AWS Health Dashboard"],
        "correta": "AWS Skill Builder",
        "explicacao": "O AWS Skill Builder é a plataforma oficial de treinamento da AWS, com centenas de cursos gratuitos e conteúdos adicionais por assinatura."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Uma startup quer obter créditos promocionais, treinamento e suporte da AWS para começar a construir seu produto. Qual programa é voltado para esse público?",
        "alternativas": ["AWS Activate", "AWS Migration Acceleration Program", "AWS Managed Services", "AWS Artifact"],
        "correta": "AWS Activate",
        "explicacao": "O AWS Activate oferece a startups créditos para serviços da AWS, suporte técnico e recursos de treinamento para acelerar o desenvolvimento."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Quais modelos de cobrança são oferecidos pelos produtos do AWS Marketplace?",
        "alternativas": ["Pagamento conforme o uso, assinaturas, contratos, BYOL e avaliações gratuitas, conforme o produto", "Apenas pagamento em dinheiro na entrega do software, feito diretamente ao representante do fornecedor do produto", "Apenas licenças perpétuas pagas diretamente ao fornecedor, fora da fatura da AWS, por transferência bancária", "Apenas produtos gratuitos"],
        "correta": "Pagamento conforme o uso, assinaturas, contratos, BYOL e avaliações gratuitas, conforme o produto",
        "explicacao": "O AWS Marketplace oferece vários modelos de preço, e as cobranças aparecem na fatura da AWS, simplificando a compra de software de terceiros."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson recebeu um erro informando que atingiu o limite de instâncias EC2 permitidas na Região. Onde ela pode visualizar esse limite e solicitar o aumento?",
        "alternativas": ["No console do Service Quotas", "No AWS Artifact", "No AWS Pricing Calculator", "No AWS Marketplace"],
        "correta": "No console do Service Quotas",
        "explicacao": "O Service Quotas permite visualizar as cotas (limites) dos serviços em cada Região e solicitar aumentos diretamente pelo console ou por API."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual afirmação sobre o custo do AWS Organizations está correta?",
        "alternativas": ["O AWS Organizations não tem custo adicional", "O AWS Organizations cobra por conta-membro adicionada", "O AWS Organizations só pode ser usado no plano Enterprise", "O AWS Organizations cobra uma porcentagem da fatura"],
        "correta": "O AWS Organizations não tem custo adicional",
        "explicacao": "O AWS Organizations é oferecido sem custo adicional. Os clientes pagam apenas pelos recursos usados nas contas."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Em geral, qual é o custo de transferir dados entre instâncias EC2 na mesma Zona de Disponibilidade usando endereços IP privados?",
        "alternativas": ["Não há cobrança", "É cobrado o dobro da transferência para a internet", "É cobrado por instância", "É cobrado por usuário do IAM"],
        "correta": "Não há cobrança",
        "explicacao": "A transferência de dados entre instâncias na mesma Zona de Disponibilidade por IPs privados não é cobrada. Entre zonas ou Regiões diferentes, normalmente há cobrança."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "Qual opção pode reduzir os custos de transferência de dados para a internet de um site com muito conteúdo estático acessado globalmente?",
        "alternativas": ["Usar o Amazon CloudFront para entregar o conteúdo a partir do cache", "Mover o site para uma instância EC2 maior, com mais largura de banda de rede", "Usar o AWS Artifact", "Desativar a compressão de arquivos"],
        "correta": "Usar o Amazon CloudFront para entregar o conteúdo a partir do cache",
        "explicacao": "O CloudFront reduz a carga na origem e, em geral, a transferência de dados da origem para o CloudFront não é cobrada, tornando a entrega global mais eficiente."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson quer encontrar um parceiro de tecnologia da AWS que ofereça um software já integrado e validado para seu caso de uso. Além do AWS Marketplace, qual recurso ajuda a encontrar esses parceiros?",
        "alternativas": ["AWS Partner Solutions Finder", "AWS Artifact", "AWS Prescriptive Guidance", "AWS Budgets"],
        "correta": "AWS Partner Solutions Finder",
        "explicacao": "O AWS Partner Solutions Finder permite pesquisar parceiros de consultoria e de tecnologia da AWS por especialização, setor, localização e caso de uso."
    },
    {
        "dominio_id": 4,
        "template_pergunta": "A lojinha do Alyson tem uma pergunta técnica urgente: seu sistema de produção está fora do ar. Ela possui o plano Business. Qual é o tempo de resposta de primeira linha esperado do AWS Support?",
        "alternativas": ["Menos de 1 hora", "Menos de 24 horas", "Menos de 12 horas", "Menos de 15 minutos"],
        "correta": "Menos de 1 hora",
        "explicacao": "No plano Business, casos de sistema de produção fora do ar têm resposta em menos de 1 hora. Respostas de 15 a 30 minutos para casos críticos de negócio são dos planos Enterprise."
    },
]
