from pydantic import BaseModel

class Course(BaseModel):
    name: str
    course_time: int
    course_times_quantity: int

    class Config:
        orm_mode = True