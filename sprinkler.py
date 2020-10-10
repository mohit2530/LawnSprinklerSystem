
from weather import water;
from client import userInfo;
from client import clientInfo;
from sendUpdate import readyEmail;
from weather import weatherData;


def mainFunction():
    
    clientInformation = userInfo.userInformation();
    generateWeatherData = weatherData.generateWeather(clientInformation);

    if (generateWeatherData):
        calculateWater = water.waterCalculator();
        calculateTimer = water.countdown(calculateWater, clientInfo["channel"]);
        readyEmail.notify(clientInfo, generateWeatherData);
        return True;

    readyEmail.notify(clientInfo, generateWeatherData);
    return False;


mainFunction()
