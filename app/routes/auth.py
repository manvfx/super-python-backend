from fastapi import APIRouter

authRoute = APIRouter()

@authRoute.post("/login")
def login():
    return {"message": "Login successful"}

@authRoute.post("/register")
def register():
    return {"message": "Registration successful"}


@authRoute.get("/me")    
def me():
    return "current user information"