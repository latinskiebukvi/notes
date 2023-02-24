from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker


engine = create_async_engine(
    "postgresql+asyncpg://postgres:admin@localhost:5432/test",
    echo=True,
)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session():
    async with async_session() as session:
        yield session
