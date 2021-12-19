from fastapi import Query
from typing import List
from ..response import get_response
from ..controller import get_vehicle_inventory_controller
from . import vehicle_api


@vehicle_api.get("/")
def get_vehicle_inventory(
    vehicletypes: List[str] = Query(None, description="Enter the types of vehicle")
):
    try:
        return get_vehicle_inventory_controller(vehicletypes)
    except Exception as e:
        print("get_vehicle_inventory exception : ", e)
        return get_response("VEHICLE_ERR001", None, 409)
