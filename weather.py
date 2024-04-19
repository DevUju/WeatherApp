from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Kansas City"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API key")}&units=imperial"
    weather_data = requests.get(request_url).json()
    return weather_data