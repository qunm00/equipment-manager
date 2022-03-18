from fastapi import APIRouter

from typing import Optional
from playhouse.shortcuts import model_to_dict, update_model_from_dict

from models.employees import Employees 
from pydantic import BaseModel

router = APIRouter()

class Employee(BaseModel):
    activestatus: bool
    nickname: str
    fullname: str
    mobile: str
    email: str

@router.get('/api/employees')
def get_all_employees():
    employees = Employees.select().order_by(Employees.activestatus.desc(), Employees.nickname)
    employees = [model_to_dict(employee) for employee in employees]
    return employees

@router.get('/api/employees/{id}')
def get_employees_by_id(id: int):
    employee = Employees.get_by_id(id)
    return model_to_dict(employee)

@router.post('/api/employees', response_model=Employee)
def create_employee(payload_: Employee):
    payload = payload_.dict()
    employee = Employees.create(**payload)
    return model_to_dict(employee)

@router.put('/api/employees/{id}')
def edit_employee(id :int, payload_: Employee):
    payload = payload_.dict()
    employee = (Employees.update( 
        activestatus = payload['activestatus'],
        nickname = payload['nickname'],
        fullname = payload['fullname'],
        mobile = payload['mobile'],
        email = payload['email']
    )
    .where(Employees.id == id)
    .execute())

@router.delete('/api/employees/{id}')
def delete_employee(id: int):
    print('request received')