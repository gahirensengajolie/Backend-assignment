from fastapi import APIRouter
from schemas.course import Course
from repositories.course import (
    add_course, get_courses, update_course, delete_course
)


router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("")
def list_courses():
    return get_courses()

@router.post("")
def create_course(course: Course):
    add_course(course.title, course.code, course.credits, course.department, course.description)
    return {"message": "Course created successfully", "course": course}

@router.put("")
def modify_course(code: str, course: Course):
    update_course(code, course.title, course.credits, course.department, course.description)
    return {"message": f"Course {code} updated successfully"}

@router.delete("")
def remove_course(code: str):
    delete_course(code)
    return {"message": f"Course {code} deleted successfully"}