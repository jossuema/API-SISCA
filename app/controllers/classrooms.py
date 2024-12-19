from sqlalchemy.orm import Session
from app import models

def create_classroom(db: Session, number: int, type: str, nfccode: str):
    new_classroom = models.Classroom(
        classroom_number=number,
        classroom_type=type,
        classroom_nfccode=nfccode
    )
    db.add(new_classroom)
    db.commit()
    db.refresh(new_classroom)
    return new_classroom

def get_classrooms(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Classroom).offset(skip).limit(limit).all()

def get_classroom(db: Session, classroom_id: int):
    return db.query(models.Classroom).filter(models.Classroom.classroom_id == classroom_id).first()

def get_classroom_by_nfccode(db: Session, nfccode: str):
    return db.query(models.Classroom).filter(models.Classroom.classroom_nfccode == nfccode).first()

def update_classroom(db: Session, classroom_id: int, number: int, type: str, nfccode: str):
    classroom = get_classroom(db, classroom_id)
    classroom.classroom_number = number
    classroom.classroom_type = type
    classroom.classroom_nfccode = nfccode
    db.commit()
    db.refresh(classroom)
    return classroom

def delete_classroom(db: Session, classroom_id: int):
    classroom = get_classroom(db, classroom_id)
    db.delete(classroom)
    db.commit()
    return classroom

def get_classroom_classes(db: Session, classroom_id: int):  
    classroom = get_classroom(db, classroom_id)
    return classroom.classes

def get_classroom_reports(db: Session, classroom_id: int):
    classroom = get_classroom(db, classroom_id)
    return classroom.reports