from models.database import Base
from sqlalchemy import Integer, Column, ForeignKey, Identity
from sqlalchemy.orm import relationship

class RegisterModel(Base):
    __tablename__ = "register"

    id = Column(Integer, Identity(), primary_key = True)
    id_lead = Column(Integer, ForeignKey('lead.id'))
    id_career = Column(Integer, ForeignKey('career.id'))
    id_course = Column(Integer, ForeignKey('course.id'))
    course_times_quantity = Column(Integer, nullable=False)

    lead = relationship("LeadModel", back_populates="reference")
    career = relationship("CareerModel", back_populates="reference")
    course = relationship("CourseModel", back_populates="reference")

    