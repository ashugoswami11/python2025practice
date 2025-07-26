import pygame
from pygame import mixer
mixer.init()
mixer.music.set_volume(0.3)

from log_retrive import logger
from datetime import timedelta, datetime
import time

def water_alert():
    start = datetime.strptime("9:00", "%H:%M")
    end = datetime.strptime("17:00", "%H:%M")
    step = timedelta(minutes = 28)

    time_list_water = []
    while start <= end:
        time_list_water.append(start.strftime("%H:%M"))
        start += step
    return time_list_water

def eyes_alert():
    start = datetime.strptime("9:00", "%H:%M")
    end = datetime.strptime("17:00", "%H:%M")
    step = timedelta(minutes=30)

    time_list_eye = []
    while start <= end:
        time_list_eye.append(start.strftime("%H:%M"))
        start += step
    return time_list_eye

def exercise_alert():
    start = datetime.strptime("9:00", "%H:%M")
    end = datetime.strptime("17:00", "%H:%M")
    step = timedelta(minutes=45)

    time_list_exercise = []
    while start <= end:
        time_list_exercise.append(start.strftime("%H:%M"))
        start += step
    return time_list_exercise

# Precalculate all times
time_list_water = water_alert()
time_list_eye = eyes_alert()
time_list_exercise = exercise_alert()

# Alert queue
alert_queue = []

# Track already triggered alerts to avoid duplicates
triggered_times = set()

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    # Only check alerts if the time is new (not handled already)
    if current_time not in triggered_times:
        triggered_times.add(current_time)

        # Check each alert and queue if time matches
        if current_time in time_list_water:
            alert_queue.append(("Water", "water.mp3", "drank"))
        if current_time in time_list_eye:
            alert_queue.append(("Eyes", "eyes.mp3", "eydone"))
        if current_time in time_list_exercise:
            alert_queue.append(("Exercise", "exercise.mp3", "exdone"))

    # If there are alerts in queue, handle them one by one
    while alert_queue:
        alert_name, file_name, stop_command = alert_queue.pop(0)
        mixer.music.load(file_name)
        while True:
            mixer.music.play()
            print(f"[{alert_name.upper()} ALERT] Please type '{stop_command}' to stop music.")
            user_input = input(">> ").strip().lower()
            if user_input == stop_command:
                logger(stop_command)
                mixer.music.stop()
                print(f"✔ {alert_name} alert handled.")
                break

    # Sleep a bit before checking again
    time.sleep(5)

