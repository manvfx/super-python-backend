from pymongo import MongoClient

# Database connection
client = MongoClient("mongodb://localhost:27017")
print("Connected to MongoDB...")
db = client["my_database"]
