
'''
LAWN SPRINKLER SYSTEM
-----------------------

Version 2.00.01

    Water Output Schematics
    -----------------------

    Average Water Output from a Sprinkler System == 1.22 inches / hour
    Average Water required by lawn = 1.3 inches / week

                Weekly Water on the Lawn ( inches )
    Formula =   -------------------------------------
                    Sprinkler Output ( hourly )

    We need to water the lawn  = 1.066 hours = 63.93 minutes in a week. Dividing it equally in 7 days : 9.13 minutes a day.

    Since it is not considered good to water continiously, we are going to split the time throughout the week.
    Water only starts at 6am by default.

'''

import config
import RPi.GPIO as GPIO
import requests, json, logging, pytz, time

from send_email import send_thread
from datetime import datetime, timedelta

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def start():

    timeZone  = pytz.timezone(config.timeZone)

    userInformation = {
        "apiKey" : config.key,
        "baseUrl" : config.uri,
        "cityName" : config.cityName,
        "logFile" : config.loggingFile,
        "infoFile" : config.informationFile,
        "currentTime": datetime.now(timeZone)
        }

    loggingValue = enableLogging(userInformation["logFile"])
    weatherData = run(userInformation)

    if (weatherData != False):
        logging.warning("Water is starting.")
        start_timer = calculateWaterFlow()
        if (start_timer):
            stopMotion = countdown(start_timer, channel) # start water && end it
            # signal to send email
            setupThread(userInformation["currentTime"], weatherData)
    else:
        logging.warning("Water has failed to start. Check logs if inconsistencies are detected.")
        return False

def countdown(allocatedTime, channel):
    '''
    Countdown timer function.
    Input : The time in seconds

    @return bool : false when the timer ends
    '''
    GPIO.setup(channel, GPIO.OUT)
    channelOff(channel)  # set the relay to on position
    while allocatedTime >= 0:
        mins, secs = divmod(allocatedTime, 60)
        timeformat = '{:02f}:{:02f}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        allocatedTime -= 1
    logging.warning("Water is ending")
    channelOn(channel) # set the relay to off
    GPIO.cleanup()
    return False

def setupThread(currentTime, weatherObject):
    '''
    Setting up the email parameters to send to the customer. Data is generated from the Weather API at the time of the sprinkler movement.
    '''
    subject = "Lawn Sprinkler System Notification"
    msg = "Current Time : {} \n City : {} \n Weather : {} \n Description : {} \n\n Current Temperature : {} \n Current Humidity : {} \n Current Wind Speed : {} \n\n".format(currentTime.strftime('%Y-%m-%d %H:%M:%S'),  weatherObject["currentCity"], weatherObject["currentWeather"], weatherObject["currentWeatherDescription"], weatherObject["currentTemperature"], weatherObject["currentHumidity"], weatherObject["currentWindSpeed"])
    message = 'Subject: {}\n\n {}'.format(subject, msg)
    return sendEmail(subject, message)

def sendEmail(subject, message="Failure to attach message"):
   '''
   Send Email function to send the email to the recepient labelled in the config file.
   '''
   send_thread(subject, message)

def run(userInformation):

    validWeatherAndTime = logWeatherAndTime(userInformation)

    if (validWeatherAndTime):
        logging.info("Weather Api Successful. The current weather is : " + validWeatherAndTime["currentWeather"])
    else:
        logging.error("Weather API data failed... Cannot generate data.")

    # Every month on the 15th, the files are cleared and logs are destroyed.
    monthlyChecks = [i for i in range(13)]
    if ( (userInformation["currentTime"].month in monthlyChecks) and userInformation["currentTime"].day == 15) :
        clearLines(fileName)

    noRainValue = noRain(userInformation["infoFile"], userInformation["currentTime"])

    # To dictate whether or not the water has to start or stop. Note: runs at 6am in the morning.
    if ((userInformation["currentTime"].hour == 7) and noRainValue):
        return validWeatherAndTime
    return False

def noRain(fileName, currentTime):
    '''
    noRain function, detects rain from yesterday to the time to execute until today. If rain is detected within the past 24 hours, it will not let the sprinkler start.
    '''
    yesterday = datetime.strftime(currentTime - timedelta(1), '%Y-%m-%d')
    today = datetime.strftime(currentTime, '%Y-%m-%d')
    with open(fileName, "r") as readingFile:
        readFile = readingFile.readlines()
        for line in readFile:
            fields = line.split()
            if ( (fields[0].__contains__(yesterday) or fields[0].__contains__(today) ) and fields[::1].__contains__("Rain")):
                logging.warning("Rain is detected... Within the past 24 hours.")
                return False
    return True

def logWeatherAndTime(userInformation):

    # every odd hour on the clock the weather api would execute its data
    hourlyChecksToMaintain = [i for i in range(24) if i % 2 != 0]

    if (userInformation["currentTime"].hour in hourlyChecksToMaintain):
        fetch_url = userInformation["baseUrl"] + "appid=" + userInformation["apiKey"] + "&q=" + userInformation["cityName"] + "&units=imperial"
        response = requests.get(fetch_url).json()

        currentWeatherData = retrieveCurrentWeatherCharacteristics(response)

        with open(userInformation["infoFile"], "a") as writeFile:
            timeAndData = userInformation["currentTime"].strftime('%Y-%m-%d %H:%M:%S') + " " + currentWeatherData["currentWeather"] + '\n'
            writeFile.write(timeAndData)
        return currentWeatherData


def retrieveCurrentWeatherCharacteristics(response):
   '''
   Method to retrieve the current weather characteristics.
   '''
   weatherData = {
	"currentCity" : response["name"],
	"currentWeather" : response["weather"][0]["main"],
	"currentWeatherDescription" : response["weather"][0]["description"],
	"currentTemperature" : str(response["main"]["temp"]) + " F",
	"currentHumidity" : str(response["main"]["humidity"]) + " %",
	"currentWindSpeed" : str(response["wind"]["speed"]) + " MPH"
   }
   return weatherData


def calculateWaterFlow():
    '''
    The average water output and average water required by a lawn are constant values and are averages depending on the grass you use.
    '''
    averageWaterOutput = 1.22 # 1.22 inches an hour
    averageWaterRequiredByLawn = 1.3 # 1.3 inches per week. This can vary depending on the grass

    weeklyWaterTheLawn = (averageWaterRequiredByLawn / averageWaterOutput ) * 60 # converting into minutes
    dailyWaterTheLawn = weeklyWaterTheLawn / 7
    # returning the value in seconds in order for the timer function to execute its time.
    return dailyWaterTheLawn * 60

def enableLogging(fileName):
    '''
    Enable Logging to accomodate default debugging logs. This logs not only will take debugging into considerations, but the info actually will retrieve data from the weather application. This information can be used to get idea on whether it rained yesterday or not.
    '''
    logging.basicConfig(filename=fileName, format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger


def channelOn(pin):
    '''
    Function to read the pin number and set it to high
    '''
    GPIO.output(pin, GPIO.HIGH)

def channelOff(pin):
    '''
    Function to read the pin number and set it to low
    '''
    GPIO.output(pin, GPIO.LOW)

def clearLines(fileName):
    '''
    Function to periodically remove the lines from the file so that the file doesn't get too large.
    '''
    lines = 0
    with open(fileName, "r") as file:
        for i, l in enumerate(file):
            pass
    lines = i + 1

    if (lines > 200):
        with open(fileName, "r") as file:
            retreiveAllLines = file.readlines()
        with open(fileName, "w") as writeFile:
            writeFile.writelines(retreiveAllLines[100::])

start()
