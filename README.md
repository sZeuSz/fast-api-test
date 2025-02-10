# Tender Manager Back

## 📌 Requirements

Before getting started, make sure you have installed:
- [Pyenv](https://github.com/pyenv/pyenv#installation)
- [Docker](https://docs.docker.com/get-docker/)
- [Poetry](https://python-poetry.org/docs/#installing-with-pipx)

---

## 🚀 Environment Setup

### 🔹 1. Install and Configure Pyenv

Add the following configurations to your `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`:
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```
Then, apply the changes:
```bash
source ~/.bashrc  # or source ~/.zshrc # or source ~/.bash_profile
```

Install and set the Python version:
```bash
pyenv install 3.12
```
```bash
pyenv local 3.12
```

---

### 🔹 2. Install Poetry

Install Poetry using `pipx`:
```bash
pipx install poetry==2.0.1 --python python3.12 --suffix "@tender-manager"
```

Add Poetry to `PATH` in `~/.bashrc`, `~/.zshrc` or `~/.bash_profile`:
```bash
export PATH="$HOME/.local/bin:$PATH"
```
Then, reload the terminal:
```bash
source ~/.bashrc  # or source ~/.zshrc # or source ~/.bash_profile
```

Set the Python version for Poetry:
```bash
poetry@tender-manager env use 3.12
```

Add the `poethepoet` plugin to Poetry:
```bash
export POETRY_VIRTUALENVS_OPTIONS_NO_PIP=true && \
poetry@tender-manager self add 'poethepoet[poetry_plugin]'
```

Install dependencies locally (Optional)
```bash
poetry@tender-manager install --no-root
```
---

## 🐳 Docker

### 🔹 3. Build and Run the Container

Build the Docker image:
```bash
poetry@tender-manager poe build-image
```

Start the container:
```bash
poetry@tender-manager poe run-container
```

Check if the API is responding:
```bash
curl http://localhost:8000/v1/ping
```

If everything is working correctly, you will see:
```json
{"message":"pong"}
```

### 🔹 4. Create and Apply Migrations
```bash
poetry@tender-manager run alembic revision --autogenerate -m "migration message"

```

```bash
poetry@tender-manager run alembic upgrade head

```
