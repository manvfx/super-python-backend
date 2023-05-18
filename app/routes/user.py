from fastapi import APIRouter
from app.models.user import User
from app.database import db

userRoute = APIRouter()


@userRoute.get("/users")
def get_users_endpoint():
    users = db.users.find()
    result = []
    for user in users:
        try:
            result.append(User(user))
        except Exception as e:
            # handle any errors during instantiation
            print(f"Failed to create user from {user}: {e}")
    return result


@userRoute.post("/users/create")
def create_user_endpoint(user: User):
    db.users.insert_one(dict(user))
    return {"message": "User created successfully"}


@userRoute.patch("/users/:id/update")
def update_user_endpoint():
    return {"message": "update item"}


@userRoute.delete("/users/:id/delete")
def delete_user_endpoint():
    return {"message": "delete item"}
