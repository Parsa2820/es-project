import distance
import servo
import time
import buzzer
import water
import led

CUP_DISTANCE=10

servo.close()

while True:
    d = distance.distance()
    w = water.level()
    print(f'{w=}, {d=}')
    with open('/var/tmp/coleman/API.txt', 'w+') as api:
        api.write(f'WLP {w}\n')
    activate = d <= CUP_DISTANCE
    empty = w == 0
    if empty:
        servo.close()
        led.on()
        if activate:
            buzzer.buzz()
        else:
            pass
    else:
        led.off()
        if activate:
            servo.open()
        else:
            servo.close()
    time.sleep(2)
