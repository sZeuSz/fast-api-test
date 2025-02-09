# Usar a imagem oficial do Python (ajuste a versão se necessário)
FROM python:3.12

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock ./

# Instalar Poetry
RUN pip install poetry

# Instalar dependências sem as dev dependencies
RUN poetry install --no-root --without dev

# Copiar o código da aplicação
COPY app ./app

# Expor a porta (opcional, pois a Vercel define a porta via variável)
EXPOSE 8000

# Comando para rodar o servidor, utilizando a variável de ambiente PORT (com fallback para 8000)
CMD ["sh", "-c", "poetry run uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
