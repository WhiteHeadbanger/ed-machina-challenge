from models.database import Base
from sqlalchemy import String, Integer, Column, Identity
from sqlalchemy.orm import relationship


class CourseModel(Base):
    __tablename__ = "course"

    id = Column(Integer, Identity(), primary_key=True)
    name = Column(String(255), nullable=False)
    course_time = Column(Integer, nullable=False)
    
    reference = relationship("RegisterModel", back_populates="course")