from fastapi import FastAPI

from routers import employees, equipment, categories

router = FastAPI()

@router.get('/api/')
def root():
    return {'message': 'Hello World'}

router.include_router(employees.router)
router.include_router(equipment.router)
router.include_router(categories.router)