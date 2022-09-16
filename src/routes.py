from fastapi import APIRouter, status

from models.database import SessionLocal

from models.lead_model import LeadModel
from models.course_model import CourseModel
from models.career_model import CareerModel
from models.register_model import RegisterModel

from schemas.lead import Lead

db = SessionLocal()

router = APIRouter()

# Show all leads, paginated.
@router.get('/')
def index():
    pass

# Create a new lead
@router.post('/create', response_model=Lead, status_code=status.HTTP_201_CREATED)
def create_lead(lead: Lead):
    # Get request body
    name = lead.name,
    email = lead.email,
    address = lead.address,
    phone = lead.phone,
    inscription_year = lead.inscription_year,
    careers = lead.careers

    db_lead = LeadModel(
        name=name,
        email=email,
        address=address,
        phone=phone,
        inscription_year=inscription_year
    )

    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    # get id_lead
    id_lead = db_lead.id

    careers_data = careers
    for career in careers_data:
        courses_data = career.courses
        
        db_career = CareerModel(name = career.name)
        db.add(db_career)
        db.commit()
        db.refresh(db_career)
        # get id_career
        id_career = db_career.id

        for course in courses_data:
            db_course = CourseModel(name = course.name, course_time = course.course_time)
            db.add(db_course)
            db.commit()
            db.refresh(db_course)
            # get id_course
            id_course = db_course.id

            # Reference table
            db_register = RegisterModel(id_lead = id_lead, id_career = id_career, id_course = id_course, course_times_quantity = course.course_times_quantity)
            db.add(db_register)
            db.commit()
            db.refresh(db_register)

    return {"Success": True, "Tracer_id": f"{id_lead}"}
    

# Pass an ID and get a result
# Query params
@router.get('/lead/{register_id}')
def show_lead():
    pass