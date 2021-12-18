from sqlalchemy import Column, String, Integer
from .base import base
from .queries import add_table_query, fetch_table_query, edit_table_query


class Customer(base):
    customerid = Column(Integer, primary_key=True, autoincrement=True)
    customername = Column(String, nullable=False)
    phonenumber = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def get(self, primeid):
        try:
            return fetch_table_query(Customer, getbyprimeid=primeid)
        except Exception:
            raise

    def fetch(self, filters=[]):
        try:
            return fetch_table_query([Customer], filters=filters)
        except Exception:
            raise

    def add(self, tablevalues, session_close=True):
        try:
            return add_table_query(Customer, tablevalues, session_close=session_close)
        except Exception:
            raise

    def edit(self, filters, tablevalues, session_close=True):
        try:
            return edit_table_query(
                Customer, filters, tablevalues, session_close=session_close
            )
        except Exception:
            raise
