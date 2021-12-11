from fastapi import APIRouter

# CREATE API ROUTERS
customer_api = APIRouter(prefix="/customer", tags=["customer"])
rental_api = APIRouter(prefix="/rental", tags=["rental booking"])
vehicle_api = APIRouter(prefix="/vehicle", tags=["vehicle inventory"])
