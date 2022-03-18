from . import PeeWeeBaseModel
import peewee as p

class Employees(PeeWeeBaseModel):
    id = p.PrimaryKeyField()
    nickname = p.TextField()
    fullname = p.TextField()
    mobile = p.TextField()
    email = p.TextField()
    activestatus = p.BooleanField()
    