from typing import List
from fastapi import Query
from pydantic import EmailStr
from ..response import get_response
from ..request import add_customer_model
from ..controller import get_customer_controller, add_customer_controller
from . import customer_api


@customer_api.get("/")
def get_customer(
    customerids: List[int] = Query(None, description="Enter the ids of customer", gt=0),
    customernames: List[str] = Query(None, description="Enter the names of customer"),
    phonenumbers: List[str] = Query(
        None, description="Enter the phone numbers of customer"
    ),
    emails: List[EmailStr] = Query(None, description="Enter the email ids of customer"),
):
    try:
        return get_customer_controller(customerids, customernames, phonenumbers, emails)
    except Exception as e:
        print("get_customer exception : ", e)
        return get_response("CUSTOMER_ERR001", None, 409)


@customer_api.post("/")
def add_customer(customer_details: add_customer_model):
    try:
        return add_customer_controller(customer_details.dict())
    except Exception as e:
        print("add_customer exception : ", e)
        return get_response("CUSTOMER_ERR002", None, 409)
