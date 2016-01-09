#!/usr/bin/python
import RPi.GPIO as GPIO
import socket
import SimpleHTTPServer
import SocketServer
import threading
from threading import Thread

def server():
    PORT = 2087

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

    print "Serving at port", PORT
    httpd.serve_forever()

def switch():
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
if __name__ == '__main__':
    Thread(target = server).start()
    Thread(target = switch).start()

