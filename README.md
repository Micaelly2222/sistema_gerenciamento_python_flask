# Sistema de Gerenciamento de uma Cafeteria

## Descrição do Projeto
Este projeto é um sistema de gerenciamento para uma cafeteria, que auxilia na gestão das operações diárias como cadastro de clientes, gerenciamento de cardápio, pedidos e pagamentos, controle de estoque e geração de relatórios de vendas e consumo de produtos. O sistema é desenvolvido em Python utilizando o framework Flask e o banco de dados PostgreSQL.

## Funcionalidades
- **Cadastro de clientes:** Permite o cadastro de novos clientes, armazenando seus dados pessoais.
- **Gerenciamento de cardápio:** Cadastra e edita os itens do cardápio.
- **Pedidos e pagamentos:** Permite aos clientes realizar pedidos através do sistema, personalizando pedidos e escolhendo o método de pagamento.
- **Controle de estoque:** Monitora o estoque de ingredientes e produtos.
- **Relatórios e análises:** Gera relatórios simples de vendas e consumo de produtos.

## Tecnologias Utilizadas
- **Linguagem de programação:** Python (versão 3.x)
- **Framework web:** Flask
- **Banco de dados:** PostgreSQL
- **ORM (Object-Relational Mapping):** SQLAlchemy
- **Outras ferramentas:** Docker
- **Bibliotecas adicionais:** 
  - Para geração de relatórios: fpdf
  - Para a interface visual: HTML

# Guia de Configuração e Execução do Sistema de Gerenciamento

## Pré-requisitos

Para rodar este sistema, você precisará ter o Docker e o Docker Compose instalados em sua máquina. Siga os links abaixo para as instruções de instalação:

- **Docker:** [Instalação do Docker](https://docs.docker.com/get-docker/)
- **Docker Compose:** [Instalação do Docker Compose](https://docs.docker.com/compose/install/)

## Passo 1: Clonar o Repositório

Clone o repositório do projeto para a sua máquina local:

```sh
git clone https://github.com/usuario/sistema_gerenciamento_python_flask.git
cd sistema_gerenciamento_python_flask
```

## Passo 2: Instalar Dependências

```sh
pip install -r requirements.txt
```
## Passo 3: Executar o Docker Compose

```sh
docker-compose up
```

## Passo 4: Acessar a Aplicação

(http://localhost:5000)

## Dados de Exemplo

No arquivo modelo_inicializacao_banco.sql, você encontrará exemplos de instruções SQL para inicializar o banco de dados com dados de exemplo.

## Documentação Visual: pasta "docs"

No diretório docs, você encontrará uma coleção de imagens que fornecem visualizações das telas da aplicação. Essas imagens mostram diferentes aspectos e funcionalidades da aplicação, incluindo o cardápio, a página inicial, os pedidos, o estoque, os clientes e os relatórios de vendas e clientes. 

