from fastapi import FastAPI
from app.database import create_user, get_users

app = FastAPI()

@app.post("/users")
def create_user_endpoint(user_data: dict):
    create_user(user_data)
    return {"message": "User created successfully"}

@app.get("/users")
def get_users_endpoint():
    users = get_users()
    return {"users": users}
