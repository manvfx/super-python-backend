from datetime import datetime
from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    created_at: datetime | None = None
    updated_at: datetime | None = None


class UserAuth(BaseModel):
    email: str
    password: str


class ResponseModel(BaseModel):
    message: str
    data: dict

    # Define arguments for the model
    def __init__(self, message: str, data: dict):
        super().__init__(message=message, data=data)


# def ResponseModel(data, message):
#     return {
#         "data": [data],
#         "code": 200,
#         "message": message,
#     }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message,
    }
