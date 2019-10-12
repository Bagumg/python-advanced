import json
from ruamel import yaml
import socket
import logging
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

logger = logging.getLogger('main')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('main.log')

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

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
                    logger.info()
                except Exception as err:
                    logger.critical(err)
                    response = make_response(request, 500, 'Internal server error')
            else:
                logger.error('404 - Action not found: {}'.format(request))
                response = make_response(request, 404, 'Action not found')
        else:
            logger.error('400 - Wrong request: {}'.format(request))
            response = make_response(request, 400, 'Wrong request')

        s_response = json.dumps(response)
        client.send(s_response.encode(encoding))
        client.close()


except KeyboardInterrupt:
    pass