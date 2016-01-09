#!/usr/bin/python
import RPi.GPIO as GPIO

PinSwitch = 17
with open("status.json", "w") as f:
    f.write('{ "status" : "boot" }')
    f.close()
while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PinSwitch, GPIO.IN)
    input = GPIO.input(PinSwitch)
    GPIO.wait_for_edge(PinSwitch, GPIO.BOTH)
    if input == 1:
        print('on')
        with open("status.json", "w") as f:
            f.write('{ "status" : "open" }')
    else:
        print('off')
        with open("status.json", "w") as f:
            f.write('{ "status" : "closed" }')
    GPIO.cleanup()

