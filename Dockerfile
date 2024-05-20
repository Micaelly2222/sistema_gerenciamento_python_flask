# Usando uma imagem oficial do Python como uma imagem de base
FROM python:3.9-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos requirements.txt e instalando as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiando o restante do código da aplicação
COPY . .

# Porta que o Flask usará
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
