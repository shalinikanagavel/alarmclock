from tkinter.ttk import *
from tkinter import *
from pygame import mixer
from datetime import datetime
from time import sleep
window = Tk()
window. title("")
window .geometry('350x150')

def sound_alarm():
    mixer.music.load("alarmsound.wav")
    mixer.music.play()
def alarm():


    while True:
        control=1
        alarm_hour="10"
        alarm_min="00"
        alarm_sec="00"
        alarm_period="AM".upper()
        now=datetime.now()
        hour = now.strftime("%I")
        min=now.strftime("%M")
        second = now.strftime("%S")
        period = now. strftime("%p")
        if control == 1:
            if alarm_period==period:
                if alarm_hour==hour:
                    if alarm_min==min:
                        if alarm_sec==second:
                            print("Time to take a break")
                            sound_alarm()
        sleep(1)                       


mixer.init()
sound_alarm()
window.mainloop()