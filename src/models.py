from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class UserData(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool
    phone_number: int
    salary: float
    join_date: date
    department: str
    bonus: Optional[float] = Field(default=0.0, ge=0.0)
    remote_work: bool
    education_level: str
    performance_rating: float
    city: str
    country: str
    gender: str
    marital_status: str
    project_count: int
    preferred_language: str
    notes: str