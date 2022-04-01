import RPi.GPIO as GPIO
from light import getLight
from time import sleep

LASER = [11,12,13,15,16,18]
LDR   = [33,35,36,37,38,40]

GPIO.setup(LASER,GPIO.OUT)

try:
    GPIO.output(LASER,True)
    HP = 5
    while HP > 0:
        for i in LDR:
            print(getLight(i),end=" ")
        print()
        sleep(1)
except:
    print("-1 "*len(LDR))
    sleep(1)
finally:
    GPIO.cleanup()
