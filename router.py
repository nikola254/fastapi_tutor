from fastapi import Depends, APIRouter

from typing import Annotated

from schemas import SUserAdd, SUser, SUserId
from repository import UserRepository


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)


@router.post("")
async def add_user(
    user: Annotated[SUserAdd, Depends()], #для удобного ввоада в docs
) -> SUserId:
    user_id = await UserRepository.add_one(user)
    return {"ok": True, "user_id": user_id}


@router.get("")
async def get_users() -> list[SUser]:
    # Возвращаем данные пользователя с паролем для демонстрации
    users = await UserRepository.find_all()
    return users