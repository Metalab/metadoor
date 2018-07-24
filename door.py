#!/usr/bin/python
import RPi.GPIO as GPIO
import time

PinSwitch = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PinSwitch, GPIO.IN)
input = GPIO.input(PinSwitch)

# boot it up :-)
with open("status.json", "w") as f:
    f.write('{ "status" : "boot" }')
    f.close()

# Note: 0 is door open, 1 is door closed
# First check bevor going into while loop:
if input == 0:
	print('on @ startup')
	with open("status.json", "w") as f:
		f.write('{ "status" : "open" }')
                f.close
else:
	print('off @ startup')
	with open("status.json", "w") as f:
		f.write('{ "status" : "closed" }')
                f.close

# While loop with GPIO.wait_for_edge that only triggers when switch is turned
while True:
    GPIO.wait_for_edge(PinSwitch, GPIO.BOTH)
    #Debounce
    time.sleep(.010)
    input = GPIO.input(PinSwitch)
    if input == 0:
        print('on in loop')
        with open("status.json", "w") as f:
            f.write('{ "status" : "open" }')
            f.close
    else:
        print('off in loop')
        with open("status.json", "w") as f:
            f.write('{ "status" : "closed" }')
            f.close

# if we ever come here..
GPIO.cleanup()
