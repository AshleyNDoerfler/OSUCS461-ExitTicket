from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime


Base = declarative_base()

class UserPost(Base):
    __tablename__ = "user_posts"
    
    post_id = Column(String, primary_key=True, index=True)
    user_uuid = Column(String, index=True)
    title = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=func.now())
    
    @classmethod
    def get_by_uuid(cls, post_id: str, db_session):
        post = db_session.query(cls).filter_by(post_id=post_id).first()
        return post

class ReadUserPost(BaseModel):
    post_id: str
    user_uuid: str
    title: str
    content: str
    created_at: datetime
    
    class Config:
        orm_mode = True  # Allows ORM models to be converted to Pydantic models
