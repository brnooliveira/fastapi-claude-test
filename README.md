# FastAPI Claude PR Review Test

Projeto simples para testar revisão automática de Pull Requests usando Claude.

## Rodar projeto

Instalar dependências:

pip install -r requirements.txt

Rodar servidor:

uvicorn app.main:app --reload

Abrir:

http://127.0.0.1:8000/docs

Endpoints:

- `/`
- `/total`
- `/users/{id}`
