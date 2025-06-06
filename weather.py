# weather.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str = "Taichung", lang: str = "zh_tw", units: str = "metric"):
    params = {
        "q": city,
        "appid": API_KEY,
        "lang": lang,
        "units": units
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"API 錯誤：{data.get('message', '未知錯誤')}")

    weather_info = {
        "城市": data["name"],
        "描述": data["weather"][0]["description"],
        "溫度": data["main"]["temp"],
        "體感溫度": data["main"]["feels_like"],
        "濕度": data["main"]["humidity"]
    }
    return weather_info
