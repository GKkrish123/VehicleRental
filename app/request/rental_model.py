from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date, datetime
from ..database import get_session, Customer, Vehicle


class add_rental_booking_model(BaseModel):
    customername: str = Field(..., description="Name of the customer", example="xxx")
    rentaldate: Optional[str] = Field(
        date.today().strftime("%d/%m/%Y"),
        description="Date of rental booking",
        example="dd/mm/yyyy",
    )
    returndate: Optional[str] = Field(
        None, description="Date of return of rental vehicle", example="dd/mm/yyyy"
    )
    vehicletype: str = Field(..., description="Type of vechicle", example="boat")

    @validator("customername")
    def should_be_valid_customer(cls, v):
        try:
            session = get_session()
            data = session.query(Customer).filter(Customer.customername == v).first()
            if data == None:
                raise ValueError("Please add customer details for rental booking")
        except ValueError as e:
            raise ValueError(f"Unregistered customername -> {e}")
        return v

    @validator("rentaldate", "returndate")
    def should_be_valid_date(cls, v):
        try:
            datetime.strptime(v, "%d/%m/%Y")
        except ValueError as e:
            raise ValueError(f"Invalid date -> {e}")
        return v

    @validator("vehicletype")
    def should_be_valid_vehicletype(cls, v):
        try:
            session = get_session()
            data = session.query(Vehicle).filter(Vehicle.vehicletype == v).first()
            if data == None:
                raise ValueError(
                    f"Currently, {v} is not available in our inventory. Please checkout the vehicle availability"
                )
            if data.inventory == 0:
                raise ValueError(
                    f"Currently, {v} cannot be rented as it is already booked"
                )
        except ValueError as e:
            raise ValueError(f"Unavailable vehicletype -> {e}")
        return v
