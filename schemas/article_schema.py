"""The schema file for the articles"""
import email
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class ArticleBase(BaseModel):
    title: str
    body: Optional[str] = None
    

class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    author: EmailStr
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        orm_mode = True
        
    
class ArticleUpdate(BaseModel):
    title: Optional[str]
    body: Optional[str]
    
    class Config:
        orm_mode = True