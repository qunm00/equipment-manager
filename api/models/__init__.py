from playhouse.postgres_ext import PostgresqlExtDatabase
from peewee import Model

from contextvars import ContextVar

db_context_var: ContextVar[PostgresqlExtDatabase] = ContextVar("db")

psql_db = PostgresqlExtDatabase(
    'equipment_manager',
    user='postgres',
    password='postgres',
    host='db',
    port=5432,
    autorollback=True
)

def create_db():
    """Create db connection"""
    return psql_db

def _get_db():
    if db_context_var.get(None) is None:
        db_context_var.set(create_db())
    return db_context_var.get()

class _DBProxy:
    def __getattr__(self, item):
        return getattr(_get_db(), item)

    def __setattr__(self, key, value):
        return setattr(_get_db(), key, value)

db = _DBProxy()

class PeeWeeBaseModel(Model):
    class Meta:
        database = psql_db
        schema = 'public'
        legacy_label_names = False
