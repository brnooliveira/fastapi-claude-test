from fastapi import APIRouter
from app.service import calculate_total

router = APIRouter()


@router.get("/total")
def total(price: float, quantity: int):
    result = calculate_total(price, quantity)
    return {"total": result}


@router.get("/users/{user_id}")
def get_user(user_id: int):
    users = {
        1: "Ana",
        2: "Carlos",
        3: "Pedro"
    }

    print("buscando usuário")
    return {"user": users[user_id]}
