import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city_name):
    """
    Fetch weather info from OpenWeatherMap API
    """
    if not WEATHER_API_KEY:
        return "Weather API key not set."
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={WEATHER_API_KEY}"
    response = requests.get(url).json()
    
    if response.get("cod") != 200:
        return "Weather info not available."
    
    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"]
    return f"{temp}°C, {desc}"
