from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client["user_db"]
collection = db["users"]
