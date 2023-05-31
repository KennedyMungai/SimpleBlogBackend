"""The schema file for the articles"""
import email
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class ArticleBase(BaseModel):
    """The base article for the article data

    Args:
        BaseModel (Pydantic model): The parent class for the Schemas
    """
    title: str
    body: Optional[str] = None


class ArticleCreate(ArticleBase):
    """The schemas used when creating articles in the database

    Args:
        ArticleBase (Pydantic): The base class for the schemas
    """
    pass


class Article(ArticleBase):
    """The template for the data as it is being stored in the database

    Args:
        ArticleBase (Pydantic): The base class for the schemas
    """
    id: int
    author: EmailStr
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        """The config class for the schema"""
        orm_mode = True


class ArticleUpdate(BaseModel):
    """The schema used to update articles in the database

    Args:
        BaseModel (Pydantic model): The  parent class for the Schemas
    """
    title: Optional[str]
    body: Optional[str]

    class Config:
        """The config class for the schema"""
        orm_mode = True
