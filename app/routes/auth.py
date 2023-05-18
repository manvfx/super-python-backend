from fastapi import APIRouter

from app.models.user import ResponseModel

authRoute = APIRouter()

@authRoute.post("/login")
def login():
    return {"message": "Login successful"}

@authRoute.post("/register")
def register():
    return {"message": "Registration successful"}


@authRoute.get("/me",response_model=ResponseModel)    
def me():
    response = {
        "message": "Success",
        "data": {"key": "value"}
    }
    return ResponseModel(**response)