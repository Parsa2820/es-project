import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO_LED = 12 

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_LED, GPIO.OUT)

def on():
    GPIO.output(GPIO_LED, True)

def off():
    GPIO.output(GPIO_LED, False)
