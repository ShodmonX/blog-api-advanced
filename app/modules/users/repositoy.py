from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from .model import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, user_id: int) -> User | None:
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalars().first()

    async def get_user_by_email(self, email: str) -> User | None:
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalars().first()
    
    async def create(self, *, email: str, username: str, hashed_password: str) -> User:
        user = User(
            email=email, 
            username=username, 
            hashed_password=hashed_password
        )
        self.db.add(user)
        await self.db.flush()
        await self.db.refresh(user)
        return user