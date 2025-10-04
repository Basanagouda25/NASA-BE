import random
from models.schemas import WeatherRequest, WeatherResponse

def fetch_weather_data(request: WeatherRequest) -> WeatherResponse:
    simulated_value = round(random.uniform(10, 40), 2)
    return WeatherResponse(
        location=request.location,
        date=request.date,
        variable=request.variable,
        value=simulated_value,
        unit="°C" if request.variable == "temperature" else "units"
    )
