from pydantic import BaseModel
from typing import Optional

class WeatherRequest(BaseModel):
    location: str
    date: str
    variable: str

class WeatherResponse(BaseModel):
    location: str
    date: str
    variable: str
    value: float
    unit: Optional[str] = None
