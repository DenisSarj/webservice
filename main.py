from fastapi import FastAPI, Path
from pydantic import BaseModel
from pydantic import EmailStr
from typing import Annotated
from items_namespase import router as router_items
from users.views import router as router_users

import uvicorn

app = FastAPI()

app.include_router(router_items)
app.include_router(router_users)


@app.get('/')
def hello_index():
    return {
        'message': 'Hello index',
    }


@app.get('/hello/')
def hello(name: str):
    name = name.title().strip()
    return {'message': f'Hello {name}'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
