from fastapi import APIRouter
from schemas.student import Student
from repositories.student import add_student, get_student, update_student, delete_student

router = APIRouter(prefix="/students", tags=["students"])

@router.get("")
def list_students():
    return {"message":"List of students"}


@router.post("")
def register_student(student:Student):
    add_student(student.name, student.age,student.email, student.country, student.id_number)
    return {"message": "Student registered successfully", "student": student}

@router.put("")
def modify_student(id_number: int, student: Student):
    update_student(id_number, student.name, student.age, student.email, student.country)
    return {"message": f"Student with ID {id_number} updated successfully"}

@router.delete("")
def remove_student(id_number: int):
    delete_student(id_number)
    return {"message": f"Student with ID {id_number} deleted successfully"}

