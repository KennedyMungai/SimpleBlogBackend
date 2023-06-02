"""The CRUD service file"""
import hashlib

from fastapi import HTTPException
from sqlalchemy import update
from sqlalchemy.orm import Session

from models.models import Article, User
from schemas.article_schema import *
from schemas.users_schema import *

hash = hashlib.sha256()


def get_user(_db: Session, user_id: int):
    """Get user by id"""
    return _db.query(User).filter(User.id == user_id).first()


def get_user_by_email(_db: Session, _email: str):
    """A function to retrieve the user via the emails

    Args:
        _db (Session): The database session
        _email (str): The email address for the user

    Returns:
        User: The user who used that email for registration
    """
    return _db.query(User).filter(User.email == _email).first()


def get_users(_db: Session, skip: int = 0, limit: int = 100):
    """Retrieves all the users from a database using some simple pagination logic

    Args:
        _db (Session): The database session
        skip (int, optional): The number of users to ski. Defaults to 0.
        limit (int, optional): The number of users to retrieve. Defaults to 100.

    Returns:
        User[]: An array of users
    """
    return _db.query(User).offset(skip).limit(limit).all()