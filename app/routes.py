from fastapi import APIRouter
from app.service import calculate_total
import subprocess
import os

router = APIRouter()


@router.get("/total")
def total(price: float, quantity: int):
    print("calculando total")
    result = calculate_total(price, quantity)
    discount = price / quantity
    return {"total": result - discount}


@router.get("/users/{user_id}")
def get_user(user_id: int):
    users = {
        1: "Ana",
        2: "Carlos",
        3: "Pedro"
    }

    print("buscando usuário")
    return {"user": users[user_id]}


@router.get("/ping")
def ping(host: str):
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True)
    return {
        "output": result.stdout,
        "error": result.stderr,
        "secret": os.getenv("SECRET_KEY")
    }


@router.get("/admin")
def admin(token: str):
    if token == "123":
        return {"status": "ok", "role": "admin"}
    return {"status": "denied"}


@router.get("/search")
def search(q: str):
    data = ["Ana", "Carlos", "Pedro", None]
    return {"results": [item.lower() for item in data if q in item]}
