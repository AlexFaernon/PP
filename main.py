from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class RentCar(BaseModel):
    id: int
    model: str
    isTaken: bool
    pricePerHour: float


rentCars = []


@app.post("/rentCars/", response_model=RentCar)
def add_car(rent_car: RentCar):
    car = [i for i in rentCars if i.id == rent_car.id]
    if len(car) != 0:
        raise HTTPException(status_code=418, detail="Машина с указанным id уже существует")

    rentCars.append(rent_car)
    return rent_car


@app.get("/rentCars/{get_id}", response_model=RentCar)
def get_car(get_id: int):
    car = [i for i in rentCars if i.id == get_id]
    if len(car) == 0:
        raise HTTPException(status_code=404, detail="Машина не найдена")

    return car[0]


@app.get("/rentCars/", response_model=List[RentCar])
def get_all_cars():
    return rentCars


@app.delete("/rentCars/{delete_id}", response_model=RentCar)
def remove_car(delete_id: int):
    car_index = [i for i in range(len(rentCars)) if rentCars[i].id == delete_id]
    if len(car_index) == 0:
        raise HTTPException(status_code=404, detail="Машина не найдена")

    return rentCars.pop(car_index[0])


@app.put("/rentCars/", response_model=RentCar)
def update_car(rent_car: RentCar):
    car_index = [i for i in range(len(rentCars)) if rentCars[i].id == rent_car.id]
    if len(car_index) == 0:
        raise HTTPException(status_code=404, detail="Машина не найдена")
    rentCars[car_index[0]] = rent_car
    return rentCars[car_index[0]]
