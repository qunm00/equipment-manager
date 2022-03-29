from pkg_resources import AvailableDistributions
from fastapi import APIRouter, HTTPException

from typing import Optional

from playhouse.shortcuts import model_to_dict

from peewee import fn, JOIN
import peewee

from pydantic import BaseModel

from models.equipment import Equipment
from models.categories import Categories
from models import db

router = APIRouter()

class Device(BaseModel):
    serialnumber: str
    name: str
    category: int 
    employee: Optional[int]

@router.get('/api/equipment')
def get_all_equipment():
    equipment = Equipment.select().order_by(fn.LOWER(Equipment.name))
    equipment = [model_to_dict(device) for device in equipment]
    return equipment

@router.get('/api/equipment/count')
def get_equipment_count():
    count = Equipment.select().count()
    return count

@router.get('/api/equipment/availability-count')
def get_availability_count():
    availability = db.execute_sql("select c.category, count(*) from equipment as e join categories as c on e.category_id = c.id " + 
                                        "where e.employee_id is null " +
                                        "group by c.category")
    availability_list = [] 
    for device in availability.fetchall():
        availability_list.append({
            'name': device[0],
            'count': device[1]
        })
    return availability_list

@router.post('/api/equipment')
def create_equipment(payload_: Device):
    try:
        payload = payload_.dict()
        payload['serialnumber'] = payload['serialnumber'].lower().strip()
        device = Equipment.create(**payload)
        return model_to_dict(device)
    except peewee.IntegrityError as e:
        error_message = str(e)
        if 'equipment_serialnumber_key' in error_message:
            raise HTTPException(status_code=400, detail='Equipment serial number already exists')

@router.patch('/api/equipment/{id}')
def update_equipment(id: int, payload_: Device):
    try:
        payload = payload_.dict()
        device = (Equipment.update(
            serialnumber = payload['serialnumber'].lower().strip(),
            name = payload['name'],
            category = payload['category'],
            employee = payload['employee'])
        .where(Equipment.id == id)
        .execute())
    except peewee.IntegrityError as e:
        error_message = str(e)
        if 'equipment_serialnumber_key' in error_message:
            raise HTTPException(status_code=400, detail='Equipment serial number already exists')
        

@router.delete('/api/equipment/{id}')
def delete_equipment(id: int):
    device = Equipment.get_by_id(id)
    print(device.employee)
    device.delete_instance()
        