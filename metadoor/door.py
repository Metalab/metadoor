#!/usr/bin/python
import RPi.GPIO as GPIO
import time

PinSwitch = 17
DOOR_STATUS_PATH = "/var/www/metadoor/webpage/doorstatus.json"

GPIO.setmode(GPIO.BCM)
GPIO.setup(PinSwitch, GPIO.IN)
input = GPIO.input(PinSwitch)


# boot it up :-)
with open(DOOR_STATUS_PATH, "w") as f:
    f.write('{ "status" : "boot" }')

# Note: 0 is door open, 1 is door closed
# First check bevor going into while loop:
if input == 0:
    print("on @ startup")
    with open(DOOR_STATUS_PATH, "w") as f:
        f.write('{ "status" : "open" }')

else:
    print("off @ startup")
    with open(DOOR_STATUS_PATH, "w") as f:
        f.write('{ "status" : "closed" }')

# While loop with GPIO.wait_for_edge that only triggers when switch is turned
while True:
    GPIO.wait_for_edge(PinSwitch, GPIO.BOTH)
    # Debounce
    time.sleep(0.010)
    input = GPIO.input(PinSwitch)
    if input == 0:
        # print('on in loop')
        with open(STATUS_PATH, "w") as f:
            f.write('{ "status" : "open" }')

    else:
        # print('off in loop')
        with open(STATUS_PATH, "w") as f:
            f.write('{ "status" : "closed" }')

# if we ever come here..
GPIO.cleanup()
