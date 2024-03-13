from fastapi import FastAPI, HTTPException
from .models import User
from .crud import create_user, get_user, update_user, delete_user

app = FastAPI()

@app.post("/users/")
async def create_new_user(user: User):
    user_id = create_user(user)
    return {"message": "User created successfully", "user_id": user_id}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    user = get_user(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}")
async def update_existing_user(user_id: str, user: User):
    updated_count = update_user(user_id, user)
    if updated_count == "0":
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {"message": "User updated successfully"}

@app.delete("/users/{user_id}")
async def delete_existing_user(user_id: str):
    deleted_count = delete_user(user_id)
    if deleted_count == "0":
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {"message": "User deleted successfully"}
