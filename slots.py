import tm1637
import time
import numpy as np
import random # i guess it works
from gpiozero import Button, LED
from signal import pause
from time import sleep

winner=LED(26)
button=Button(18) #i hate bouncy buttons and i cant fix that grrr

tm = tm1637.TM1637(clk=27, dio=22)
clear = [0,0,0,0]
tm.write(clear)
tm.show("spin")

def spin(): # THIS GAME IS RIGGED
    a=str(random.randint(0,9))
    b=str(random.randint(0,9))
    r=random.randint(1,4) # 1-4 chooses the location of different number
    s=0
    while s<35: #spin animation thing or idk.
        sleep(0.02)
        s+=1
        j=str(random.randint(0,9))
        k=str(random.randint(0,9))
        l=str(random.randint(0,9))
        m=str(random.randint(0,9))
        tm.show(j+k+l+m)
    if r==1:
        tm.show(b+a+a+a)
    if r==2:
        tm.show(a+b+a+a)
    if r==3:
        tm.show(a+a+b+a)
    if r==4:
        tm.show(a+a+a+b)
    if a==b: #OMG YOU WON
        print("you won!!!")
        w=0
        while w<5:
            w+=1
            winner.on()
            tm.brightness(0) #no the screen is not broken 
            sleep(0.5)
            winner.off()
            tm.brightness(7)
            sleep(0.5)
    else:
        print("you lost, press button to spin again")
    sleep(1) #cooldown before spinning again
    retry
    
button.when_pressed = spin

def retry(): # allows retry without needing to rerun code
    button.when_pressed = spin


pause()
