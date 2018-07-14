#!/usr/bin/python
import RPi.GPIO as GPIO

PinSwitch = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PinSwitch, GPIO.IN)
input = GPIO.input(PinSwitch)

# boot it up :-)
with open("status.json", "w") as f:
    f.write('{ "status" : "boot" }')
    f.close()
    
# First check bevor going into while loop:
if input == 1:
	print('on')
	with open("status.json", "w") as f:
		f.write('{ "status" : "open" }')
else:
	print('off')
	with open("status.json", "w") as f:
		f.write('{ "status" : "closed" }')

# While loop with GPIO.wait_for_edge that only triggers when switch is turned
while True:
    GPIO.wait_for_edge(PinSwitch, GPIO.BOTH)
    if input == 1:
        print('on')
        with open("status.json", "w") as f:
            f.write('{ "status" : "open" }')
    else:
        print('off')
        with open("status.json", "w") as f:
            f.write('{ "status" : "closed" }')

# if we ever come here..
GPIO.cleanup()
