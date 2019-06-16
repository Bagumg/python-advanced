from socket import *
import time

ping = 'ping'

while True:
    time.sleep(1)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8888))
    s.send(ping.encode('utf-8'))
    pong = s.recv(10000)
    if pong.decode('utf-8') == 'pong':
        print(pong.decode('utf-8'))
    s.close()