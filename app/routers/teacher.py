from fastapi import APIRouter, HTTPException, status
from schemas.teacher import Teacher
from repositories.teacher import (
    add_teacher, 
    get_teachers, 
    update_teacher, 
    delete_teacher,
)

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.get("")
def view_teacher(employee_id: int):
    teacher = get_teachers(employee_id)
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    return {"teacher": teacher}

@router.get("")
def view_all_teachers():
    return {"teachers": get_teachers()}

@router.post("", status_code=status.HTTP_201_CREATED)
def register_teacher(teacher: Teacher):
    add_teacher(
        teacher.name, 
        teacher.subject, 
        teacher.email, 
        teacher.years_experience, 
        teacher.employee_id
    )
    return {"message": "Teacher registered successfully", "teacher": teacher}

@router.put("")
def modify_teacher(employee_id: int, teacher: Teacher):
    if not get_teachers(employee_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
        
    update_teacher(
        employee_id, 
        teacher.name, 
        teacher.subject, 
        teacher.email, 
        teacher.years_experience
    )
    return {"message": f"Teacher with ID {employee_id} updated successfully"}

@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def remove_teacher(employee_id: int):
    if not get_teachers(employee_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
        
    delete_teacher(employee_id)
    return None
