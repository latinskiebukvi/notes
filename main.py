from typing import List

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn

from db.models import Note
from db.settings import (
    get_session,
    async_execution,
    async_addition,
    async_update
)

from schemas import schemas


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def get_notes(
    session: AsyncSession=Depends(get_session),
    response_model=schemas.Note
):
    result = await async_execution(session=session, stmt=Note, filter=Note.id.isnot(None))
    return {"notes": result}


@app.post("/")
async def add_notes(
    item: schemas.NotesList,
    session: AsyncSession=Depends(get_session)
):  
    to_add = []
    to_update = []

    for note in item.notes:
        if note.id is None:
            to_add.append(Note(**note.dict()))
        else:
            to_update.append(Note(**note.dict()))

    await async_update(session=session, items=to_update, stmt=Note)
    await async_addition(session=session, items=to_add)
    return item


if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",
        port=5000,
        log_level="info",
        reload=True
    )
    server = uvicorn.Server(config)
    server.run()
