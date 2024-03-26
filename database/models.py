from sqlalchemy import Column, String, Integer, DateTime, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, default=0)
    username = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True)
    password = Column(String)
    city = Column(String)
    birthday = Column(Date)
    profile_photo = Column(String)
    reg_date = Column(DateTime)

    # Связь с таблицей автомобилей
    cars = relationship("Car", back_populates="user")


# Таблица Машин
class Car(Base):
    __tablename__ = 'cars'
    car_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    car_price = Column(Float)
    car_name = Column(String)
    car_company = Column(String)
    car_mileage = Column(Integer)
    car_color = Column(String)
    car_year = Column(Integer)

    user = relationship("User", back_populates="cars")