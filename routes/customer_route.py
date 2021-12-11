from typing import List
from fastapi import Query
from pydantic.networks import EmailStr
from database.db_conn import get_session
from database.customer import Customer
from response.response import get_response
from request.customer_model import add_customer_model
from router import customer_api

@customer_api.get("/")
def get_customer(
    customerids: List[int] = Query(None, description="Enter the ids of customer",gt=0),
    customernames: List[str] = Query(None, description="Enter the names of customer"),
    phonenumbers: List[str] = Query(None, description="Enter the phone numbers of customer"),
    emails: List[EmailStr] = Query(None, description="Enter the email ids of customer")
):
    try:
        session = get_session()
        customer_filters = []
        if customerids:
            customer_filters.append(Customer.customerid.in_(customerids))
        if customernames:
            customer_filters.append(Customer.customername.in_(customernames))
        if phonenumbers:
            customer_filters.append(Customer.phonenumber.in_(phonenumbers))
        if emails:
            customer_filters.append(Customer.email.in_(emails))
        customer_details = session.query(Customer).filter(*customer_filters).all()
        if len(customer_details) == 0:
            return get_response("CUSTOMER_ERR003", None, 409)
        return get_response("CUSTOMER_RES001", customer_details, 200)
    except Exception as e:
        print("get_customer exception : ", e)
        return get_response("CUSTOMER_ERR001", None, 409)

@customer_api.post("/")
def add_customer(
    customer_details: add_customer_model
):
    try:
        session = get_session()
        add_customer_details = Customer(**customer_details.dict())
        session.add(add_customer_details)
        session.commit()
        return get_response("CUSTOMER_RES002", add_customer_details, 200)
    except Exception as e:
        print("add_customer exception : ", e)
        return get_response("CUSTOMER_ERR002", None, 409)