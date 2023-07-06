from uuid import uuid4
from sqlalchemy import MetaData, Table, Column, Boolean, String
from pydantic import BaseModel


metadata = MetaData()

todos = Table(
    "todos",
    metadata,
    Column("id", String, primary_key=True, index=True),
    Column("title", String),
    Column("completed", Boolean),
)


class TodoCreate(BaseModel):
    id: str = str(uuid4())
    title: str
    completed: bool


class TodoUpdate(BaseModel):
    title: str
    completed: bool


class Todo(BaseModel):
    id: str
    title: str
    completed: bool
