from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from user_registry.schemas import UserDB, UserList, UserPublic, UserSchema

app = FastAPI()


database = []


@app.post(
    '/create_user/', status_code=HTTPStatus.CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    db_user = UserDB(
        id=len(database) + 1,
        **user.model_dump(),
    )

    database.append(db_user)

    return db_user


@app.get('/read_users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.get(
    '/read_user/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
)
def read_user(user_id: int):
    if user_id > 0 and user_id <= len(database):
        db_user = database[user_id - 1]

        return db_user
    else:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
