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


@app.get("/api/v1/user/{id}/")
async def get_user(user_id:str):
    users ={
        "hola43443":{
            "username": "napster",
            "email": "gabo@gmail.com",
            "password": "123456789"
        },
        "hola43443":{
            "username": "david",
            "email": "david@gmail.com",
            "password": "12345678910"
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


@app.post("/api/v1/tasks/create")
async def create_task(task_title: str, description: str, state: str):
    return {
        "task_title": task_title,
        "description": description,
        "state": state,
        "message": "The task was created successfully"
    }

@app.get("/api/v1/tasks/{user_id}")
async def list_task(user_id:str):
    tasks = []
    tasks_info = [
        ["hola43443", "sum_function", "This function add numbers", "pending"],
        ["hola43443", "subtraction_function", "This function subtracts numbers", "pending"],
        ["hi11", "subtraction_function", "This function subtracts numbers", "pending"],

    ]
    for task in tasks_info:
        if task[0] == user_id:
            print(task[0])
            tasks.append(task[1::])

    return{
        "user_id": user_id,
        "tasks": tasks
    }
