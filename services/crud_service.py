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