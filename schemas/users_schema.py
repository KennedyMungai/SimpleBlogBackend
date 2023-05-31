"""The schema file for the users"""
from typing import List

from pydantic import BaseModel, EmailStr

from schemas.article_schema import Article


class UserBase(BaseModel):
    """The base schema for the user data

    Args:
        BaseModel (Pydantic): The base class for the schema data
    """
    email: EmailStr


class UserCreate(UserBase):
    """The schema for the user creation

    Args:
        UserBase (UserBase): The base schema for the user data
    """
    password: str


class User(UserBase):
    """The template of the user data in the database

    Args:
        UserBase (Pydantic): The base for the schemas
    """
    id: int
    is_active: bool
    articles: List[Article] = []

    class Config:
        """The config class for the schemas"""
        orm_mode = True
