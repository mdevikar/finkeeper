from fastapi import APIRouter

from api.v1.endpoints import users, earnings, expenses, investments

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(earnings.router, prefix="/earnings", tags=["earnings"])
router.include_router(expenses.router, prefix="/expenses", tags=["expenses"])
router.include_router(investments.router, prefix="/investments", tags=["investments"])
