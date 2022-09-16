from models.database import Base
from sqlalchemy import String, Integer, Column, Identity
from sqlalchemy.orm import relationship

class LeadModel(Base):
    __tablename__ = "lead"
    
    id = Column(Integer, Identity(), primary_key = True)
    lead_name = Column(String(255), nullable = False)
    email = Column(String(255), nullable = False)
    address = Column(String(255), nullable = False)
    phone = Column(Integer, nullable = False)
    inscription_year = Column(Integer, nullable = False)
    
    reference = relationship("RegisterModel", back_populates="lead")

