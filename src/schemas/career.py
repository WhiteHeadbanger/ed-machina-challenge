from pydantic import BaseModel
from schemas.course import Course

from typing import Union, Dict, List

class Career(BaseModel):
    name: str
    courses: Union[List[Course], None]

    class Config:
        orm_mode = True