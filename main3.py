import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Section 3
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) # Blue
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) # Yellow
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # White

while True: # Run forever
    GPIO.output(3, GPIO.HIGH) # Turn on
    time.sleep(1)
    GPIO.output(3, GPIO.LOW)  # Turn off
    GPIO.output(5, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(5, GPIO.LOW)

GPIO.cleanup()

