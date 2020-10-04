
import pytz;
from client import config;
from datetime import datetime;


def userInformation():

    timeZone  = pytz.timezone(config.timeZone)

    userInformation = {
        "apiKey" : config.key,
        "baseUrl" : config.uri,
        "channel" : config.channel,
        "cityName" : config.cityName,
        "waterTime" : config.waterTime,
        "infoFile" : config.informationFile,
        "currentTime": datetime.now(timeZone)
        }

    return userInformation;
