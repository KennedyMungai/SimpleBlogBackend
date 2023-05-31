"""The file to hold the models for the app"""
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.db import Base


class User(Base):
    """The User model

    Args:
        Base (Declarative Base): The base for the model
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    
    articles = relationship("Article", back_populates='author', cascade='all, delete')
    
    def __repr__(self):
        return f"<User {self.email}>"
    
    
class Article(Base):
    """The model for the article data

    Args:
        Base (Declarative Base): No Idea
    """
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    body = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    author_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

    author = relationship("User", back_populates="articles")
    
    def __repr__(self):
        return f"<Article {self.title}>"