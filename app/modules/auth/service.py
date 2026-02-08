from sqlalchemy.exc import IntegrityError

from app.core.exceptions import Conflict
from app.core.security import get_password_hash, verify_password_hash
from app.modules.users.repositoy import UserRepository

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def register(self, *, email: str, username: str, password: str):
        hashed_password = get_password_hash(password)
        try:
            user = await self.user_repo.create(
                email=email,
                username=username,
                hashed_password=hashed_password,
            )
            return user
        except IntegrityError as e:
            constraint = getattr(getattr(e.orig, 'diag', None), 'constraint_name', None)
            if not constraint:
                raise Conflict(message="User with provided email or username already exists", code="user_exists")
            if constraint == "uq_users_email":
                raise Conflict(message="Email already exists", code="email_exists")
            if constraint == "uq_users_username":
                raise Conflict(message="Username already exists", code="username_exists")