import requests
import json
from flask import Flask, render_template, redirect, request

# Variables
Humidity = ""
Temperature= ""
TimeZone = ""
Clouds = ""

app = Flask(__name__)

@app.route("/getweather", methods=['GET', 'POST'])
def getWeather():
    if request.method == 'POST':
        global Humidity
        global Temperature
        global TimeZone
        global Clouds

        latitude = int(request.form['lat'])
        longitude = int(request.form['lon'])

        apiurl = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}.44&lon={longitude}.04&exclude=hourly,daily&appid=98f3a2dc3ba15d13d4a2d1b821f319eb"
        
        data = requests.get(apiurl).text
        JsonData = json.loads(data)

        CurrentData = JsonData['current']

        Humidity = CurrentData['humidity']
        Temperature = CurrentData['temp']
        TimeZone = JsonData['timezone']
        Clouds = CurrentData['clouds']

    
    return redirect('/')

@app.route("/")
def Home():
    global Humidity
    global Temperature
    global TimeZone
    global Clouds
    CelTemp = ""

    if Temperature == "":
        pass
    else:
        CelTemp = round(int(Temperature) - 273.15, 0)

    return render_template("Main.html", props=[CelTemp, Humidity, Clouds, TimeZone])

if __name__ == "__main__":
    app.run(debug=True)