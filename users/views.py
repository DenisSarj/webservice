from users.schemas import User
from fastapi import APIRouter
from users import crud

router = APIRouter(prefix='/user', tags=['User'])


@router.post('/')
def create_user(user: User):
    return crud.create_user(user_in=user)
