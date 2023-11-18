from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    name: Annotated[str, MinLen(1), MaxLen(52)]
