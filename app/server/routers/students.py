from fastapi import APIRouter


router = APIRouter()

PREFIX = '/students'
TAGES = ['Students']


@router.get("/")
def list_students():
    return {}


@router.post("/")
def create_new_student():
    pass


@router.get("/{sudent_id}")
def get_student_by_id(student_id: int):
    pass


@router.put("/{student_id}")
def update_student_info(student_id: int):
    pass


@router.delete("/{student_id}")
def delete_student(student_id: int):
    pass
