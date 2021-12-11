from typing import List
from database.vehicle import Vehicle
from fastapi import Query
from database.db_conn import get_session
from database.rental import Rentalbooking
from response.response import get_response
from request.rental_model import add_rental_booking_model
from router import rental_api

@rental_api.get("/")
def get_rental_booking(
    bookingids: List[int] = Query(None, description="Enter the ids of rental booking",gt=0),
    customernames: List[str] = Query(None, description="Enter the names of customer"),
    vechicletypes: List[str] = Query(None, description="Enter the types of vehicle")
):
    try:
        session = get_session()
        booking_filters = []
        if bookingids:
            booking_filters.append(Rentalbooking.bookingid.in_(bookingids))
        if customernames:
            booking_filters.append(Rentalbooking.customername.in_(customernames))
        if vechicletypes:
            booking_filters.append(Rentalbooking.vehicletype.in_(vechicletypes))
        rental_booking_details = session.query(Rentalbooking).filter(*booking_filters).all()
        if len(rental_booking_details) == 0:
            return get_response("RENTAL_ERR003", None, 409)
        return get_response("RENTAL_RES001", rental_booking_details, 200)
    except Exception as e:
        print("get_rental_booking exception : ", e)
        return get_response("RENTAL_ERR001", None, 409)

@rental_api.post("/")
def add_rental_booking(
    rental_booking_details: add_rental_booking_model
):
    try:
        session = get_session()
        rental_booking_details = rental_booking_details.dict()
        vehicle_inventory = session.query(Vehicle).filter(Vehicle.vehicletype == rental_booking_details["vehicletype"]).first()
        vehicle_inventory.inventory -= 1
        add_rental_booking_details = Rentalbooking(**rental_booking_details)
        session.add(add_rental_booking_details)
        session.commit()
        return get_response("RENTAL_RES002", add_rental_booking_details, 200)
    except Exception as e:
        print("add_rental_booking exception : ", e)
        return get_response("RENTAL_ERR002", None, 409)