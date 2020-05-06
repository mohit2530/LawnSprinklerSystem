
'''
LAWN SPRINKLER SYSTEM
-----------------------


Version 1.0.03

Note

    Water Output Schematics
    -----------------------

    Average Water Output from a Sprinkler System == 1.22 inches / hour

    Average Water required by lawn = 1.3 inches / week

                Weekly Water on the Lawn ( inches )
    Formula =   -------------------------------------
                    Sprinkler Output ( hourly )

    We need to water the lawn  = 1.066 hours = 63.93 minutes in a week. Dividing it equally in 7 days : 9.13 minutes a day.

    Since it is not considered good to water continiously, we are going to split the time throughout the week.


'''

from datetime import datetime
import requests, json, logging, time

def start():

    # for logging purposes only
    loggingValue = enableLogging();
    shouldStartWater = run(datetime);

    if (shouldStartWater != False):
        start_timer = calculateWaterFlow();
        logging.info(shouldStartWater);
        stopMotion = countdown(start_timer);
        return stopMotion;

def countdown(allocatedTime):
    '''
    Countdown timer function.
    Input : The time in seconds

    @return bool : false when the timer ends

    '''

    while allocatedTime:
        mins, secs = divmod(allocatedTime, 60)
        timeformat = '{:02f}:{:02f}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        allocatedTime -= 1
    return False;


def run(datetime):

    validWeatherAndTime = logWeatherAndTime(datetime);

    if (validWeatherAndTime):
        logging.info("Weather Api Successful. The current weather is : " + validWeatherAndTime);
        return validWeatherAndTime;
    logging.error("Weather API data failed... Cannot generate data.");
    return False;

def logWeatherAndTime(datetime):

    city_name = "Worthington";
    fileName = "information.txt";
    currentTime = datetime.today().hour;
    api_key = "59003b2d5fc0527ad0947d7857ed26cb";
    base_url = "http://api.openweathermap.org/data/2.5/weather?";

    if (currentTime >= 5 and currentTime <= 10):
        fetch_url = base_url + "appid=" + api_key + "&q=" + city_name;
        response = requests.get(fetch_url).json();
        currentWeather = response["weather"][0]["main"];
        writeFile = open(fileName, "a");
        timeAndData = datetime.now().strftime("%d/%m/%Y %H:%M:%S " + currentWeather + '\n');
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

def enableLogging():
    '''
    Enable Logging to accomodate default debugging logs. This logs not only will take debugging into considerations, but the info actually will
    retrieve data from the weather application. This information can be used to get idea on whether it rained yesterday or not.
    '''
    logging.basicConfig(filename="loggingFile.log", format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger();
    logger.setLevel(logging.DEBUG);
    return logger;

start();