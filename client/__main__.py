import socket
import json
from datetime import datetime

encoding = 'utf-8'
buffersize = 1024
port = 8008
host = 'localhost'

action = input('Укажите нужное действие: ')
data = input('Введите данные: ')


request = {
    'action': action,
    'data': data,
    'time': datetime.now().timestamp()
}

j_request = json.dumps(request)

try:
    soc = socket.socket()
    soc.connect((host, port))
    print('Client started')
    request = {
        'action': action,
        'data': data,
        'time': datetime.now().timestamp()
    }
    s_request = json.dumps(request)
    soc.send(s_request.encode(encoding))
    response = soc.recv(buffersize)
    print(response.decode(encoding))
except KeyboardInterrupt:
    pass