#IMPORTS
from pyowm.weatherapi25 import location
from weather import Weather
from flask import Flask, render_template, request, redirect, url_for

#-------------------------------------------------
app = Flask(__name__)

@app.route('/weather/<city>')
def print_current_weather(city):
    w = Weather(city)
    #pass all information here
    return render_template('weather.html', 
        location = city, 
        cloud_status = str(w.get_current_cloud_status().detailed_status),
        current_temp = str(w.get_current_temp_info()['temp']),
        feel_temp = str(w.get_current_temp_info()['feels_like']),
        wind_speed = str(w.get_current_wind_info()['speed'])
    )

@app.route('/select_location')
def select_location():
    return render_template('index.html')

@app.route('/index',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      selected_location = request.form['selected_location']
      return redirect(url_for('print_current_weather',city = selected_location))
   else:
      return None

if __name__ == '__main__':
    app.run()