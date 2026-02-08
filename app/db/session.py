from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.core.settings import get_settings


settings = get_settings()

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)

LocalAsyncSession = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
