from . import PeeWeeBaseModel
import peewee as p

class Employees(PeeWeeBaseModel):
    """
    CREATE TABLE employees (
        id SERIAL PRIMARY KEY,
        nickname TEXT UNIQUE NOT NULL,
        fullname TEXT NOT NULL,
        mobile TEXT UNIQUE,
        email TEXT UNIQUE,
        activestatus BOOLEAN DEFAULT TRUE
    )
    """
    id = p.PrimaryKeyField()
    nickname = p.TextField(unique = True, null = False)
    fullname = p.TextField(null = False)
    mobile = p.TextField(unique = True)
    email = p.TextField(unique = True)
    activestatus = p.BooleanField(default = True)
