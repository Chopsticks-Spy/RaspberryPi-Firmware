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
            if getLight(i) > 15:
                HP -= 1
                print(f"{HP}/5")
                sleep(0.1)
                break
    print("GAME OVER!")
finally:
    GPIO.cleanup()
