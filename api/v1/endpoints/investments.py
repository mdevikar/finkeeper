from fastapi import APIRouter

router = APIRouter()

@router.post("/stocks")
def add_stock_investment():
    return {"message": "Stock investment added successfully", "investment_id": "mock_UUID"}

@router.get("/stocks")
def get_stock_investments():
    return {"investments": [{"stock_name": "ABC Corp", "amount_invested": 1000}]}

@router.post("/property")
def add_property_investment():
    return {"message": "Property investment added successfully", "investment_id": "mock_UUID"}

@router.post("/fixed-deposits")
def add_fixed_deposit():
    return {"message": "Fixed deposit added successfully", "investment_id": "mock_UUID"}

@router.post("/mutual-funds")
def add_mutual_fund():
    return {"message": "Mutual fund added successfully", "investment_id": "mock_UUID"}
