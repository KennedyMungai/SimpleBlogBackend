"""The CRUD service file"""
import hashlib

from fastapi import HTTPException
from sqlalchemy import update
from sqlalchemy.orm import Session

from models.models import Article, User
from schemas.article_schema import ArticleCreate
from schemas.users_schema import User, UserCreate

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


def create_user(_db: Session, _user: UserCreate):
    """A function to add users to the database

    Args:
        _db (Session): The database session
        _user (UserCreate): The data needed to create users

    Returns:
        User: The created user
    """
    hash.update(_user.password.encode('utf-8'))
    hashed_password = hash.hexdigest()
    
    _db_user = User(_user.email, hashed_password)
    _db.add(_db_user)
    _db.commit()
    _db.refresh(_db_user)

    return _db_user


def get_articles(_db: Session, _skip:int = 0, _limit: int = 100):
    """A function to retrieve all the articles from the database

    Args:
        _db (Session): The database session
        _skip (int, optional): The number of articles to skip. Defaults to 0.
        _limit (int, optional): The number of articles to retrieve. Defaults to 100.

    Returns:
        Article[]: An array of articles
    """
    return _db.query(Article).offset(_skip).limit(_limit).all()


def create_article(_db: Session, _article: ArticleCreate, _user_id: int):
    """A function to add articles to the database

    Args:
        _db (Session): The database session
        _article (ArticleCreate): The data needed to create articles
        _user_id (int): The user id of the user who created the article

    Returns:
        Article: The created article
    """
    _db_article = Article(_article.title, _article.content, _user_id)
    _db.add(_db_article)
    _db.commit()
    _db.refresh(_db_article)

    return _db_article