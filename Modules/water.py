import RPi.GPIO as GPIO
 
channel1 = 21
channel2 = 20
channel3 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel1, GPIO.IN)
GPIO.setup(channel2, GPIO.IN)
GPIO.setup(channel3, GPIO.IN)

_sensor = {channel1: False, channel2: False, channel3: False}

def _callback(channel):
    _sensor[channel] = not _sensor[channel]

GPIO.add_event_detect(channel1, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel1, _callback)
GPIO.add_event_detect(channel2, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel2, _callback)
GPIO.add_event_detect(channel3, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel3, _callback)
 
def level():
    if _sensor[channel1]:
        return 100
    if _sensor[channel2]:
        return 66
    if _sensor[channel3]: 
        return 33 
    else:
        return 0
