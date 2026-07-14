from fastapi import FastAPI
from database import create_table
from routers import student, teacher,course
    
app=FastAPI(title= "School Registration API")

create_table()

app.include_router(student.router)
app.include_router(teacher.router)
app.include_router(course.router)

  
@app.get("/", tags=["Root"])
def home ():
    return{"message: Welcome to my firstserver "}



# class Student(BaseModel):
#     name:str #type hint
#     age: int
#     email: str
#     country:str
#     id_number:int

# class Teacher(BaseModel):
#     name: str
#     subject: str
#     email: str
#     years_experience: int
#     employee_id: int

# class Course (BaseModel):
#     title: str
#     code: str
#     credits: int
#     department: str
#     description: str


# students=[]
  

# @app.get("/students")
# def list_students():
#     return {"message":"List of students"}


# @app.post("/students")
# def register_student(student:Student):
#     add_student(student.name, student.age,student.email, student.country, student.id_number)
#     return {"message": "Student registered successfully", "student": student}

# @app.put("/students/{id_number}")
# def modify_student(id_number: int, student: Student):
#     update_student(id_number, student.name, student.age, student.email, student.country)
#     return {"message": f"Student with ID {id_number} updated successfully"}

# @app.delete("/students/{id_number}")
# def remove_student(id_number: int):
#     delete_student(id_number)
#     return {"message": f"Student with ID {id_number} deleted successfully"}


# # Teacher
# @app.get("/teachers/{employee_id}")
# def view_teacher(employee_id: int):
#     teacher = get_teacher(employee_id)
#     return {"teacher": teacher}

# @app.get("/teachers")
# def register_teacher(teacher:Teacher):
#     add_teacher(teacher.name, teacher.subject, teacher.email, teacher.years_experience, teacher.employee_id)
#     return{"message": f"Teacher registered successfully", "teacher":teacher}

# @app.put("/teachers/{employee_id}")
# def modify_teacher(employee_id: int, teacher:Teacher):
#     update_teacher(employee_id,teacher.name, teacher.subject, teacher.email, teacher.years_experience)
#     return{"message": f"Teacher with ID {employee_id} updated successfully"}

# @app.delete("/teachers/{employee_id}")
# def remove_teacher(employee_id: int):
#     delete_teacher(employee_id)
#     return {"message": f"Teacher with ID {employee_id} deleted successfully"}

# # Courses
# @app.get("/courses")
# def list_courses():
#     return get_courses()

# @app.post("/courses")
# def create_course(course: Course):
#     add_course(course.title, course.code, course.credits, course.department, course.description)
#     return {"message": "Course created successfully", "course": course}

# @app.put("/courses/{code}")
# def modify_course(code: str, course: Course):
#     update_course(code, course.title, course.credits, course.department, course.description)
#     return {"message": f"Course {code} updated successfully"}

# @app.delete("/courses/{code}")
# def remove_course(code: str):
#     delete_course(code)
#     return {"message": f"Course {code} deleted successfully"}



    






