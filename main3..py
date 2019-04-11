# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:52:14 2019

@author: Mounika Reddy P
"""

import time
import RPi.GPIO as GPIO

# Section 4
import random
GPIO.setup(3, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

print("Reaction time game")
print("Python project 4")

GPIO.output(3, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
time.sleep(2)
GPIO.output(3, GPIO.LOW)
GPIO.output(13, GPIO.LOW)

print("The green light will stay on for a random amount of time between 1-10s")
print("Then swap to the red light")
print("As soon as it changes hit the switch")
print("We start in 5s")
time.sleep(5)

GPIO.output(3, GPIO.HIGH)
r = random.randint(1, 10)
time.sleep(r)
GPIO.output(3, GPIO.LOW)
GPIO.output(13, GPIO.HIGH)
start = time.time()

try:
    while True:
        if(GPIO.input(12) == 1):
            end = time.time()
            print("You pressed the button")
            elapsed = end - start
            print("And it took" + round(elapsed, 2))
            print("Try to beat that next time")
            GPIO.output(3, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.cleanup()
            break
        else:
            GPIO.output(3, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)

except KeyboardInterrupt:
    print("Game over")
