#speech.py
import threading
import os
import random
from pyttsx3 import init

en = init()


def say(text, speed=150):
    #talk
    en.setProperty('rate', speed)
    en.say(text)
    en.runAndWait()



# import numpy as np [song array]
# TODO: Refactor function to support both W&L
def beep():
    f1=random.randint(500, 1000)
    f2=random.randint(500, 1000)
    os.system("beep -f {f1} -l {f2}".format(f1,f2)) # TODO: Use f string
    

def noise():
    for i in range(10000):
        t = threading.Thread(target=beep)
        t.start()
def make_noise():
    t=threading.Thread(target=noise)
    t.start()
