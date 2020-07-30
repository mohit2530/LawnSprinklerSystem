
'''
LAWN SPRINKLER SYSTEM
-----------------------

Version 2.00.00

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

from datetime import datetime, timedelta
import requests, json, logging, pytz, time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
channel = 21
GPIO.setup(channel, GPIO.OUT)

def start():
    # for logging purposes only
    fileName = "/home/pi/Desktop/code/LawnSprinklerSystem/loggingFile.log";
    loggingValue = enableLogging(fileName);
    shouldStartWater = run(datetime);

    if (shouldStartWater != False):
        logging.warning("Water is starting.")
        start_timer = calculateWaterFlow();
        if (start_timer):
       		stopMotion = countdown(start_timer); # start water && end it
    else:
        logging.warning("Water has failed to start. Check logs if inconsistencies are detected.");
        return False;

def countdown(allocatedTime):
    '''
    Countdown timer function.
    Input : The time in seconds

    @return bool : false when the timer ends
    '''
    channelOff(21);  # set the relay to on position
    while allocatedTime >= 0:
        mins, secs = divmod(allocatedTime, 60)
        timeformat = '{:02f}:{:02f}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        allocatedTime -= 1
    logging.warning("Water is ending")
    channelOn(21); # set the relay to off
    GPIO.cleanup()
    return False;

def run(datetime):
    city_name = "Worthington";
    timeZone = pytz.timezone('America/New_York')
    currentTime =  datetime.now(timeZone);
    fileName = "/home/pi/Desktop/code/LawnSprinklerSystem/information.txt";

    validWeatherAndTime = logWeatherAndTime(currentTime, city_name, fileName);
    if (validWeatherAndTime):
        logging.info("Weather Api Successful. The current weather is : " + validWeatherAndTime);
    else:
        logging.error("Weather API data failed... Cannot generate data.");

    if ( currentTime.month == 12 and currentTime.day == 31) :
        clearInfoPeriodically(fileName);

    noRainValue = noRain(fileName, currentTime); # retrieve the data from the information.txt file
     # To dictate whether or not the water has to start or stop. Note: runs at 6am in the morning.
    if ( (currentTime.hour == 6) and noRainValue):
        return True;
    return False;

def noRain(fileName, currentTime):
    '''
    noRain function, detects rain from yesterday to the time to execute until today. If rain is detected within the past 24 hours, it will not let the sprinkler start.
    '''
    yesterday = datetime.strftime(currentTime - timedelta(1), '%Y-%m-%d')
    today = datetime.strftime(currentTime, '%Y-%m-%d')
    with open(fileName, "r") as readingFile:
        readFile = readingFile.readlines();
        for line in readFile:
            fields = line.split();
            if ( (fields[0].__contains__(yesterday) or fields[0].__contains__(today) ) and fields[::1].__contains__("Rain")):
                logging.warning("Rain is detected... Within the past 24 hours.")
                return False;
    return True;

def logWeatherAndTime( currentTime, city_name, fileName):

    api_key = "59003b2d5fc0527ad0947d7857ed26cb";
    base_url = "http://api.openweathermap.org/data/2.5/weather?";
    # every odd hour on the clock the weather api would execute its data
    hourlyChecksToMaintain = [i for i in range(24) if i % 2 != 0];

    if (currentTime.hour in hourlyChecksToMaintain):
        fetch_url = base_url + "appid=" + api_key + "&q=" + city_name;
        response = requests.get(fetch_url).json();
        currentWeather = response["weather"][0]["main"];
        with open(fileName, "a") as writeFile:
            timeAndData = currentTime.strftime('%Y-%m-%d %H:%M:%S') + " " + currentWeather + '\n';
            writeFile.write(timeAndData)
        return currentWeather;

def calculateWaterFlow():
    '''
    The average water output and average water required by a lawn are constant values and are averages depending on the grass you use.
    '''
    averageWaterOutput = 1.22 # 1.22 inches an hour
    averageWaterRequiredByLawn = 1.3 # 1.3 inches per week. This can vary depending on the grass

    weeklyWaterTheLawn = (averageWaterRequiredByLawn / averageWaterOutput ) * 60 # converting into minutes
    dailyWaterTheLawn = weeklyWaterTheLawn / 7;
    # returning the value in seconds in order for the timer function to execute its time.
    return dailyWaterTheLawn * 60;

def enableLogging(fileName):
    '''
    Enable Logging to accomodate default debugging logs. This logs not only will take debugging into considerations, but the info actually will retrieve data from the weather application. This information can be used to get idea on whether it rained yesterday or not.
    '''
    logging.basicConfig(filename=fileName, format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger();
    logger.setLevel(logging.DEBUG);
    return logger;


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

def clearInfoPeriodically(fileName):
    '''
    Function to periodically remove the lines from the file so that the file doesn't get too large.
    '''
    lines = 0;
    with open(fileName, "r") as file:
        for i, l in enumerate(file):
            pass
    lines = i + 1;

    if (lines > 200):
        with open(fileName, "r") as file:
            retreiveAllLines = file.readlines();
        with open(fileName, "w") as writeFile:
            writeFile.writelines(retreiveAllLines[100::]);

start();
