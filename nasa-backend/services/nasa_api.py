import requests

BASE_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"

def fetch_nasa_data(lat: float, lon: float, start: str, end: str, variables: str):
    params = {
        "parameters": variables,  # e.g., "T2M,PRECTOTCORR"
        "community": "AG",        # AG = agriculture, CL = climatology
        "longitude": lon,
        "latitude": lat,
        "start": start.replace("-", ""),  # YYYYMMDD
        "end": end.replace("-", ""),
        "format": "JSON"
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()
