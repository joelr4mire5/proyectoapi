import uuid
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app=FastAPI(title="APIs proyecto clase 5",
            version="0.0.1")

@app.post("/api/v1/register/")
async def register_user(username:str, email:str, password:str):
    return {
        "ID": str(uuid.uuid4()),
        "username":username,
        "email":email,
        "password":password,
        "message":"The user was registered successfully",

    }


@app.get("/api/v1/user_id/")
async def get_user(user_id:str):
    users ={
        "hola43443":{
            "username": "napster",
            "name": "gabo"
        },
        "ide-67":{
            "username": "andrey",
            "name": "gabo"
            }
        }

    if user_id in users:
        user= users[user_id]

        return JSONResponse(
        content=user,
        status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(
            content="No existe el usuario",
            status_code=status.HTTP_404_NOT_FOUND
        )
