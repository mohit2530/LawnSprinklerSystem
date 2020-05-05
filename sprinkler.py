
'''
LAWN SPRINKLER SYSTEM
-----------------------


Version 1.0.03

Note

    Water Output Schematics
    -----------------------

    Average Water Output from a Sprinkler System == 1.22 inches / hour

    Average Water required by lawn = 1.3 inches / week

                Weekly Water on the Lawn ( inches )
    Formula =   -------------------------------------
                    Sprinkler Output ( hourly )

    We need to water the lawn  = 1.066 hours = 63.93 minutes in a week. Dividing it equally in 7 days : 9.13 minutes a day.

    Since it is not considered good to water continiously, we are going to split the time throughout the week.


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

def calculateWaterFlow():

    averageWaterOutput = 1.22 # 1.22 inches an hour
    averageWaterRequiredByLawn = 1.3 # 1.3 inches per week. This can vary depending on the grass

    weeklyWaterTheLawn = (averageWaterRequiredByLawn / averageWaterOutput ) * 60 # converting into minutes
    dailyWaterTheLawn = weeklyWaterTheLawn / 7;



start();