# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:35:29 2019

@author: Mounika Reddy P
"""

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.seteariningd(False)
GPIO.setup(5,GPIO.OUT,initial = GPIO.LOW)

while True:
    ## we have declare about the white light   maintain low in above lines
    
    GPIO.output(5,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(5,GPIO.LOW)
    time.sleep(1)
  #####    
#GPIO.setup(5, GPIO.OUT)
#GPIO.output(5, GPIO.HIGH)
#time.sleep(3)
  
  ###the green light will maintain high then out so that it will blink 
  
   GPIO.setup(7, GPIO.OUT)
   GPIO.output(7, GPIO.HIGH)
   ### time is given to green  light  to stop at certain time
   time.sleep(3)
   
   GPIO.setup(3, GPIO.OUT)
   GPIO.output(3, GPIO.HIGH)
   time.sleep(3)
   
   ### the blue light will stop completely 
   GPIO.setup(7, GPIO.OUT)
   time.sleep(1)
  
   GPIO.output(5, GPIO.HIGH)
   time.sleep(1)
   
###after the function all the lights will sleep
   GPIO.cleanup()
