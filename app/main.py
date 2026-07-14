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



