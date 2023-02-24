from typing import List
from typing import Optional
from pydantic import BaseModel


class Base(BaseModel):
    token: Optional[str]


class Note(BaseModel):
    id: Optional[int]
    title: str
    content: str


class NotesList(Base):
    notes: List[Note]
