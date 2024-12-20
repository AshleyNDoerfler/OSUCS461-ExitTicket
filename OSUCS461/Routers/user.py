from fastapi import APIRouter, HTTPException
from typing import List
from Classes.Database import UserLogic, PostLogic
from Models import User, ReadUser, ReadUserPost, CreateUserRequest

router = APIRouter()

@router.post("/users/", tags=["users"], response_model=ReadUser)
async def create_user(user: CreateUserRequest):
    try:
        user_id = UserLogic.create(user.email)
        created_user = UserLogic.get_by_uuid(user_id)
        if not created_user:
            raise HTTPException(status_code=404, detail="User could not be retrieved after creation.")
        return created_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route: Get a user by UUID
@router.get("/users/{user_uuid}", tags=["users"], response_model=ReadUser)
async def get_user(user_uuid: str):
    try:
        user = UserLogic.get_by_uuid(user_uuid)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        return user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route: Update a user by UUID
@router.put("/users/{user_uuid}", tags=["users"], response_model=ReadUser)
async def update_user(user_uuid: str, user: User):
    try:
        updated = UserLogic.update(user_uuid, user)
        if not updated:
            raise HTTPException(status_code=404, detail="User not found for update.")
        updated_user = UserLogic.get_by_uuid(user_uuid)
        return updated_user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route: Delete a user by UUID
@router.delete("/users/{user_uuid}", tags=["users"])
async def delete_user(user_uuid: str):
    try:
        deleted = UserLogic.delete(user_uuid)
        if not deleted:
            raise HTTPException(status_code=404, detail="User not found for deletion.")
        return {"message": "User deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route: Get all posts for a user
@router.get("/users/{user_uuid}/posts", tags=["posts"], response_model=List[ReadUserPost])
async def get_user_posts(user_uuid: str):
    try:
        posts = PostLogic.get_posts_by_user_uuid(user_uuid)
        if not posts:
            raise HTTPException(status_code=404, detail="No posts found for this user.")
        return posts
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
