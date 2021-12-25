
from weather import water;
from client import userInfo;
from sendUpdate import readyEmail;
from weather import weatherData;


def mainFunction():
    
    clientInformation = userInfo.userInformation();
    generateWeatherData = weatherData.generateWeather(clientInformation);

    if (generateWeatherData):
        calculateWater = water.waterCalculator();
        calculateTimer = water.countdown(calculateWater, clientInformation["channel"]);
        readyEmail.notify(clientInformation, generateWeatherData);
        return True;

    readyEmail.notify(clientInformation, generateWeatherData);
    return False;


mainFunction()
