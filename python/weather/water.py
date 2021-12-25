
import RPi.GPIO as GPIO;

def waterCalculator():

    averageWaterOutput = 1.22 # 1.22 inches an hour
    averageWaterRequiredByLawn = 2.0 # 2.0 inches per week. This can vary depending on the grass

    weeklyWaterTheLawn = (averageWaterRequiredByLawn / averageWaterOutput ) * 60 # converting into minutes
    dailyWaterTheLawn = weeklyWaterTheLawn / 7

    return dailyWaterTheLawn * 60


def countdown(timerStart, channel):

    GPIO.setup(channel, GPIO.OUT);
    
    toggle(channel, True)  # set the relay to on position

    while allocatedTime >= 0:
        mins, secs = divmod(allocatedTime, 60)
        timeformat = '{:02f}:{:02f}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        allocatedTime -= 1

    toggle(channel) # set the relay to off
    GPIO.cleanup()

    return False


def toggle(channel, mode=False):
    if (mode):
        GPIO.output(channel, GPIO.LOW);
        return;

    GPIO.output(channel, GPIO.HIGH);