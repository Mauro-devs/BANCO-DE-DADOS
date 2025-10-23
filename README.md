# Projeto CRUD com Oracle - Execução no Linux
Este projeto implementa um CRUD (Create, Read, Update, Delete) em **Python**, com integração ao **Oracle Database**.  
O ambiente de execução proposto é **Linux**.
<br>

## Pré-requisitos 🐧
Antes de iniciar, garanta que o seu ambiente Linux possua:
<br>

- **python 3.10+**
- **pip** (gerenciador de pacotes do Python)
- **docker**

## Criando o Ambiente Virtual (venv)
Antes de tudo, clone o projeto do GitHub 🐱:
```bash
git clone https://github.com/Mauro-devs/BANCO-DE-DADOS.git
```

Para isolar as dependências do projeto:

1. No diretório do projeto crie o ambiente virtual:
   ```bash
   python3 -m venv venv
   ```


2. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

3. Com o ambiente ativo, instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```
<br>

## Configuração da Conexão com o Banco 🐳
Para executar o projeto, é necessário que o Oracle Database esteja rodando.
Você pode usar uma instalação local ou, de forma mais prática, utilizar o Docker.

> Caso não possua o Oracle instalado, utilize o container oficial Oracle XE
<br>

1. Baixe a imagem:
   ```bash
   docker pull gvenzl/oracle-xe
   ```
2. Crie e inicie o container:
   ```bash
   docker run -d --name meu-oracle-db -p 1521:1521 -e ORACLE_PASSWORD=sua_senha_forte gvenzl/oracle-xe
   ```
3. Confirme que o container está rodando:
   ```bash
   docker ps
   ```
<br>

Por **segurança**🔒, as credenciais do banco não devem ser escritas diretamente no código.
Para configurar a conexão:

1. Dentro da pasta `connexion/`, crie uma subpasta chamada `acesso`:
   ```bash
   mkdir -p connexion/acesso
   ```
2. Dentro dela, crie o arquivo `autenticacao.oracle`:
   ```bash
   nano connexion/acesso/autenticacao.oracle
   ```
3. Adicione as informações do seu banco **na seguinte ordem**, separadas por vírgula:
   ```
   host,porta,servicename,user,senha
   ```
   Exemplo:
   >localhost,1521,XEP,admin,1234
<br>

## Execução do Projeto
Após ter feito os passos acima, rode esses comandos dentro da pasta do projeto clonado

1. Crie as tabelas no banco:
   ```bash
   python3 create_table.py
   ```

2. Execute o CRUD:
   ```bash
   python3 main.py
   ```
