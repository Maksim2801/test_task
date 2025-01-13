from pydantic import BaseModel
from typing import List

class OrganizationBase(BaseModel):
    name: str
    phone_number: str

class OrganizationOut(OrganizationBase):
    id: int
    class Config:
        orm_mode = True
