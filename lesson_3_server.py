from socket import *
import time


s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 8888))
s.listen(5)
pong = 'pong'

while True:
    client, addr = s.accept()
    ping = client.recv(10000)
    if ping.decode('utf-8') == 'ping':
        time.sleep(1)
        client.send(pong.encode('utf-8'))
        print(ping.decode('utf-8'))
    client.close()