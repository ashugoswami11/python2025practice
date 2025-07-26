#-- working on the water alert
import pygame
from pygame import mixer
mixer.init()
mixer.music.set_volume(0.3)

from log_retrive import logger

from datetime import timedelta, datetime

now = datetime.now()
formatted_now = now.strftime("%H:%M")  #current time

def water_alert():

    day_start = "9:00"
    day_end = "17:00"
    start = datetime.strptime(day_start, "%H:%M")
    end = datetime.strptime(day_end, "%H:%M")

    step = timedelta(minutes=1)

    time_list_water = []
    time_start = start #just taking 9:00 am into different variable so that by accident i won't change the original
    while time_start <= end:
        time_list_water.append(time_start.strftime("%H:%M"))
        time_start = time_start + step

    return time_list_water

def eyes_alert():

    day_start = "9:00"
    day_end = "17:00"
    start = datetime.strptime(day_start, "%H:%M")
    end = datetime.strptime(day_end, "%H:%M")

    step = timedelta(minutes=30)

    time_list_eye = []
    time_start = start #just taking 9:00 am into different variable so that by accident i won't change the original
    while time_start <= end:
        time_list_eye.append(time_start.strftime("%H:%M"))
        time_start = time_start + step

    return time_list_eye


def exercise_alert():

    day_start = "9:00"
    day_end = "17:00"
    start = datetime.strptime(day_start, "%H:%M")
    end = datetime.strptime(day_end, "%H:%M")

    step = timedelta(minutes=45)

    time_list_exercise = []
    time_start = start #just taking 9:00 am into different variable so that by accident i won't change the original
    while time_start <= end:
        time_list_exercise.append(time_start.strftime("%H:%M"))
        time_start = time_start + step

    return time_list_exercise

#---------------------------------
while True:
    now = datetime.now()
    formatted_now = now.strftime("%H:%M")  # current time
    time_list_water =water_alert()
    if formatted_now in time_list_water:
        mixer.music.load("water.mp3")
        while True:
            mixer.music.play()
            print("please write 'drank' to stop music")
            w_input = input().strip().lower()
            if w_input == "drank":
                print("thank you for playing")
                logger("drank")
                mixer.music.stop()
            break


#----------------------------------------------------------

    time_list_eye = eyes_alert()
    if formatted_now in time_list_eye:
        mixer.music.load("eyes.mp3")
        while True:
            mixer.music.play()
            print("please write 'eydone' to stop music")
            e_input = input().strip().lower()
            if e_input == "eydone":
                from log_retrive import logger
                logger("eydone")
                mixer.music.stop()
            break


#-----------------------------------------------------------
    time_list_exercise = exercise_alert()
    if formatted_now in time_list_exercise:
        mixer.music.load("exercise.mp3")
        while True:
            mixer.music.play()
            print("please write 'exdone' to stop music")
            ex_input = input().strip().lower()
            if ex_input == "exdone":
                from log_retrive import logger
                logger("exdone")
                mixer.music.stop()
            break

