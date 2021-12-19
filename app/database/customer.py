from sqlalchemy import Column, String, Integer
from .base import base


class Customer(base):
    customerid = Column(Integer, primary_key=True, autoincrement=True)
    customername = Column(String, nullable=False)
    phonenumber = Column(String, nullable=False)
    email = Column(String, nullable=False)
