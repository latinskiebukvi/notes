from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession


def model_to_dict(model):
    return {k: v for k, v in model.__dict__.items() if "_" not in k}


async def async_execution(session: AsyncSession, stmt, filter):
    result = await session.execute(select(stmt).filter(filter))
    return [model_to_dict(model) for model in result.scalars().all()]


async def async_addition(session: AsyncSession, items):
    session.add_all(items)
    await session.commit()


async def gen(iterable):
    for item in iterable:
        yield item


async def async_update(session: AsyncSession, items, stmt):
    async for item in gen(items):
        await session.execute(
            update(stmt).where(stmt.id == item.id).values(model_to_dict(item))
        )
        await session.commit()
