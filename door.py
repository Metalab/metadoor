#!/usr/bin/python
import RPi.GPIO as GPIO
import socket
import SimpleHTTPServer
import SocketServer
import threading
from threading import Thread

def server():
    PORT = 80

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "Serving at port", PORT
    httpd.serve_forever()

def switch():
    with open("status.json", "w") as f:
        f.write('{ "status" : "boot" }')
        f.close()


    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    input = GPIO.input(18)

    while True:
       GPIO.wait_for_edge(18, GPIO.RISING)
       print('on')
       with open("status.json", "w") as f:
           f.write('{ "status" : "open" }')

       GPIO.wait_for_edge(18, GPIO.FALLING)
       print('off')
       with open("status.json", "w") as f:
           f.write('{ "status" : "closed" }')

    GPIO.cleanup()

if __name__ == '__main__':
    Thread(target = server).start()
    Thread(target = switch).start()




#    sock = socket.socket()
#    sock.connect(('212.47.233.90', 5454))
#    sock.close()
##########
#    sock = socket.socket()
#    sock.connect(('212.47.233.90', 6464))
#    sock.close()
