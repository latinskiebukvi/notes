from typing import List
from pydantic import BaseModel


class Base(BaseModel):
    token: str


class Note(BaseModel):
    title: str
    content: str


class NotesList(Base):
    notes: List[Note]