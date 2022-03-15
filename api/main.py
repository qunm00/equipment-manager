from typing import Optional
from fastapi import FastAPI

router = FastAPI()

@router.get("/")
def read_root():
    return {"Hello": "World"}