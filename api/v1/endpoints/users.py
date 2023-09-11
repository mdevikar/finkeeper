from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_user():
    return {"message": "User registered successfully", "user_id": "mock_UUID"}

@router.post("/login")
def login_user():
    return {"message": "Login successful", "token": "mock_JWT_token"}
