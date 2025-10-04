from fastapi import APIRouter
from services.nasa_api import fetch_nasa_data

router = APIRouter()

@router.get("/data")
def get_weather_data(lat: float, lon: float, start: str, end: str, variables: str):
    data = fetch_nasa_data(lat, lon, start, end, variables)
    return data
