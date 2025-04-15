from fastapi import FastAPI, APIRouter
from model import School, Student
from data import school_db, student_db

app = FastAPI(
    title="PDP School API LMS",
    version="0.0.2",
    description="Student for LMS"

)
router = APIRouter(
    prefix="/api"
)

school_data: dict = {}
student_data: dict = {}

@router.get("/")
async def root():
    return {"message": "Hello World"}

# http://127.0.0.1:8000/api/school
@router.get("/school")
async def school():
    return {"data": school_db}


@router.get("/student")
async def student():
    return {"data": student_db}


@router.post("/school")
async def school_create(schools: School):
    school_data["title"] = schools.title
    school_data["room"] = schools.room
    school_data["teacher"] = schools.teacher

    return {"data": school_data}


@router.post("/student")
async def student_create(students: Student):
    school_data["name"] = students.name
    school_data["email"] = students.email
    school_data["room_id"] = students.room_id
    school_data["since"] = students.since
    return {"data": school_data}


@router.get("/school/{school_name}")
async def school_name(school_name:str):
    for school in school_db:
        if school["title"].lower() == school_name.lower():
            return {"data" : school }


@router.get("/student/{student_name}")
async def student_name(student_name:str):
    for student in student_db:
        if student["name"].lower() == student_name.lower():
            return {"data":student}

app.include_router(router)