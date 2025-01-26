from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def great() -> dict:
    return {"massage": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def news_id(user_id: int) -> dict:
    return {"massage": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def id_paginator(username: str, age: int) -> dict:
    return {"User": username, "Age": age}
