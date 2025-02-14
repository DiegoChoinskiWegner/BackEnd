# Usando uma imagem base do Python (especificando a versão)
FROM python:3.12.1

# Definindo o diretório de trabalho no container
WORKDIR /stract-2025

# Copiando os arquivos do seu projeto para o diretório de trabalho
COPY . /stract-2025

# Instalando as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expondo a porta em que o Flask vai rodar (geralmente 5000)
EXPOSE 8000

# Definindo o comando para iniciar a aplicação
CMD ["python", "app.py"]