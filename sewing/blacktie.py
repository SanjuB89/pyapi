#!/usr/bin/python3
"""A basic threading example | rzfeeser@alta3.com"""
 
from multiprocessing import Process, current_process
# Make a thread that simulates a NASA count down
# Waits 1 second at the bottom of each loop

import datetime

## Python standard library
import threading
 
## py standard library
import time

dict = {
        "car1": 1,
        "car2": 1.5,
        "car3": 2,
        "car4": 2.5,
        "car5": 1.10,
        "car6": 0.5,
        }
def groundcontrol():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)
def finishTime():
    now = datetime.datetime.now()
    #print("Current date and time: ")
    return (str(now))

def car1(veh1, power):
    for i in range(0,10):
        print(f"******** mile {i} completed by {veh1}")
        time.sleep(power)
    print("------------>>{0} completed the laps at {1}".format(veh1, finishTime()))

def car2(veh2, power):
    for i in range(0,10):
        print(f"######## mile {i} completed by {veh2}")
        time.sleep(power)
    print("------------>>{0} completed the laps at {1}".format(veh2, finishTime()))
def start():
    veh1 = ""
    veh2 = ""
    print("Choose from {}".format(list(dict)))
    while veh1 == "" and veh1.lower() not in dict:
        veh1 = input("Player 1 choose car: ")
    while veh2 == "" and veh2.lower not in dict:
        veh2 = input("Player 2 choose car: ")
    print("Let the race begin")

    power1 =float(dict[veh1])
    power2 =float(dict[veh2])
    mythread = Process(target=car1, args=(veh1, power1,))
    yourthread = Process(target=car2, args=(veh2, power2,))
    mythread.start()
    yourthread.start()
print("")
if __name__ == "__main__": 
    start()


