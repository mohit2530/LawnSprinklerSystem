
import smtplib;
from client import password;
from client import clientInfo;

def notify(clientInfo, weatherObject):

    if (clientInfo["waterTime"] == clientInfo["currentTime"]):
        generateEmail(clientInfo, weatherObject);
    
    return False;


def generateEmail(clientInfo, weatherObject = {"error" : "Rain was detected within 24 hours."} ):

    subject = "Lawn Sprinkler System Notification"

    if (bool(weatherObject) == True):

        msg = "Current Time : {} \n City : {} \n Weather : {} \n Description : {} \n\n Current Temperature : {} \n Current Humidity : {} \n Current Wind Speed : {} \n\n".format(clientInfo["currentTime"].strftime('%Y-%m-%d %H:%M:%S'),  weatherObject["currentCity"], weatherObject["currentWeather"], weatherObject["currentWeatherDescription"], weatherObject["currentTemperature"], weatherObject["currentHumidity"], weatherObject["currentWindSpeed"])
        message = 'Subject: {}\n\n {}'.format(subject, msg)

        return sendMail(subject, message);

    message = 'Subject: {}\n\n {}'.format(subject, weatherObject["error"]);
    
    return sendMail(subject, message);


def sendMail(subject, msg):
    
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()

        server.login(config.FROM, password.PASSWORD)
        message = 'Subject: {}\n\n {}'.format(subject, msg)
        server.sendmail(config.FROM, config.TO, message)
        server.quit()
        print("Message sent succesfully.")
    
    except:
        print("Failure to send email.")
