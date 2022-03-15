from fastapi import FastAPI

router = FastAPI()

@router.get('/')
def root_access():
    return {'message': 'Hello World'}
