from ..database import Rentalbooking, Vehicle
from ..response import get_response


def get_rental_booking_controller(bookingids, customernames, vechicletypes):
    try:
        booking_filters = []
        if bookingids:
            booking_filters.append(Rentalbooking.bookingid.in_(bookingids))
        if customernames:
            booking_filters.append(Rentalbooking.customername.in_(customernames))
        if vechicletypes:
            booking_filters.append(Rentalbooking.vehicletype.in_(vechicletypes))
        rental_booking_details = Rentalbooking().fetch(booking_filters).all()
        if len(rental_booking_details) == 0:
            return get_response("RENTAL_ERR003", None, 409)
        return get_response("RENTAL_RES001", rental_booking_details, 200)
    except Exception:
        raise

def add_rental_booking_controller(rental_booking_details):
    try:
        vehicle_filters = [
            Vehicle.vehicletype == rental_booking_details["vehicletype"]
        ]
        vehicle_update = {
            "inventory": Vehicle.inventory - 1
        }
        Vehicle().edit(vehicle_filters, vehicle_update, session_close=False)
        add_rental_booking_details = Rentalbooking().add(rental_booking_details)
        return get_response("RENTAL_RES002", add_rental_booking_details, 200)
    except Exception:
        raise