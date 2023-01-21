from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from sqlalchemy import update


engine = create_async_engine(
    "postgresql+asyncpg://postgres:admin@localhost:5432/test",
    echo=True,
)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session():
    async with async_session() as session:
        yield session


async def async_execution(session: AsyncSession, stmt, filter):
    result = await session.execute(select(stmt).filter(filter))
    return result.scalars().all()


async def async_addition(session: AsyncSession, items):
    session.add_all(items)
    await session.commit()


async def gen(iterable):
    for item in iterable:
        yield item


async def async_update(session: AsyncSession, items, stmt):
    async for item in gen(items):
        await session.execute(
            update(
                stmt
            ).where(
                stmt.id==item.id
            ).values(
                {k: v for k, v in item.__dict__.items() if "_" not in k}
            )
        )
        await session.commit()
