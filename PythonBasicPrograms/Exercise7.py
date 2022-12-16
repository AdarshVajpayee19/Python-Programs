# HEALTHY PROGRAMMER

# 9-am to 5-pm
# WATER - water.mp3 (3.5 litres) - DRANK - log - Every 30 min
# EYES - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# PHYSICAL ACTIVITY - physical.mp3 - every - 45 min - ExDone - log

# Rules:
# pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    # watersecs = 40*60
    # exsecs = 30*60
    # eyessecs = 45*60

    watersecs = 5
    exsecs = 10
    eyessecs = 20

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3','drank')
            init_water = time()
            log_now("Drank water at ")

        if time() - init_eyes > eyessecs:
            print("Eyes exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3','doneeyes')
            init_eyes = time()
            log_now("Eyes relaxed at ")

        if time() - init_exercise > exsecs:
            print("Physical Activity time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical_activity.mp3','donephy')
            init_exercise = time()
            log_now("Physical Activity done at ")

