import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO_BUZZER = 27 

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_BUZZER, GPIO.OUT)

def buzz():
    for _ in range(0, 3):
        GPIO.output(GPIO_BUZZER, True)
        time.sleep(0.1)
        GPIO.output(GPIO_BUZZER, False)
        time.sleep(0.1)
