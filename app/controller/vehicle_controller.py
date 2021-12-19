from ..database import Vehicle
from ..response import get_response

def get_vehicle_inventory_controller(vehicletypes):
    try:
        vehicle_inventory_filters = []
        if vehicletypes:
            vehicle_inventory_filters.append(Vehicle.vehicletype.in_(vehicletypes))
        vehicle_inventory_details = Vehicle().fetch(vehicle_inventory_filters).all()
        if len(vehicle_inventory_details) == 0:
            return get_response("VEHICLE_ERR002", None, 409)
        return get_response("VEHICLE_RES001", vehicle_inventory_details, 200)
    except Exception:
        raise