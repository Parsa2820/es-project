from gpiozero import Servo
 
GPIO=17
 
servo = Servo(GPIO)

def open():
    servo.min()

def close():
    servo.max()
