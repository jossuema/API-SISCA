from sqlalchemy.orm import Session
from app.models import Report
from typing import Optional
import datetime

def create_report(db: Session, report_datetime: datetime, classroom_id: int, user_id: int):
    new_report = Report(
        report_datetime=report_datetime,
        classroom_id=classroom_id,
        user_id=user_id
    )
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return new_report

def get_reports(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Report).offset(skip).limit(limit).all()

def get_report(db: Session, report_id: int):
    return db.query(Report).filter(Report.report_id == report_id).first()

def update_report(db: Session, report_id: int, report_datetime: datetime, classroom_id: int, user_id: int):
    report = get_report(db, report_id)
    report.report_datetime = report_datetime
    report.classroom_id = classroom_id
    report.user_id = user_id
    db.commit()
    db.refresh(report)
    return report

def delete_report(db: Session, report_id: int):
    report = get_report(db, report_id)
    db.delete(report)
    db.commit()
    return report

def get_reports_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Report).filter(Report.user_id == user_id).offset(skip).limit(limit).all()

def get_reports_by_classroom(db: Session, classroom_id: int, skip: int = 0, limit: int = 10):
    return db.query(Report).filter(Report.classroom_id == classroom_id).offset(skip).limit(limit).all()

def get_reports_by_user_and_classroom(db: Session, user_id: int, classroom_id: int, skip: int = 0, limit: int = 10):
    return db.query(Report).filter(Report.user_id == user_id, Report.classroom_id == classroom_id).offset(skip).limit(limit).all()

def get_reports_by_date(db: Session, report_datetime: datetime, skip: int = 0, limit: int = 10):
    return db.query(Report).filter(Report.report_datetime == report_datetime).offset(skip).limit(limit).all()

def get_reports_by_user_and_date(db: Session, user_id: int, report_datetime: datetime, skip: int = 0, limit: int = 10):
    return db.query(Report).filter(Report.user_id == user_id, Report.report_datetime == report_datetime).offset(skip).limit(limit).all()

def get_reports_by_classroom_and_date(db: Session, classroom_id: int, report_datetime: datetime, skip: int = 0, limit: int = 10):
    return db.query(Report).filter(Report.classroom_id == classroom_id, Report.report_datetime == report_datetime).offset(skip).limit(limit).all()

def get_reports_by_user_classroom_and_date(db: Session, user_id: int, classroom_id: int, report_datetime: datetime, skip: int = 0, limit: int = 10):
    return db.query(Report).filter(Report.user_id == user_id, Report.classroom_id == classroom_id, Report.report_datetime == report_datetime).offset(skip).limit(limit).all()
    