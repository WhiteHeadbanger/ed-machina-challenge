from models.database import Base, engine
from models.lead_model import LeadModel
from models.career_model import CareerModel
from models.course_model import CourseModel
from models.register_model import RegisterModel

print("Creating database...")

Base.metadata.create_all(bind=engine)