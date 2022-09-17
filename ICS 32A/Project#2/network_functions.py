# Eric Trinh / 20091235 / network_functions.py

import socket
import io

def user_inputs() -> (str, int, str):
    '''
    Separately prompts the user to enter a host, a port,
    and a username, which the three are returned in a tuple.
    If the port is not a valid one, the user is prompted
    to entered until there is a valid one. If the username
    is not a valid one, the user is prompted to entered
    until there is a valid one.
    '''
    host = input('Enter an IP address or a hostname\n')
    while True:
        try:
            port = int(input('Enter a port for the server\n'))
            if not port in range(1,65536):
                raise ValueError
        except:
            print('Invalid port')
        else:
            break
    while True:
        user = input('Enter a username with no spaces\n')
        if not ' ' in user:
            break

    return host, port, user

def test_connection(host: str, port: int) -> (bool, socket.socket):
    '''
    Given a host and a port, attempts to establish a connection.
    If the connection fails, returns False and a socket of None,
    but if the connection is not the ConnectFour server, then
    returns False and the socket.
    '''
    valid_hosts = ['circinus-32.ics.uci.edu', '128.195.27.42']
    valid_port = 4444
    c4 = None
    test = True
    try:
        c4 = socket.socket()
        c4.connect((host,port))
    except:
        test = False
    if not(host.lower() in valid_hosts and port == valid_port):
        test = False

    return test, c4


def setup_game(c4: socket.socket, user: str, col: int, row: int) -> (io.TextIOWrapper,io.TextIOWrapper):
    '''
    Given a socket, a string for the username, and two integers for the
    columns and rows, communicates to the server according to the
    I32CFSP protocol and prepares the server for gameplay.
    '''
    c4_input = c4.makefile('r')
    c4_output = c4.makefile('w')
    c4_output.write(f'I32CFSP_HELLO {user}\r\n')
    c4_output.flush()
    nothing = c4_input.readline()
    c4_output.write(f'AI_GAME {col} {row}\r\n')
    c4_output.flush()
    nothing = c4_input.readline()

    return c4_input, c4_output


def write_read_move(c4_input: io.TextIOWrapper, c4_output: io.TextIOWrapper, move: [str]) -> [str]:
    '''
    Given two pseudo file objects and a list of string containing the
    user's move, sends the move to the server and returns the computer's
    move.
    '''
    c4_output.write(f'{move[0]} {move[1]}\r\n')
    c4_output.flush()
    feedback = c4_input.readline()
    comp_move = ''
    if feedback == 'OKAY\n':
        comp_move = c4_input.readline()
        nothing = c4_input.readline()
    elif feedback == 'INVALID\n':
        nothing = c4_input.readline()

    return comp_move.strip('\n').split()
