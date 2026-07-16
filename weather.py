import requests

from config import API_KEY, BASE_URL, UNITS, LANGUAGE

def format_weather(data: dict) -> dict:
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "min_temp": data["main"]["temp_min"],
        "max_temp": data["main"]["temp_max"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }


def get_weather(city : str,  unit : str = UNITS, language : str = LANGUAGE) -> dict | None:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": unit,
        "lang": language
    }
    try:
        response = requests.get(BASE_URL, params=params)
        if response.ok:
            return format_weather(response.json())
        return None
    except requests.RequestException:
        return None
