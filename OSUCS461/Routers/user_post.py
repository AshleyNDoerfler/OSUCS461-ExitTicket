from fastapi import APIRouter, HTTPException
from typing import List
from Classes.Database import UserLogic, PostLogic
from Models import User, UserPost, ReadUser, ReadUserPost, CreateUserRequest

router = APIRouter()

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

# Route: Create a post for a user
@router.post("/users/{user_uuid}/posts", tags=["posts"], response_model=ReadUserPost)
async def create_post(user_uuid: str, post: UserPost):
    try:
        post.user_uuid = user_uuid
        post_id = PostLogic.save(post)
        created_post = PostLogic.get_by_uuid(post_id)
        if not created_post:
            raise HTTPException(status_code=404, detail="Post could not be retrieved after creation.")
        return created_post
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
