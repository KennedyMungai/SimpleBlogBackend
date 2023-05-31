"""The schema file for the users"""
from typing import List

from pydantic import BaseModel, EmailStr

from schemas.article_schema import Article


class UserBase(BaseModel):
    email: EmailStr
    

class UserCreate(UserBase):
    password: str
    
    
class User(UserBase):
    id: int
    is_active: bool
    articles: List[Article] = []
    
    class Config:
        orm_mode = True