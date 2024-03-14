from bson import ObjectId
from .database import collection
from .models import User
from datetime import datetime


def create_user(user: User):
    user_data = user.model_dump()
    user_data["fecha_creacion"] = datetime.now()
    result = collection.insert_one(user_data)
    return str(result.inserted_id)


def get_user(user_id: str):
    user = collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
    return user


def update_user(user_id: str, user: User):
    updated_user = collection.update_one(
        {"_id": ObjectId(user_id)}, {"$set": user.model_dump()}
    )
    return str(updated_user.modified_count)


def delete_user(user_id: str):
    result = collection.delete_one({"_id": ObjectId(user_id)})
    return str(result.deleted_count)


def find_users(skip: int = 0, limit: int = 10):
    try:
        # List users using pagination
        cursor = collection.find({}).skip(skip).limit(limit)

        users_list = []
        for u in cursor:
            u["_id"] = str(u["_id"])  # Convert ObjectId to string
            users_list.append(u)

        return users_list
    except Exception as e:
        return {"error": str(e)}
