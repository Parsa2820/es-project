import RPi.GPIO as GPIO
 
channel1 = 21
channel2 = 20
channel3 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel1, GPIO.IN)
GPIO.setup(channel2, GPIO.IN)
GPIO.setup(channel3, GPIO.IN)
 
def level():
    sensor1 = GPIO.input(channel1)
    sensor2 = GPIO.input(channel2)
    sensor3 = GPIO.input(channel3)
    if sensor3:
        return 100
    if sensor2:
        return 66
    if sensor1: 
        return 33 
    else:
        return 0
