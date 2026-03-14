from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Claude PR Review Test",
    description="Projeto simples para testar análise de PR com Claude",
)

app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "API rodando"}
