FROM python:3.9-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y curl build-essential

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do Poetry
COPY pyproject.toml poetry.lock* /app/

# Instala o Poetry de forma oficial
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Desabilita venvs e instala dependências
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copia o restante do código
COPY . .

# Expõe porta da aplicação
EXPOSE 8000

# Comando para rodar o FastAPI com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
