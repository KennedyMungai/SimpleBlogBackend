"""The entrypoint for the application script"""
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from database.db import engine, get_db
from schemas.article_schema import Article
from schemas.users_schema import User, UserCreate
from services.crud_service import create_user, get_user_by_email

app = FastAPI(name="SImple Blog Project", description="A simple blog project", version="0.1.0")


@app.get("/", name='Root', description='The root endpoint for the application')
async def root():
    """The root endpoint for the application"""
    return {"Message": "App Works"}


@app.post("/users", name='Create User', description='Create a new user', response_model=User)
async def create_user_endpoint(_user: UserCreate, _db: Session = Depends(get_db)):
    """An endpoint to create the usr in the

    Args:
        _user (UserCreate): The schema used to create users in the database
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Raises:
        HTTPException: A 400 is raised if the user already exists

    Returns:
        User: The user created
    """
    _db_user = get_user_by_email(_user.email, _db)
    if _db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
    return create_user(_user, _db)
    