from ..database import Customer
from ..response import get_response


def get_customer_controller(customerids, customernames, phonenumbers, emails):
    try:
        customer_filters = []
        if customerids:
            customer_filters.append(Customer.customerid.in_(customerids))
        if customernames:
            customer_filters.append(Customer.customername.in_(customernames))
        if phonenumbers:
            customer_filters.append(Customer.phonenumber.in_(phonenumbers))
        if emails:
            customer_filters.append(Customer.email.in_(emails))
        customer_details = Customer().fetch(customer_filters).all()
        if len(customer_details) == 0:
            return get_response("CUSTOMER_ERR003", None, 409)
        return get_response("CUSTOMER_RES001", customer_details, 200)
    except Exception:
        raise


def add_customer_controller(customer_details):
    try:
        add_customer_details = Customer().add(customer_details)
        return get_response("CUSTOMER_RES002", add_customer_details, 200)
    except Exception:
        raise
