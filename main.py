#IMPORTS
import requests
import json
import os
from dotenv import load_dotenv

#---------------------------------------------------------------------------------------------------------------------------
#API CREDENTIAL
load_dotenv('.env')

#HTTP REQUESTS
query = {'q' : 'gorey', 'APPID': os.getenv('API_KEY')}
current_weather_url = "https://api.openweathermap.org/data/2.5/weather?"
weather_forecast_url = "https://api.openweathermap.org/data/2.5/forecast?"

#---------------------------------------------------------------------------------------------------------------------------
#FUNCTIONS
#FORMATS THE JSON RESPONSE
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#---------------------------------------------------------------------------------------------------------------------------
#SCRIPT
current_weather_response = requests.get(current_weather_url, params=query)
weather_forecast_response = requests.get(weather_forecast_url, params=query)

# print("Current weather in " + current_weather_response.json()['name'] + ", " + current_weather_response.json()['sys']['country'] + ":")
# jprint(current_weather_response.json()['weather'][0]['description'])

# print("Weather forecast for " + weather_forecast_response.json()['city']['name'] + ", " + weather_forecast_response.json()['city']['country'] + ":")
# jprint(weather_forecast_response.json()['weather'][0]['description'])