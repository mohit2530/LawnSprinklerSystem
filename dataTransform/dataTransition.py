
import requests, json

def logDataInFile(clientInfo):
    
    oddHours = [i for i in range(24) if i % 2 != 0];

    if (clientInfo["currentTime"].hour in oddHours):

        fetch_url = clientInfo["baseUrl"] + "appid=" + clientInfo["apiKey"] + "&q=" + clientInfo["cityName"] + "&units=imperial"
    
    response = requests.get(fetch_url).json();
    currentWeatherData = formatWeatherData(response);

    with open(clientInfo["infoFile"], "a") as writeFile:
        
        timeAndData = clientInfo["currentTime"].strftime('%Y-%m-%d %H:%M:%S') + " " + currentWeatherData["currentCity"] + " " + currentWeatherData["currentWeather"] + " " + currentWeatherData["currentWeatherDescription"] + " " + currentWeatherData["currentTemperature"] + " " + currentWeatherData["currentHumidity"] + " " + currentWeatherData["currentWindSpeed"] + '\n';
        
        writeFile.write(timeAndData);
    
    return currentWeatherData;


def formatWeatherData(payload):

    weatherData = {
        "currentCity" : payload["name"],
        "currentWeather" : payload["weather"][0]["main"],
        "currentWeatherDescription" : payload["weather"][0]["description"],
        "currentTemperature" : str(payload["main"]["temp"]) + " F",
        "currentHumidity" : str(payload["main"]["humidity"]) + " %",
        "currentWindSpeed" : str(payload["wind"]["speed"]) + " MPH"
   }
    
    return weatherData;


def clearLines(fileName):
    lines = 0
    with open(fileName, "r") as file:
        for i, l in enumerate(file):
            pass
    lines = i + 1

    if (lines > 200):
        with open(fileName, "r") as file:
            retreiveAllLines = file.readlines()
        with open(fileName, "w") as writeFile:
            writeFile.writelines(retreiveAllLines[100::]);

