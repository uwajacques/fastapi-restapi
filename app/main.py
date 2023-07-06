from fastapi import FastAPI, HTTPException
from config.db import database
from models.todo import todos, TodoCreate, TodoUpdate

app = FastAPI()


@app.on_event("startup")
async def startup():
    # Connect to the database
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # Disconnect from the database
    await database.disconnect()


# Get all todos
@app.get("/todos")
async def root():
    try:
        query = todos.select()
        result = await database.fetch_all(query)
        return result

    except:
        raise HTTPException(
            status_code=500,
            detail="Oops something went wrong"
        )


# Create todo
@app.post("/todo")
async def create(todo: TodoCreate):
    try:
        query = todos.insert().values(
            id=str(todo.id), title=todo.title, completed=todo.completed)
        await database.execute(query)
        return todo

    except:
        raise HTTPException(
            status_code=500,
            detail="Oops something went wrong"
        )


# Get todo
@app.get("/todo/{todo_id}")
async def get_todo(todo_id: str):
    query = todos.select().where(todos.c.id == todo_id)
    result = await database.fetch_one(query)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Todo with id: {todo_id} was not found")
    return result


# Update todo
@app.put("/todo/{todo_id}")
async def update_todo(todo: TodoUpdate, todo_id: str):
    query = (
        todos.update()
        .where(todos.c.id == todo_id)
        .values(title=todo.title, completed=todo.completed)
        .returning(todos.c.id)
    )
    result = await database.execute(query)

    if not result:
        raise HTTPException(
            status_code=404, detail=f"Todo with id: {todo_id} was not found")
    return {**todo.dict(), "id": todo_id}


# Delete todo
@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: str):
    query = todos.delete().where(todos.c.id == todo_id)
    result = await database.execute(query)
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}
