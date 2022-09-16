from pydantic import BaseModel

class Register(BaseModel):
    id_lead: int
    id_career: int
    id_course: int
    course_times_quantity: int

    class Config:
        orm_mode = True