from fastapi import APIRouter

from playhouse.shortcuts import model_to_dict

from pydantic import BaseModel
from models.categories import Categories

router = APIRouter()

class Category(BaseModel):
    category: str

class CategoryID(Category):
    id: int

@router.get('/api/categories')
def get_all_categories():
    categories = Categories.select()
    categories = [model_to_dict(category) for category in categories]
    return categories

@router.get('/api/categories/{category}', response_model=CategoryID)
def get_by_category(category: str):
    category = Categories.get(Categories.category == category)
    return model_to_dict(category)

@router.post('/api/categories', response_model=Category)
def create_category(payload_: Category):
    payload = payload_.dict()
    category = Categories.create(**payload)
    return model_to_dict(category)