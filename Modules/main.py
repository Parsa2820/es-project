import distance
import servo
import time
import buzzer
import water

CUP_DISTANCE=10

servo.close()

while True:
    d = distance.distance()
    w = water.level()
    print(f'{w=}, {d=}')
    with open('/var/tmp/coleman/API.txt', 'w') as api:
        api.write(f'WLP {w}')
    if d <= CUP_DISTANCE:
        servo.open()
    else:
        servo.close()
    time.sleep(2)
