from fastapi import APIRouter
from models.schemas import WeatherRequest, WeatherResponse
from services.nasa_api import fetch_weather_data

router = APIRouter()

@router.get("/hello")
def say_hello():
    return {"message": "Hello from the Data Router 🌍"}

@router.post("/weather", response_model=WeatherResponse)
def get_weather(request: WeatherRequest):
    return fetch_weather_data(request)
