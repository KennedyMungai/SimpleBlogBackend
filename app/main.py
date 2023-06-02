"""The entrypoint for the application script"""
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from database.db import engine, get_db

from schemas.users_schema import User
from schemas.article_schema import Article

app = FastAPI(name="SImple Blog Project", description="A simple blog project", version="0.1.0")


@app.get("/", name='Root', description='The root endpoint for the application')
async def root():
    """The root endpoint for the application"""
    return {"Message": "App Works"}