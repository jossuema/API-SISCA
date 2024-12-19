from sqlalchemy.orm import Session
from app import models, schemas
from typing import Optional

def create_subject(db: Session, name: str, description: Optional[str] = None):
    new_subject = models.Subject(
        subject_name=name,
        subject_description=description
    )
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    return new_subject

def get_subjects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Subject).offset(skip).limit(limit).all()

def get_subject(db: Session, subject_id: int):
    return db.query(models.Subject).filter(models.Subject.subject_id == subject_id).first()

def get_subject_by_name(db: Session, name: str):
    return db.query(models.Subject).filter(models.Subject.subject_name == name).first()

def update_subject(db: Session, subject_id: int, name: str, description: Optional[str] = None):
    subject = get_subject(db, subject_id)
    subject.subject_name = name
    subject.subject_description = description
    db.commit()
    db.refresh(subject)
    return subject

def delete_subject(db: Session, subject_id: int):
    subject = get_subject(db, subject_id)
    db.delete(subject)
    db.commit()
    return subject