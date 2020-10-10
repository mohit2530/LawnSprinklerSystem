import RPi.GPIO as GPIO
import time

channel = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel, GPIO.OUT)


GPIO.output(channel, GPIO.HIGH)

#time.sleep(5)

#GPIO.output(channel, GPIO.LOW)
