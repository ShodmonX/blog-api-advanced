from sqlalchemy import Index, Integer, String, Boolean, Text, text, DateTime, Index, func, Enum as SQLEnum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime
from enum import Enum
from typing import Any

from app.db import Base


class UserRoleEnum(str, Enum):
    ADMIN = "admin"
    AUTHOR = "author"
    READER = "reader"

class User(Base):
    __tablename__ = "users"

    id:                 Mapped[int]             = mapped_column(Integer, primary_key=True, index=True)
    email:              Mapped[str]             = mapped_column(String(255), nullable=False)
    username:           Mapped[str]             = mapped_column(String(50), nullable=False)
    hashed_password:    Mapped[str]             = mapped_column(String(255), nullable=False)
    is_active:          Mapped[bool]            = mapped_column(Boolean, default=text("'true'"), server_default=text("'true'"))
    is_verified:        Mapped[bool]            = mapped_column(Boolean, default=text("'false'"), server_default=text("'false'"))
    is_superuser:       Mapped[bool]            = mapped_column(Boolean, default=text("'false'"), server_default=text("'false'"))
    created_at:         Mapped[datetime]        = mapped_column(DateTime(timezone=False), server_default=func.now())
    updated_at:         Mapped[datetime]        = mapped_column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())
    last_login:         Mapped[datetime | None] = mapped_column(DateTime(timezone=False), nullable=True)
    profile_image:      Mapped[str | None]      = mapped_column(String(255), nullable=True)
    timezone:           Mapped[str | None]      = mapped_column(String(50), nullable=True)
    bio:                Mapped[str | None]      = mapped_column(Text, nullable=True)
    website:            Mapped[str | None]      = mapped_column(String(255), nullable=True)
    location:           Mapped[str | None]      = mapped_column(String(100), nullable=True)
    role:               Mapped[UserRoleEnum]    = mapped_column(SQLEnum(UserRoleEnum, name="user_role_enum"), default=UserRoleEnum.READER, server_default=text("'reader'"))

    __table_args__ = (
        Index("ix_users_email", "email"),
        Index("ix_users_username", "username"),
        UniqueConstraint("email", name="uq_users_email"),
        UniqueConstraint("username", name="uq_users_username"),
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, username={self.username}, role={self.role})>"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "is_active": self.is_active,
            "is_verified": self.is_verified,
            "is_superuser": self.is_superuser,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "last_login": self.last_login,
            "profile_image": self.profile_image,
            "timezone": self.timezone,
            "bio": self.bio,
            "website": self.website,
            "location": self.location,
            "role": self.role,
        }