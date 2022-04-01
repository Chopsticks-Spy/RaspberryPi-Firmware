import RPi.GPIO as GPIO
from time import time,sleep
GPIO.setmode(GPIO.BOARD)

def getLight(ldr):
    try:
        GPIO.setup(ldr,GPIO.OUT)
        GPIO.output(ldr,GPIO.LOW)
        sleep(0.01)
    
        time_start = time()
        GPIO.setup(ldr,GPIO.IN)
        while GPIO.input(ldr) == GPIO.LOW:
            pass
        return int((time()-time_start)*100000)
    except:
        GPIO.cleanup()
        return -1
