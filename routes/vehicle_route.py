from typing import List
from fastapi import Query
from database.db_conn import get_session
from database.vehicle import Vehicle
from response.response import get_response
from router import vehicle_api


@vehicle_api.get("/")
def get_vehicle_inventory(
    vehicletypes: List[str] = Query(None, description="Enter the types of vehicle")
):
    try:
        session = get_session()
        vehicle_inventory_filters = []
        if vehicletypes:
            vehicle_inventory_filters.append(Vehicle.vehicletype.in_(vehicletypes))
        vehicle_inventory_details = (
            session.query(Vehicle).filter(*vehicle_inventory_filters).all()
        )
        if len(vehicle_inventory_details) == 0:
            return get_response("VEHICLE_ERR002", None, 409)
        return get_response("VEHICLE_RES001", vehicle_inventory_details, 200)
    except Exception as e:
        print("get_vehicle_inventory exception : ", e)
        return get_response("VEHICLE_ERR001", None, 409)
