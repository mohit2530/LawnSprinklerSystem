from weather import water;
from client import userInfo;
from email import setupEmail;
from weather import weatherData;


def mainFunction():
    
    clientInformation = userInfo.userInformation();
    generateWeatherData = weatherData.generateWeather(clientInformation);

    if (generateWeatherData):
        calculateWater = water.waterCalculator();
        calculateTimer = water.countdown(calculateWater, clientInfo["channel"]);
        setupEmail.notify(clientInfo, generateWeatherData);
        return True;

    setupEmail.notify(clientInfo, generateWeatherData);
    return False;


mainFunction()
