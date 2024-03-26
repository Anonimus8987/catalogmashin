from fastapi import FastAPI
from cars.car_api import car_router
from database import Base, engine

app = FastAPI(docs_url='/')

app.include_router(car_router)