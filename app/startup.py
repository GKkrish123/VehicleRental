import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .route import customer_route, rental_route, vehicle_route, mockdb_route
from .database import create_db_engine, create_db_session

# METADATA TAGS FOR SWAGGER AND DOCS
tags_metadata = [
    {
        "name": "customer",
        "description": "Contains all API's related to customer",
    },
    {
        "name": "rental booking",
        "description": "Contains all API's related to rental booking",
    },
    {
        "name": "vehicle inventory",
        "description": "Contains all API's related to vehicle inventory",
    },
    {
        "name": "mock database",
        "description": "Contains all API's related to mock database",
    },
]

# DESCRIPTION OF APP
app_description = (
    "Consists of **VEHICLE RENTAL APIs** which performs **server-side** operations."
)

# CREATE FASTAPI APP
app = FastAPI(
    title="VEHICLE RENTAL",
    description=app_description,
    version="1.0.0",
    openapi_tags=tags_metadata,
    terms_of_service="https://gokulakrishnan.netlify.app/",
    contact={
        "name": "Gokulakrishnan A",
        "url": "https://gokulakrishnan.netlify.app/",
        "email": "www.krishnan.arulsigamani@gmail.com",
    },
    license_info={
        "name": "FastAPI",
        "url": "https://fastapi.tiangolo.com/",
    },
)

# APPLY MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OPERATIONS ON STARTUP
@app.on_event("startup")
async def startup_event():
    create_db_engine()


# MIDDLEWARE OPERATIONS
@app.middleware("http")
async def set_global_session(request: Request, call_next):
    create_db_session()
    response = await call_next(request)
    return response


# CUSTOM VALIDATION ERROR RESPONSE
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [
        {
            "name": err["loc"][1],
            "location": err["loc"][0],
            "detail": err["msg"],
            "type": err["type"],
        }
        for err in exc.errors()
    ]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"validation_error": errors}),
    )


# INCLUDE ROUTERS
app.include_router(customer_route.customer_api)
app.include_router(rental_route.rental_api)
app.include_router(vehicle_route.vehicle_api)
app.include_router(mockdb_route.mockdb_api)

# APP START
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
