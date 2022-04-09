import RPi.GPIO as GPIO
from light import getLight
from time import sleep,time
from math import sqrt
from api import *

def initGame(enableLDR,HP=5):
    TotalLDR = [16,18,15,13,11,12]
    #TotalLDR   = [11,12,13,15,16,18]
    LDR = [TotalLDR[i] for i in range(6) if enableLDR[i]]
    Button = 22
    print("Waited for 3 seconds...")
    average = [0 for i in LDR]

    for i in range(30):
        average = [average[i]+getLight(LDR[i]) for i in range(len(average))]
        #print(i,average)
        sleep(0.1)
    average = [int(i/30) for i in average]
    boundary = [int(i*2) for i in average]
    print("START!",average,boundary)
    try:
        GPIO.setmode(GPIO.BOARD)
        start_time = time()
        GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        lastest_hit = 0
        prev = [0 for i in LDR]
        while (GPIO.input(Button) == 1 or time()-lastest_hit < 1)  and HP > 0:
            result = [getLight(i) for i in LDR]
            crnt = [int(result[i] > boundary[i]) for i in range(len(result))]
            if sum([crnt[i]*prev[i] for i in range(len(LDR))]) > 0:
                HP -= 1
                lastest_hit = time()
                print(f"HP: {HP}/5 {result} | {boundary}")
                if HP == 0:
                    break
            #print(result,boundary)
            prev = [i for i in crnt]
            #print(f"HP: {HP}/5 {result} | {boundary}")
            sleep(0.1)

        if HP <= 0:
            print("GAME OVER")
        else:
            diff_time = time()-start_time
            print(f"YOU WIN (Time Used: {diff_time:.2f} seconds) You Got: {int(HP*1000/sqrt(diff_time))} Points!")
            #while not GPIO.input(Button):
            #    pass
            #sleep(0.2)
    #except:
    #    print("ERROR")
    finally:
        setLaser([0,0,0,0,0,0])
        GPIO.cleanup()
