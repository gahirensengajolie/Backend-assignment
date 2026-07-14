from pydantic import BaseModel
class Teacher(BaseModel):
    name: str
    subject: str
    email: str
    years_experience: int
    employee_id: int