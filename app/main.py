from fastapi import FastAPI
from routers import task, user

app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)