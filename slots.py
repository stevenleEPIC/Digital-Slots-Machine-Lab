import tm1637
import time
import numpy as np
import random # i guess it works
from gpiozero import Button, LED
from signal import pause
from time import sleep

winner=LED(26)
blue=Button(18) #i hate bouncy buttons and i cant fix that grrr
white=Button(24) #automatic win hehehehehehehebhehhehhe

tm = tm1637.TM1637(clk=27, dio=22)
clear = [0,0,0,0]
tm.write(clear)
tm.show("spin")



def spin():
    a=str(random.randint(0,9))
    b=str(random.randint(0,9))
    r=random.randint(1,4) # 1-4 chooses the location of different number
    s=0

    if white.is_pressed: # winner
        d=1
    else: # normal
        d=0

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
    if a==b or d==1: # a==b is winner, d==1 forces winner
        tm.show(a+a+a+a)
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
    
blue.when_pressed = spin

def retry(): # allows retry without needing to rerun code
    blue.when_pressed = spin


pause()
