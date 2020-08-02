import time
import socket
import argparse

from config import MAX_CMD_LEN, CLIENT_CMDS, SERVER_CMDS, DEFAULT_SERVER_PORT
import exceptions


def build_command(cmd_string):
    cmd_string = cmd_string.strip()
    cmd_split = cmd_sting.split()
    cmd_name = cmd_split[0]
    cmd_value = '' if len(cmd_split) == 1 else cmd_split[1]
    cmd_send_string = cmd_name
    if cmd_name not in CLIENT_CMDS:
        raise exceptions.CommandNameException(f'Invalid client command: "{cmd_name}"')
    if cmd_name == 'SET_VOL':
        if not cmd_value:
            raise exceptions.CommandValueException(f'Invalid value: "{cmd_value}" for client command "{cmd_name}"')
        try:
            float(cmd_value)
        except ValueError:
            raise exceptions.CommandValueException(f'Invalid value: "{cmd_value}" for client command "{cmd_name}"')
        cmd_send_string = ' ' + cmd_value
    return bytes(cmd_send_string, encoding='utf-8')


def process_response(sock):
    response_data = sock.recv(MAX_CMD_LEN)
    decoded_response = response_data.decode().strip()
    if decoded_response not in SERVER_CMDS:
        raise exceptions.ServerInvalidResponse('Innvalid response received from server.')
    if decoded_response == 'ERROR':
        raise exceptions.ServerError('Server returned ERROR.')
    elif decoded_response == 'SUCCESS':
        return decoded_response
    else:
        return decoded_response.split()[1]


def main(server_ip, server_port, command):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))
    sock.send(build_command(command))
    response = process_response(sock)
    print(response)
    sock.send(build_command('CLOSE_CONN'))
    response = process_response(sock)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('server-ip', help="Server's IP")
    parser.add_argument('-p', '--server-port', default=DEFAULT_SERVER_PORT, type=int, help="Server's PORT", required=False)
    parser.add_argument('-c', '--cmd', help='Command', required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    main(args.server_ip, args.server_port, args.cmd)
