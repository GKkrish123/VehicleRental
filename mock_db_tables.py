from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import (
    SQL_DB_SYSTEM,
    DB_USERNAME,
    DB_PASSWORD,
    DB_SERVER,
    DB_HOST,
    DB_PORT
)

DB_URL = f'{SQL_DB_SYSTEM}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SERVER}'

db = create_engine(DB_URL)  
base = declarative_base()

class Customer(base):
    __tablename__ = "customer"

    customerid = Column(Integer, primary_key=True, autoincrement=True)
    customername = Column(String, nullable=False)
    phonenumber = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Rentalbooking(base):
    __tablename__ = "rentalbooking"

    bookingid = Column(Integer, primary_key=True, autoincrement=True)
    customername = Column(String, nullable=False)
    rentaldate = Column(String, nullable=False)
    returndate = Column(String)
    vehicletype = Column(String, nullable=False)

class Vehicle(base):
    __tablename__ = "vehicle"

    vehicletype = Column(String, nullable=False, primary_key=True)
    inventory = Column(Integer, nullable=False)

base.metadata.create_all(db)

Session = sessionmaker(db)  
session = Session()

objects = [
    Vehicle(vehicletype="bikes", inventory=2),
    Vehicle(vehicletype="cycle", inventory=3),
    Vehicle(vehicletype="car", inventory=1),
    Vehicle(vehicletype="boat", inventory=2)
]
session.bulk_save_objects(objects)
session.commit()
session.close()

print("\n! MOCK TABLES CREATED SUCCESSFULLY !")