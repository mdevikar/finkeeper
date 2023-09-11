from fastapi import APIRouter

router = APIRouter()

@router.post("/salary")
def add_salary():
    return {"message": "Salary added successfully", "salary_id": "mock_UUID"}

@router.get("/salary")
def get_salary():
    return {"amount": 5000, "last_increment_date": "2023-01-01"}
