from fastapi import FastAPI
from app.database import create_user, get_users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Super Backend",
    version="1.0.0",
)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": "Welcome to this app!",
    }

@app.post("/users")
def create_user_endpoint(user_data: dict):
    create_user(user_data)
    return {"message": "User created successfully"}

@app.get("/users")
def get_users_endpoint():
    users = get_users()
    return {"users": users}
