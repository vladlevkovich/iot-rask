from peewee import *
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
db = PostgresqlDatabase(
    os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('DB_HOST')
)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(max_length=150)
    email = CharField(unique=True, max_length=50)
    password = CharField(max_length=10000)
    created = DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'users'


class Location(BaseModel):
    name = CharField(max_length=25)

    class Meta:
        db_table = 'locations'


class Device(BaseModel):
    name = CharField(max_length=50)
    type = CharField(max_length=25)
    login = CharField(max_length=50)
    password = CharField(max_length=10000)
    location = ForeignKeyField(Location)
    user = ForeignKeyField(User)

    class Meta:
        db_table = 'devices'
