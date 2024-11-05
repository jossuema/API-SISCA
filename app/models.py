from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Date, Enum, DateTime, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

# Enum para los roles y días de clase
class UserRole(enum.Enum):
    teacher = "teacher"
    admin = "admin"

class ClassDay(enum.Enum):
    Monday = "Lunes"
    Tuesday = "Martes"
    Wednesday = "Miercoles"
    Thursday = "Jueves"
    Friday = "Viernes"
    Saturday = "Sabado"
    Sunday = "Domingo"

# Modelo de User
class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    user_email = Column(String, unique=True, nullable=False)
    user_name = Column(String, nullable=False)
    user_lastname = Column(String, nullable=False)
    user_img = Column(String, nullable=True)  # URL para la imagen
    user_role = Column(Enum(UserRole), nullable=False)
    user_password = Column(String, nullable=False)
    
    # Relaciones
    reports = relationship("Report", back_populates="user")
    classes = relationship("Class", back_populates="user")

# Modelo de Subject
class Subject(Base):
    __tablename__ = 'subjects'
    
    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String, nullable=False)
    subject_description = Column(String, nullable=True)
    
    # Relaciones
    classes = relationship("Class", back_populates="subject")

# Modelo de Classroom
class Classroom(Base):
    __tablename__ = 'classrooms'
    
    classroom_id = Column(Integer, primary_key=True)
    classroom_number = Column(Integer, nullable=False)
    classroom_type = Column(Enum("lab", "normal"), nullable=False)
    classroom_nfccode = Column(String, nullable=False, unique=True)
    
    # Relaciones
    reports = relationship("Report", back_populates="classroom")
    classes = relationship("Class", back_populates="classroom")

# Modelo de Report
class Report(Base):
    __tablename__ = 'reports'
    
    report_id = Column(Integer, primary_key=True)
    report_time = Column(DateTime, nullable=False)
    report_date = Column(Date, nullable=False)
    classroom_id = Column(Integer, ForeignKey('classrooms.classroom_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    
    # Relaciones
    classroom = relationship("Classroom", back_populates="reports")
    user = relationship("User", back_populates="reports")

# Modelo de Class
class Class(Base):
    __tablename__ = 'classes'
    
    class_id = Column(Integer, primary_key=True)
    class_day = Column(Enum(ClassDay), nullable=False)
    class_hour_start = Column(Time, nullable=False)
    class_hour_end = Column(Time, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'), nullable=False)
    classroom_id = Column(Integer, ForeignKey('classrooms.classroom_id'), nullable=False)
    
    # Relaciones
    user = relationship("User", back_populates="classes")
    subject = relationship("Subject", back_populates="classes")
    classroom = relationship("Classroom", back_populates="classes")