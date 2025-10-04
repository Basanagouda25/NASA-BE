from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import WeatherRequest, WeatherResponse
from services.nasa_api import fetch_weather_data

app = FastAPI()

# Allow frontend (React) to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for testing, allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Nasa Weather API is running!"}

@app.post("/weather", response_model=WeatherResponse)
def get_weather(request: WeatherRequest):
    return fetch_weather_data(request)
