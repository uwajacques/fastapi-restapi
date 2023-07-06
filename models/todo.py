from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4


class Todo(BaseModel):
    id: Optional[UUID] = uuid4()
    title: str
    completed: bool


class UpdateTodo(BaseModel):
    title: Optional[str]
    completed: Optional[bool]
