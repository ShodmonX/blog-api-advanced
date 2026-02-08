from fastapi import APIRouter, Depends, Body

from typing import Annotated
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.modules.users.repositoy import UserRepository
from .service import AuthService
from .schemas import UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    db: Annotated[AsyncSession, Depends(get_db)],
    payload: Annotated[UserCreate, Body(...)]
):
    user_repo = UserRepository(db)
    auth_service = AuthService(user_repo)
    return await auth_service.register(email=payload.email, username=payload.username, password=payload.password)