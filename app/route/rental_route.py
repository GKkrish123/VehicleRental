from fastapi import Query
from typing import List
from ..response import get_response
from ..controller import get_rental_booking_controller, add_rental_booking_controller
from ..request import add_rental_booking_model
from . import rental_api


@rental_api.get("/")
def get_rental_booking(
    bookingids: List[int] = Query(None, description="Enter the ids of rental booking", gt=0),
    customernames: List[str] = Query(None, description="Enter the names of customer"),
    vechicletypes: List[str] = Query(None, description="Enter the types of vehicle"),
):
    try:
        return get_rental_booking_controller(bookingids, customernames, vechicletypes)
    except Exception as e:
        print("get_rental_booking exception : ", e)
        return get_response("RENTAL_ERR001", None, 409)


@rental_api.post("/")
def add_rental_booking(rental_booking_details: add_rental_booking_model):
    try:
        return add_rental_booking_controller(rental_booking_details.dict())
    except Exception as e:
        print("add_rental_booking exception : ", e)
        return get_response("RENTAL_ERR002", None, 409)
