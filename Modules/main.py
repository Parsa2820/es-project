import distance
import servo
import time

CUP_DISTANCE=10

servo.close()

while True:
    d = distance.distance()
    print(d)
    if d <= CUP_DISTANCE:
        servo.open()
    else:
        servo.close()
    time.sleep(2)
