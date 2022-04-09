import RPi.GPIO as GPIO
from light import getLight
from time import sleep


LASER = [36,35]
LDR   = [11,12]
Button = 22

GPIO.setup(LASER,GPIO.OUT)

try:
    GPIO.output(LASER,GPIO.HIGH)
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
