from fastapi import FastAPI
from api.v1 import router as api_v1_router

app = FastAPI()

app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to FinKeeper!"}
