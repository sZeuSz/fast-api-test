# Usar a imagem oficial do Python (ajuste a versão se necessário)
FROM python:3.12

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock ./

# Instalar Poetry (a versão mais recente, que usa --without dev)
RUN pip install poetry

# Instalar dependências sem as dev dependencies
RUN poetry install --no-root

# Copiar o código da aplicação
COPY app ./app

# Expor a porta
EXPOSE 8000

# Comando para rodar o servidor
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
