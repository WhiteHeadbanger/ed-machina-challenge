from models.database import Base
from sqlalchemy import String, Integer, Column, Identity
from sqlalchemy.orm import relationship

class CareerModel(Base):
    __tablename__ = "career"
    
    id = Column(Integer, Identity(), primary_key=True)
    name = Column(String(255), nullable=False)
    
    reference = relationship("RegisterModel", back_populates="career")


