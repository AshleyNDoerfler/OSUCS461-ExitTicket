from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    user_id: str = Field(..., description="Unique identifier for the user.")
    username: str = Field(..., min_length=3, max_length=50, description="Username of the user.")
    email: EmailStr = Field(..., description="User's email address.")
    is_active: Optional[bool] = Field(default=True, description="Indicates if the user is active.")

    class Config:
        schema_extra = {
            "example": {
                "user_id": "12345",
                "username": "johndoe",
                "email": "johndoe@example.com",
                "is_active": True,
            }
        }

class ReadUser(BaseModel):
    user_id: str
    username: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "user_id": "12345",
                "username": "johndoe",
                "email": "johndoe@example.com",
            }
        }

class CreateUserRequest(BaseModel):
    email: EmailStr
    username: str
    password: str 

    class Config:
        schema_extra = {
            "example": {
                "email": "johndoe@example.com",
                "username": "johndoe",
                "password": "securepassword",
            }
        }
