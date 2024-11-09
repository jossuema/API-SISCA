from sqlalchemy.orm import Session
from app import models, schemas
from . import utils

def create_user(db: Session, email: str, name: str, lastname: str, password: str, role: str, img_url: str | None = None):
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
