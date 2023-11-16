from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import EmailStr

import uvicorn


class User(BaseModel):
    email: EmailStr
    name: str


app = FastAPI()


@app.get('/')
def hello_index():
    return {
        'messege': 'Hello index',
    }


@app.post('/user/')
def create_user(user: User):
    return {
        'email': user.email,
        'name': user.name,
        'message': 'Successfully!'
    }


@app.get('/hello/')
def hello(name: str):
    name = name.title().strip()
    return {'message': f'Hello {name}'}


@app.get("/items/")
def list_items():
    return [
        'item1',
        'item2',
    ]


@app.get('/items/latest/')
def get_latest_item():
    return {'item': {'id': 0, 'name': 'latest'}}


@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        'item':
            {'id': item_id}
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
