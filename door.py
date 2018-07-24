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
    
# First check bevor going into while loop:
#input=GPIO.input(PinSwitch)
#I have no fuckin clue why this is working inverted on startup! - hetti
if input == 0:
	print('on out')
	with open("status.json", "w") as f:
		f.write('{ "status" : "open" }')
                f.close
else:
	print('off out')
	with open("status.json", "w") as f:
		f.write('{ "status" : "closed" }')
                f.close

# While loop with GPIO.wait_for_edge that only triggers when switch is turned
while 1:
    input=GPIO.input(PinSwitch)
    GPIO.wait_for_edge(PinSwitch, GPIO.BOTH)
    #Debounce
    time.sleep(.010)
    if input == True:
        print('on while')
        with open("status.json", "w") as f:
            f.write('{ "status" : "open" }')
            f.close
    else:
        print('off while')
        with open("status.json", "w") as f:
            f.write('{ "status" : "closed" }')
            f.close

# if we ever come here..
GPIO.cleanup()
