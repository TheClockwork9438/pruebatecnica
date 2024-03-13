from bson import ObjectId
from .database import collection
from .models import User
from datetime import datetime

def create_user(user: User):
    user_data = user.model_dump()
    user_data['fecha_creacion'] = datetime.now()
    result = collection.insert_one(user_data)
    return str(result.inserted_id)

def get_user(user_id: str):
    user = collection.find_one({"_id": ObjectId(user_id)})
    return user

def update_user(user_id: str, user: User):
    updated_user = collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict()})
    return str(updated_user.modified_count)

def delete_user(user_id: str):
    result = collection.delete_one({"_id": ObjectId(user_id)})
    return str(result.deleted_count)
