from sqlalchemy.orm import Session
from app.models import Class, class_day_enum
from typing import Optional
import time

def create_class(db: Session, class_day: str, class_course: str, class_hour_start: str, class_hour_end: str, user_id: int, subject_id: int, classroom_id: int):
    new_class = Class(
        class_day=class_day,
        class_course=class_course,
        class_hour_start=class_hour_start,
        class_hour_end=class_hour_end,
        user_id=user_id,
        subject_id=subject_id,
        classroom_id=classroom_id
    )
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

def get_classes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Class).offset(skip).limit(limit).all()

def get_class(db: Session, class_id: int):
    return db.query(Class).filter(Class.class_id == class_id).first()

def update_class(db: Session, class_id: int, class_day: str, class_course: str, class_hour_start: str, class_hour_end: str, user_id: int, subject_id: int, classroom_id: int):
    class_ = get_class(db, class_id)
    class_.class_day = class_day
    class_.class_course = class_course
    class_.class_hour_start = class_hour_start
    class_.class_hour_end = class_hour_end
    class_.user_id = user_id
    class_.subject_id = subject_id
    class_.classroom_id = classroom_id
    db.commit()
    db.refresh(class_)
    return class_

def delete_class(db: Session, class_id: int):
    class_ = get_class(db, class_id)
    db.delete(class_)
    db.commit()
    return class_

def get_classes_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Class).filter(Class.user_id == user_id).offset(skip).limit(limit).all()

def get_classes_by_subject(db: Session, subject_id: int, skip: int = 0, limit: int = 10):
    return db.query(Class).filter(Class.subject_id == subject_id).offset(skip).limit(limit).all()

def get_classes_by_classroom(db: Session, classroom_id: int, skip: int = 0, limit: int = 10):
    return db.query(Class).filter(Class.classroom_id == classroom_id).offset(skip).limit(limit).all()

def get_classes_by_user_and_subject(db: Session, user_id: int, subject_id: int, skip: int = 0, limit: int = 10):
    return db.query(Class).filter(Class.user_id == user_id, Class.subject_id == subject_id).offset(skip).limit(limit).all()

def get_classes_by_user_and_classroom(db: Session, user_id: int, classroom_id: int, skip: int = 0, limit: int = 10):
    return db.query(Class).filter(Class.user_id == user_id, Class.classroom_id == classroom_id).offset(skip).limit(limit).all()

def get_classes_by_subject_and_classroom(db: Session, subject_id: int, classroom_id: int, skip: int = 0, limit: int = 10):
    return db.query(Class).filter(Class.subject_id == subject_id, Class.classroom_id == classroom_id).offset(skip).limit(limit).all()

def get_classes_by_user_subject_and_classroom(db: Session, user_id: int, subject_id: int, classroom_id: int, skip: int = 0, limit: int = 10):
    return db.query(Class).filter(Class.user_id == user_id, Class.subject_id == subject_id, Class.classroom_id == classroom_id).offset(skip).limit(limit).all()

def get_classes_by_day(db: Session, class_day: str, skip: int = 0, limit: int = 10):
    return db.query(Class).filter(Class.class_day == class_day).offset(skip).limit(limit).all()

def get_classes_by_user_and_day(db: Session, user_id: int, class_day: str, skip: int = 0, limit: int = 10):
    return db.query(Class).filter(Class.user_id == user_id, Class.class_day == class_day).offset(skip).limit(limit).all()