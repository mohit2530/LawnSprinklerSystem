from weather import water;
from client import userInfo;
from email import setupThread;
from weather import weatherData;


def mainFunction():
    
    clientInformation = userInfo.userInformation();
    generateWeatherData = weatherData.generateWeather(clientInformation);

    if (generateWeatherData):
        calculateWater = water.waterCalculator();
        calculateTimer = water.countdown(calculateWater, clientInfo["channel"]);
        setupThread.notify(clientInfo, generateWeatherData);
        return True;

    setupThread.notify(clientInfo, generateWeatherData);
    return False;


mainFunction()
