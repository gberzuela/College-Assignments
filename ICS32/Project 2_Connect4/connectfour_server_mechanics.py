import socket
from collections import namedtuple


ConnectFourSocket = namedtuple(
    'ConnectFourSocket',
    ['socket', 'input', 'output'])


def game_introduction() -> None:
    print('Welcome to Connect Four: Server Edition.\n')
    print('The rules are simple:')
    print('You will play against a Connect 4 AI.')
    print('The first to place four pieces in a row')
    print('(horizontally, vertically, or diagonally) wins.\n')
    print('You will be given the option to either pop one of your own')
    print('pieces from the bottom of the desired column or')
    print('drop a piece into a desired column.\n')
    print('Before we get started: ')
    print('You must provide a valid host and port to play with.\n')


def connecting_interface() -> ConnectFourSocket:
    while True:
        try:
            host = _get_host()
            port = _get_port()
            
            print()
            print(f'Connecting to {host} port {port}...\n')
            
            connectfour_socket = socket.socket()
            connectfour_socket.connect((host, port))
            connectfour_input = connectfour_socket.makefile('r')
            connectfour_output = connectfour_socket.makefile('w')

            print('Connected successfully!\n')
            return ConnectFourSocket(
                socket = connectfour_socket,
                input = connectfour_input,
                output = connectfour_output)

        except TimeoutError:
            print('There was a timeout error. Please provide a valid host and port.\n')


def close_connection(connection: ConnectFourSocket) -> None:
        print('Closing Connection.')
        connection.socket.close()
        connection.input.close()
        connection.output.close()


def send_user_message(connection: ConnectFourSocket, message: str) -> None:
    connection.output.write(message + '\r\n')
    connection.output.flush()


def read_message(connection: ConnectFourSocket) -> '????':
    return connection.input.readline()[:-1]


def _get_host() -> str:
    while True:
        host = input('Host: ').strip()

        if len(host) == 0:
            print('Please specify a host: ')
        else:
            return host


def _get_port() -> int:
    while True:
        try:
            port = int(input('Port: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535.')
            else:
                return port

        except ValueError:
            print('Port must be an integer between 0 and 65535.')


