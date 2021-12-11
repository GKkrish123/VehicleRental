from sqlalchemy import Column, String, Integer
from database.base import base

class Vehicle(base):
    vehicletype = Column(String, nullable=False, primary_key=True)
    inventory = Column(Integer, nullable=False)