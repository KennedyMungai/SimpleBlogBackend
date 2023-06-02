"""The CRUD service file"""
import hashlib

from fastapi import HTTPException
from sqlalchemy import update
from sqlalchemy.orm import Session

from models import *
from schemas.article_schema import *
from schemas.users_schema import *


hash = hashlib.sha256()