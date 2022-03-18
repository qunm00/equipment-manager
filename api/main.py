from fastapi import FastAPI

from routers import employees

router = FastAPI()

router.include_router(employees.router)

@router.get('/api/')
def root():
    return {'message': 'Hello World'}
