from sqlalchemy import Column, String, Integer
from database.base import base

class Rentalbooking(base):
    bookingid = Column(Integer, primary_key=True, autoincrement=True)
    customername = Column(String, nullable=False)
    rentaldate = Column(String, nullable=False)
    returndate = Column(String)
    vehicletype = Column(String, nullable=False)
