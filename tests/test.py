from dotenv.main import load_dotenv
import requests
import dotenv
import os

load_dotenv('.env')
current_weather_url = "https://api.openweathermap.org/data/2.5/weather?"

#Happy path - valid location
def test_real_location():
    query = {'q' : 'Tralee', 'APPID': os.getenv('API_KEY')}
    response = requests.get(current_weather_url, query)
    assert response.status_code == 200

#Negative - fake location
def test_fake_location():
    query = {'q' : 'AAAAAAAAAAAA', 'APPID': os.getenv('API_KEY')}
    response = requests.get(current_weather_url, query)
    assert response.status_code == 404