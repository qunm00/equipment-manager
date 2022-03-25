from . import PeeWeeBaseModel
import peewee as p

class Categories(PeeWeeBaseModel):
    """
    CREATE TABLE categories (
	    id SERIAL PRIMARY KEY,
	    category TEXT UNIQUE NOT NULL
    )
    """
    id = p.PrimaryKeyField()
    category = p.TextField(unique = True, null = False)