import json
from ruamel import yaml
import socket
import logging
from argparse import ArgumentParser
from actions import get_server_actions, resolve
from protocol import validate_request, make_response
from handlers import handle_default_request

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

# logger = logging.getLogger('main')
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler = logging.FileHandler('main.log')
#
# file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.DEBUG)
#
# logger.addHandler(file_handler)
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('main.log', encoding=encoding),
        logging.StreamHandler()
    ]
)

try:
    soc = socket.socket()
    soc.bind((host, port))
    soc.listen(5)
    print(f'Сервер запущен {host}:{port}')
    print('Жду подключения')

    while True:
        client, address = soc.accept()
        b_request = client.recv(buffersize)
        b_response = handle_default_request(b_request)
        client.send(b_response)
        client.close()

except KeyboardInterrupt:
    pass