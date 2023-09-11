from fastapi import APIRouter

router = APIRouter()

@router.post("/monthly")
def add_monthly_expense():
    return {"message": "Monthly expense added successfully", "expense_id": "mock_UUID"}

@router.get("/monthly")
def get_monthly_expenses():
    return {"expenses": [{"type": "grocery", "amount": 200}]}

@router.post("/emi")
def add_emi():
    return {"message": "EMI added successfully", "emi_id": "mock_UUID"}

@router.post("/yearly")
def add_yearly_deduction():
    return {"message": "Yearly deduction added successfully", "deduction_id": "mock_UUID"}
