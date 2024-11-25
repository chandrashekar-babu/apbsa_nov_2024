from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED

class TodoItem(BaseModel):
    title: str
    description: str
    date: str 

def get_db():
    from pymongo import MongoClient
    conn = MongoClient()
    tododb = conn.todos
    return tododb.todos


app = FastAPI()

todos = get_db()

@app.get("/todos")
def get_todos():
    """Return a list of todos
       Each todo will have a title and description
    """
    return todos.find()

@app.post("/todos", status_code=HTTP_201_CREATED)
def post_todo(todo: TodoItem, response: Response):
    return todos.insert_one(todo.dict())

@app.get("/todos/{title}")
def get_todo(title: str):
    return todos.find_one({"title": title})
