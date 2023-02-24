from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(400))
