from sqlalchemy.orm import Session
from app import models, schemas
from typing import Optional
from . import utils

def create_user(db: Session, email: str, name: str, lastname: str, password: str, role: str, img_url: Optional[str] = None):
    hashed_password = utils.hash_password(password)
    new_user = models.User(
        user_email=email,
        user_name=name,
        user_lastname=lastname,
        user_password=hashed_password,
        user_role=role,
        user_img=img_url
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.user_email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def update_user(db: Session, user_id: int, email: str, name: str, lastname: str, password: str, role: str, img_url: Optional[str] = None):
    user = get_user(db, user_id)
    user.user_email = email
    user.user_name = name
    user.user_lastname = lastname
    user.user_password = utils.hash_password(password)
    user.user_role = role
    user.user_img = img_url
    db.commit()
    db.refresh(user)
    return user