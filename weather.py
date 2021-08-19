#IMPORTS
import requests
import json
import os
from dotenv import load_dotenv

#---------------------------------------------------------------------------------------------------------------------------
#API CREDENTIAL
load_dotenv('.env')

#HTTP REQUESTS URLS
# query = {'q' : 'Tralee', 'APPID': os.getenv('API_KEY')}
current_weather_url = "https://api.openweathermap.org/data/2.5/weather?"
weather_forecast_url = "https://api.openweathermap.org/data/2.5/forecast?"

#---------------------------------------------------------------------------------------------------------------------------
#CLASS OBJECT
class Weather:

    #ATTRIBUTES
    city = 'Rome'
    country = None
    query = {'q' : city, 'APPID': os.getenv('API_KEY')}
    current_weather_response = None
    weather_forecast_response = None

    #CURRENT WEATHER ATTR
    current_weather = None

    #FORECAST ATTR
    weather_forecast = None


#CONSTRUCTOR
    def __init__(self) -> None:
        pass
#---------------------------------------------------------------------------------------------------------------------------
#FUNCTIONS
    #FORMATS THE JSON RESPONSE
    def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def connect_to_api(self):
        try:
            self.current_weather_response = requests.get(current_weather_url, params=self.query)
            self.weather_forecast_response = requests.get(weather_forecast_url, params=self.query)

        except Exception as e:
            print("UWU")

    #SETTERS AND GETTERS
    def setCurrentWeather(self):
        self.current_weather = self.current_weather_response.json()['weather'][0]['description']                         

    def setWeatherForecast(self):        
        self.weather_forecast = self.weather_forecast_response.json()['weather'][0]['description']                       
    
    def setCountry(self):
        self.country = self.current_weather_response.json()['sys']['country']

    def setCity(self, city):
        self.city = city

    def getCurrentWeather(self):
        return self.current_weather

    def getWeatherForecast(self):
        return self.weather_forecast

    def getCity(self):
        return self.city

    def getCountry(self):
        return self.country

    def getCurrentWeatherResponse(self):
        return self.current_weather_response.json()

#---------------------------------------------------------------------------------------------------------------------------
# weather_forecast_response = requests.get(weather_forecast_url, params=query)
# print("Current weather in " + current_weather_response.json()['name'] + ", " + current_weather_response.json()['sys']['country'] + ":")
# jprint(current_weather_response.json()['weather'][0]['description'])

# print("Weather forecast for " + weather_forecast_response.json()['city']['name'] + ", " + weather_forecast_response.json()['city']['country'] + ":")
# jprint(weather_forecast_response.json()['weather'][0]['description'])
# print(len(weather_forecast_response.json()['list']))