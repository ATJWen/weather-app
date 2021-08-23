#IMPORTS
import os
from dotenv import load_dotenv
from pyowm.owm import OWM
from pyowm.weatherapi25 import weather
from pyowm.utils import timestamps, formatting
import json

#----------------------------------------------------------------------
#API CREDENTIALS
load_dotenv(".env")
try:
    owm = OWM(os.getenv('API_KEY'))
except:
    print("Unable to connect to OWM")

class Weather:
    def __init__(self,city):
        self.city = city
        self.mgr = owm.weather_manager()
        self.weather = self.mgr.weather_at_place(self.city).weather #CURRENT WEATHER OBJECT
        self.forecast = self.mgr.forecast_at_place(self.city, '3h').forecast #DAILY FORECAST OBJECT EVERY 3HR FOR THE NEXT 5 DAYS

#----------------------------------------------------------------------
    #FUNCTIONS
    def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

#----------------------------------------------------------------------
    #GET CURRENT WEATHER
    #GET CLOUD STATUS
    def get_current_cloud_status(self):
        # print(self.weather.status) #CLOUDS
        # print(self.weather.detailed_status) #DETAILED DESCRIPTION OF CLOUDS
        print(self.weather.rain)
        return self.weather

    #GET MIN-MAX TEMP IN CELSIUS OF THE DAY
    def get_current_temp_info(self):
        temp_dict_celsius = self.weather.temperature('celsius')
        # temp_dict_celsius['temp_min'] #MINIMUM TEMP OF THE DAY
        # temp_dict_celsius['temp_max'] #MAX TEMP OF THE DAY
        # temp_dict_celsius['feels_like'] #CURRENT WEATHER FEEL
        # temp_dict_celsius['temp'] #CURRENT ACTUAL WEATHER
        # print(temp_dict_celsius)
        return temp_dict_celsius

    #GET CURRENT WIND INFO
    def get_current_wind_info(self):
        wind_dict_in_mps = self.weather.wind()
        # wind_dict_in_mps['speed'] #CURRENT WIND SPEED
        # wind_dict_in_mps['deg'] #DIRECTION OF WIND
        # print(wind_dict_in_mps)
        return wind_dict_in_mps

    #GET CURRENT RAIN AMOUNT (MM)
    def get_current_rain_info(self):
        rain = self.weather.rain
        if bool(rain):
            # print(rain)
            return rain['1h'] + "mm"
        else:
            # print("NO RAIN DATA FOR THE PAST HOUR")
            return "NO RAIN DATA FOR THE PAST HOUR"

#---------------------------------------------------------------------
    #FORECASTING
    # def get_forecast_datetime(self):
    #     forecast_date = []
    #     for daily_weather in self.forecast:
    #         # print(formatting.to_ISO8601(daily_weather.ref_time))
    #         forecast_date.append(formatting.to_ISO8601(daily_weather.ref_time))
    #     return forecast_date

    # def get_forecast_status(self):
    #     for daily_weather in self.forecast:
    #         print("STATUS: " + daily_weather.status + ", DETAILED STATUS: " + daily_weather.detailed_status)

    # def get_forecast_temp(self):
    #     for daily_weather in self.forecast:
    #         forecast_temp_celsius = daily_weather.temperature('celsius')
    #         print(forecast_temp_celsius['temp'])

    # def get_forecast_wind(self):
    #     for daily_weather in self.forecast:
    #         print(daily_weather.wnd['speed'])

    # def get_forecast_rain(self):
    #     for daily_weather in self.forecast:
    #         if bool(daily_weather.rain):
    #             print(daily_weather.rain['3h'])
    #         else:
    #             print("NO RAIN")

    # def get_general_forecast(self):
    #     for daily_weather in self.forecast:
    #         print(daily_weather.__dict__)
