from . import PeeWeeBaseModel
import peewee as p 

from models.employees import Employees
from models.categories import Categories


class Equipment(PeeWeeBaseModel):
    """
    CREATE TABLE equipment (
        id SERIAL PRIMARY KEY,
        serialnumber TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        category_id INT,
        employee_id INT NOT NULL,
        FOREIGN KEY (category_id) references categories(id),
        FOREIGN KEY (employee_id) references employees(id)
    )
    """
    id = p.PrimaryKeyField()
    serialnumber = p.TextField(unique = True, null = False)
    name = p.TextField(null = False)
    category = p.ForeignKeyField(Categories, backref="equipment")
    employee = p.ForeignKeyField(Employees, backref="equipment")