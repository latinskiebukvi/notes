from fastapi import FastAPI
import uvicorn

from db.models import Note
from db.settings import async_execution


app = FastAPI()


@app.get("/")
async def root():
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


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
