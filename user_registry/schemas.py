from datetime import date

from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    cpf: int
    birth_date: date


class UserDB(UserSchema):
    id: int


class UserPublic(BaseModel):
    id: int
    name: str
    birth_date: date


class UserList(BaseModel):
    users: list[UserPublic]
