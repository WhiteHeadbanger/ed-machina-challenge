from pydantic import BaseModel
from typing import List, Union
from schemas.career import Career


class Lead(BaseModel):
    lead_name: str
    email: str
    address: str
    phone: int
    inscription_year: int
    careers: Union[List[Career], None]

    class Config:
        orm_mode = True