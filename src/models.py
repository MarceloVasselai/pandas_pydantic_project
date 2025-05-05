from pydantic import BaseModel, Field, EmailStr,field_validator
from datetime import date
from typing import Optional, Annotated

class UserData(BaseModel):
    name: str
    age: int
    email: EmailStr  # Validação de e-mail
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
    project_count: Annotated[int, Field(ge=0)]  # Contagem de projetos deve ser não negativa
    preferred_language: str
    notes: str

    @field_validator("notes")  # Validação do campo notes
    def validate_notes_contains_player(cls, value):
        if "player" not in value.lower():
            raise ValueError("The notes field must contain the word 'player'.")
        return value