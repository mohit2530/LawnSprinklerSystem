
'''
LAWN SPRINKLER SYSTEM
-----------------------


Version 1.0.01 ( Initial Set up and MVP Requirements)

Note:

Certain things that are kept into consideration.

a) Time of the day
b) Weather of the current day.
c) Amount of water that is being consumed.
d) Lawn dryness - default to medium FOR MVP.

'''

from datetime import datetime
import requests, json

def start():
    shouldStartWater = run(datetime);
    if (shouldStartWater != False):
        return True;

def run(datetime):
    startWater = False;
    lawnDryness = "MEDIUM";
    validWeatherAndTime = checkWeathersAndTime(datetime, lawnDryness);
    if (validWeatherAndTime):
        return validWeatherAndTime;
    return False;

def checkWeathersAndTime(datetime, lawnDryness):

    city_name = "Worthington";
    currentTime = datetime.today().hour;
    api_key = "59003b2d5fc0527ad0947d7857ed26cb";
    base_url = "http://api.openweathermap.org/data/2.5/weather?";

    if (currentTime >= 5 and currentTime <= 10):
        fetch_url = base_url + "appid=" + api_key + "&q=" + city_name;
        response = requests.get(fetch_url).json();
        currentWeather = response["weather"][0]["main"];
        return currentWeather;

start();