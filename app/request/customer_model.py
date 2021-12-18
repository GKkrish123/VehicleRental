from pydantic import BaseModel, Field, validator, EmailStr
from ..database import get_session, Customer
import re


class add_customer_model(BaseModel):
    customername: str = Field(
        ..., description="Name of the customer", example="xyz", min_length=3
    )
    phonenumber: str = Field(
        ..., description="Phone number of the customer", example="9191993945"
    )
    email: EmailStr = Field(
        ..., description="Email ID of the customer", example="xyz@gmail.com"
    )

    @validator("email")
    def should_be_valid_email(cls, v):
        try:
            session = get_session()
            data = session.query(Customer).filter(Customer.email == v).first()
            if data == None:
                return v
            raise ValueError("This email is already registered with another customer")
        except ValueError as e:
            raise ValueError(e)

    @validator("phonenumber")
    def should_be_valid_phonenumber(cls, v):
        try:
            if not re.fullmatch("(0|91)?[7-9][0-9]{9}", v):
                raise ValueError("value is not a valid phone number")
            session = get_session()
            data = session.query(Customer).filter(Customer.phonenumber == v).first()
            if data == None:
                return v
            raise ValueError(
                "This phone number is already registered with another customer"
            )
        except ValueError as e:
            raise ValueError(e)
