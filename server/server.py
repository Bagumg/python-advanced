import json
from ruamel import yaml
import socket
from argparse import ArgumentParser
from actions import get_server_actions, resolve
from protocol import validate_request, make_response

get_server_actions()
# parser = ArgumentParser()
# parser.add_argument('-c', '--config', type=str, help='Runs config file')
# args = parser.parse_args()

host = 'localhost'
port = 8008
buffersize = 1024
encoding = 'utf-8'

# if args.config:
#     with open(args.config) as file:
#         config = yaml.load(file, Loader=yaml.Loader)
#         host = config.get('host')
#         port = config.get('port')

try:
    soc = socket.socket()
    soc.bind((host, port))
    soc.listen(5)
    print(f'Сервер запущен {host}:{port}')
    print('Жду подключения')

    while True:
        client, address = soc.accept()
        b_request = client.recv(buffersize)
        request = json.loads(b_request.decode(encoding))

        if validate_request(request):
            action_name = request.get('action')
            controller = resolve(action_name)
            if controller:
                try:
                    response = controller(request)
                except Exception as err:
                    response = make_response(request, 500, 'Internal server error')
            else:
                response = make_response(request, 404, 'Action not found')
        else:
            response = make_response(request, 400, 'Wrong request')
        s_response = json.dumps(response)
        client.send(s_response.encode(encoding))
        client.close()


except KeyboardInterrupt:
    pass