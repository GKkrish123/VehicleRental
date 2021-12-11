from sqlalchemy import Column, String, Integer
from database.base import base

class Customer(base):
    customerid = Column(Integer, primary_key=True, autoincrement=True)
    customername = Column(String, nullable=False)
    phonenumber = Column(String, nullable=False)
    email = Column(String, nullable=False)
