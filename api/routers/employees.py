from fastapi import APIRouter, HTTPException 

from typing import Optional
from playhouse.shortcuts import model_to_dict
from peewee import fn
import peewee

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
    employees = Employees.select().order_by(Employees.activestatus.desc(), fn.LOWER(Employees.nickname))
    employees = [model_to_dict(employee) for employee in employees]
    return employees

@router.post('/api/employees', response_model=Employee)
def create_employee(payload_: Employee):
    try:
        payload = payload_.dict()
        employee = Employees.create(**payload)
        return model_to_dict(employee)
    except peewee.IntegrityError as e:
        error_message = str(e)
        if 'employees_nickname_key' in error_message:
            raise HTTPException(status_code=400, detail='nickname already exists')
        if 'employees_email_key' in error_message:
            raise HTTPException(status_code=400, detail='email already exists')
        if 'employees_mobile_key' in error_message:
            raise HTTPException(status_code=400, detail='mobile number already exists')

@router.patch('/api/employees/{id}')
def edit_employee(id :int, payload_: Employee):
    try:
        payload = payload_.dict()
        # proper?
        employee = (Employees.update( 
            activestatus = payload['activestatus'],
            nickname = payload['nickname'],
            fullname = payload['fullname'],
            mobile = payload['mobile'],
            email = payload['email']
        )
        .where(Employees.id == id)
        .execute())
    except peewee.IntegrityError as e:
        error_message = str(e)
        if 'employees_nickname_key' in error_message:
            raise HTTPException(status_code=400, detail='nickname already exists')
        if 'employees_email_key' in error_message:
            raise HTTPException(status_code=400, detail='email already exists')
        if 'employees_mobile_key' in error_message:
            raise HTTPException(status_code=400, detail='mobile number already exists')

@router.delete('/api/employees/{id}')
def delete_employee(id: int):
    print(f'deleting employee {id}')
    employee = Employees.get_by_id(id)
    employee.delete_instance()
    print(f'successfully delete employeee {id}')