import peewee
from peewee import fn

from fastapi import APIRouter, HTTPException 

from playhouse.shortcuts import model_to_dict

from models.employees import Employees 

from pydantic import BaseModel

router = APIRouter()

class Employee(BaseModel):
    activestatus: bool
    nickname: str
    fullname: str
    mobile: str
    email: str

class EmployeeID(Employee):
    id: int

@router.get('/api/employees')
def get_all_employees():
    employees = Employees.select().order_by(Employees.activestatus.desc(), fn.LOWER(Employees.nickname))
    employees = [model_to_dict(employee) for employee in employees]
    return employees

@router.get('/api/employees/count')
def get_employees_count():
    count = Employees.select().count()
    return count

@router.get('/api/employees/{nickname}', response_model=EmployeeID)
def get_employee_by_nickname(nickname: str):
    employee = Employees.get(Employees.nickname == nickname)
    return model_to_dict(employee)
    

@router.post('/api/employees', response_model=Employee)
def create_employee(payload_: Employee):
    try:
        payload = payload_.dict()
        payload['nickname'] = payload['nickname'].lower().strip()
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
        employee = (Employees.update( 
            activestatus = payload['activestatus'],
            nickname = payload['nickname'].lower().strip(),
            fullname = payload['fullname'],
            mobile = payload['mobile'],
            email = payload['email'])
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
    try:
        employee = Employees.get_by_id(id)
        employee.delete_instance()
    except peewee.IntegrityError as e:
        error_message = str(e)
        if 'equipment_employee_id_fkey' in error_message:
            raise HTTPException(status_code=400, detail=f'{employee.nickname} is borrowing something')
        
        