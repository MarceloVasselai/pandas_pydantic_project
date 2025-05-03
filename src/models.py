from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class UserData(BaseModel):
    name: str
    email: str
    age: int
    birthdate: date
    height: float
    is_active: bool
    address: str
    phone_number: str
    salary: float
    join_date: date
    department: str
    position: str
    performance_score: Optional[int] = Field(default=None, ge=1, le=5)
    bonus: Optional[float] = Field(default=0.0, ge=0.0)
    has_company_car: bool
    remote_work: bool
    years_of_experience: int
    education_level: str
    certifications: Optional[str] = None
    last_promotion_date: Optional[date] = None