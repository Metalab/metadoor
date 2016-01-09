#!/usr/bin/python
import RPi.GPIO as GPIO

with open("status.json", "w") as f:
    f.write('{ "status" : "boot" }')
    f.close()
pinSwitch = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSwitch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
while True:
   GPIO.wait_for_edge(pinSwitch, GPIO.RISING)
   print('on')
   with open("status.json", "w") as f:
       f.write('{ "status" : "open" }')

   GPIO.wait_for_edge(pinSwitch, GPIO.FALLING)
   print('off')
   with open("status.json", "w") as f:
       f.write('{ "status" : "closed" }')
GPIO.cleanup()

