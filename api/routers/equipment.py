from fastapi import APIRouter

from typing import Optional

from playhouse.shortcuts import model_to_dict

from peewee import fn

from pydantic import BaseModel

from models.equipment import Equipment


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

@router.post('/api/equipment')
def create_equipment(payload_: Device):
    payload = payload_.dict()
    device = Equipment.create(**payload)
    return model_to_dict(device)

@router.patch('/api/equipment/{id}')
def update_equipment(id: int, payload_: Device):
    payload = payload_.dict()
    device = (Equipment.update(
        serialnumber = payload['serialnumber'],
        name = payload['name'],
        category = payload['category'],
        employee = payload['employee'])
    .where(Equipment.id == id)
    .execute())

@router.delete('/api/equipment/{id}')
def delete_equipment(id: int):
    device = Equipment.get_by_id(id)
    device.delete_instance()