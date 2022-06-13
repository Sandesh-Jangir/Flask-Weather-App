import requests
import json
from flask import Flask, render_template, redirect, request

# Variables
humidity = ""
temperature= ""
time_zone = ""
clouds = ""

app = Flask(__name__)

@app.route("/getweather", methods=['GET', 'POST'])
def getWeather():
    if request.method == 'POST':
        # Importing Global Variables
        global humidity
        global temperature
        global time_zone
        global clouds
        global error_occured
        error_occured = False
        
        try:
            # Fetching latitude and longitude from the User
            latitude = int(request.form['lat'])
            longitude = int(request.form['lon'])
            # Fetching data from the api
            api_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}.44&lon={longitude}.04&exclude=hourly,daily&appid=98f3a2dc3ba15d13d4a2d1b821f319eb"

            # Transforming fetched data into JSONified data
            data = requests.get(api_url).text
            jsonified_data = json.loads(data)
            
            # Fetching weather data of current time
            current_weather_data = jsonified_data['current']

            humidity = current_weather_data['humidity']
            temperature = current_weather_data['temp']
            time_zone = jsonified_data['timezone']
            clouds = current_weather_data['clouds']

        except ValueError as error:
            error_occured = True
    
    return redirect('/')

@app.route("/")
def Main():
    # Importing Global Variables
    global humidity
    global temperature
    global time_zone
    global clouds
    global error_occured
    temperature_in_celcius = ""

    if temperature == "":
        pass
    else:
        # Converting Temperature to Celcius
        temperature_in_celcius = round(int(temperature) - 273.15, 0)
    # Rendering HTML file and props
    return render_template("Main.html", props=[temperature_in_celcius, humidity, clouds, time_zone, error_occured])

if __name__ == "__main__":
    app.run(debug=True)
