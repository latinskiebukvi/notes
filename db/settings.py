from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select


engine = create_async_engine(
    "postgresql+asyncpg://postgres:admin@localhost:5432/test",
    echo=True,
)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def async_execution(stmt):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(stmt))
            return result