from fastapi import FastAPI
import uvicorn

from db.models import Note
from db.settings import async_execution, async_addition

from schemas import schemas


app = FastAPI()


@app.get("/")
async def get_notes():
    result = await async_execution(Note)
    response = []
    for i in result:
        for j in i:
            response.append({
                "id": j.id,
                "title": j.title,
                "content": j.content
            })
    return response


@app.post("/notes")
async def add_notes(item: schemas.NotesList):
    notes = [Note(**note.dict()) for note in item.notes]
    await async_addition(notes)
    return item


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
