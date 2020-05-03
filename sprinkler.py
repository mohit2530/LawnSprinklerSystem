
'''
LAWN SPRINKLER SYSTEM 
-----------------------


Version 1.0.01 ( Initial Set up and MVP Requirements)

Note: 

Certain things that are kept into consideration.

a) Time of the day
b) Weather of the following two days and the previous two days.
c) Amount of water that is being consumed.
d) Lawn dryness - default to medium FOR MVP.

'''

from datetime import datetime


def start():
    initialPrints = ["Detecting Power ", "Sprinkler System On ", "Water Level Detection Meter Initialized ", "Machine Operational "];
    tickMark = u'\u2713';
    for value in initialPrints:
        print((value + tickMark).encode('utf8'));
    shouldStartWater = run(datetime);
    print(shouldStartWater); # just for printing purposes, QA test ongoing
    return shouldStartWater;

def run(datetime):
    startWater = False;
    lawnDryness = "MEDIUM";
    conditions = checkWeathersAndTime(datetime, lawnDryness);

    conditionO1 = conditions[0];
    conditionO2 = conditions[1];

    if (conditionO1 == True and conditionO2 == True):
        startWater == True;
    return startWater;


def checkWeathersAndTime(datetime, lawnDryness):
    hoursValid = False;
    weatherValid = False;

    upperLimitOfHours = 10;
    lowerLimitOfHours = 5;

    weatherArrays = ["Sunny", "Windy", "Cloudy"];
    noRain = True;

    currentTime = datetime.today().hour;
    currentWeather = "Rainy";

    if ( currentTime >= lowerLimitOfHours and currentTime <= upperLimitOfHours):
        hoursValid = True;
    if ( currentWeather in weatherArrays and lawnDryness == "MEDIUM"):
        weatherValid = True;

    return [hoursValid, weatherValid];


start();