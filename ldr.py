import RPi.GPIO as GPIO
from light import getLight
from time import sleep,time

LDR   = [11,12,13,15,16,18]
Button = 22
LIMIT = 600
try:
    start_time = time()
    GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    HP = 5
    lastest_hit = 0
    while (GPIO.input(Button) == 1 or time()-lastest_hit < 1)  and HP > 0:
        result = [getLight(11),getLight(12)]
        if result[0] > LIMIT or result[1] > LIMIT:
            HP -= 1
            lastest_hit = time()
            print(f"HP: {HP}/5 [{result[0]}, {result[1]}]")
            if HP == 0:
                break
        sleep(0.1)
    if HP <= 0:
        print("GAME OVER")
    else:
        print(f"YOU WIN (Time Used: {time()-start_time:.2f} seconds)")
        #while not GPIO.input(Button):
        #    pass
        #sleep(0.2)
except:
    print("ERROR")
finally:
    GPIO.cleanup()
