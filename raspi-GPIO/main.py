import RPi.GPIO as GPIO
from light import getLight
from time import sleep

LASER = [35,36]
LDR   = [11,12]
Button = 22

GPIO.setup(LASER,GPIO.OUT)
GPIO.setup(Button,GPIO.IN)

try:
    GPIO.output(LASER,GPIO.HIGH)
    HP = 5
    while HP > 0:
        for i in LDR:
            if getLight(i) > 1000:
                HP -= 1
                print(f"{HP}/5")
                sleep(0.1)
                break
        else:
            if not GPIO.input(Button):
                print("YOU WIN")
    print("GAME OVER!")
finally:
    GPIO.cleanup()
