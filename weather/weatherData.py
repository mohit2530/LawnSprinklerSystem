
from dataTransform import dataTransition;
from datetime import datetime, timedelta;

def generateWeather(clientInfo):

    generateLogs = dataTransition.logDataInFile(clientInfo);

    monthlyChecks = [i for i in range(13)];
    clearLocalSave(clientInfo, monthlyChecks);

    hintsOfRain = checkForRain(clientInfo);
    
    if (hintsOfRain and clientInfo["waterTime"]):
        return generateLogs;


def matchDayAndTime(clientInfo):
    return (clientInfo["currentTime"].day == 15 and clientInfo["currentTime"].hour == clientInfo["waterTime"]);


def clearLocalSave(clientInfo, deleteSaveDates):

    if (clientInfo["currentTime"].month in deleteSaveDates and matchDayAndTime(clientInfo)):
        clearLines(clientInfo["infoFile"]);
        clearLines(clientInfo["logFile"]);

    return;

def checkForRain(clientInfo):

    today = datetime.strftime(clientInfo["currentTime"], '%Y-%m-%d');
    yesterday = datetime.strftime(clientInfo["currentTime"] - timedelta(1), '%Y-%m-%d');

    with open(clientInfo["infoFile"], "r") as readingFile:
        readFile = readingFile.readlines()
        for line in readFile:
            fields = line.split()
            if ( (fields[0].__contains__(yesterday) or fields[0].__contains__(today) ) and (fields[3:4].__contains__("Rain") or fields[3:4].__contains__("Thunderstorm")):
                return True;
    return False;
