# main.py
from weather import get_weather
from emailer import send_weather_email

if __name__ == "__main__":
    info = get_weather("Taichung")
    send_weather_email(info)
