import RPi.GPIO as GPIO
from light import getLight
from time import sleep

LDR   = [11,12,13,15,16,18]
Button = 22

try:
    GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    while True:
        while GPIO.input(Button) == 1:
            pass
        sleep(0.2)
        print("Pressed")
        while not GPIO.input(Button):
            pass
        sleep(0.2)
finally:
    GPIO.cleanup()
