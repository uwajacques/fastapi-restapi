from fastapi import FastAPI, HTTPException, Response
from typing import List
from models.todo import Todo, UpdateTodo
from uuid import UUID

app = FastAPI()
db: List[Todo] = [
    Todo(
        id=UUID("fbdbe803-8e4b-4910-ace2-572dd000bd46"),
        title='Learn python',
        completed=False
    ),
    Todo(
        id=UUID("c5367802-9c73-4e66-92f0-627deff4da57"),
        title='Do shopping',
        completed=False
    ),
    Todo(
        id=UUID("03e9c262-8329-4969-997c-a57229561954"),
        title='Go to the park',
        completed=False
    ),
]


# Get all items
@app.get("/todos")
async def root():
    return db


# Create todo
@app.post("/todo")
async def create(todo: Todo):
    db.append(todo)
    return db


# Get todo
@app.get("/todo/{todo_id}")
async def get_todo(todo_id: str):
    for todo in db:
        if todo.id == UUID(todo_id):
            return todo

    raise HTTPException(
        status_code=404,
        detail=f"Todo with id: {todo_id} was not found"
    )


# Update todo
@app.put("/todo/{todo_id}")
async def update_todo(updated_todo: UpdateTodo, todo_id: str):
    for todo in db:
        if todo.id == UUID(todo_id):
            if updated_todo.title is not None:
                todo.title = updated_todo.title
            if updated_todo.completed is not None:
                todo.completed = updated_todo.completed
            return updated_todo

    raise HTTPException(
        status_code=404,
        detail=f"Todo with id: {todo_id} was not found"
    )


# Delete todo
@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: str):
    for todo in db:
        if todo.id == UUID(todo_id):
            db.remove(todo)

            return f"Todo with id: {todo_id} was deleted"

    raise HTTPException(
        status_code=404,
        detail=f"Todo with id: {todo_id} was not found"
    )