from pymongo import MongoClient

# Database connection
client = MongoClient("mongodb://localhost:27017")
db = client["my_database"]

# Example model
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Example CRUD operations
def create_user(user_data):
    user = User(name=user_data["name"], email=user_data["email"])
    db.users.insert_one(user.__dict__)

def get_users():
    users = db.users.find()
    return [User(**user) for user in users]
