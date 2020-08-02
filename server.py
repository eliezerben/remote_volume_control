import socket

from win_volume import VolumeManager
from config import MAX_CMD_LEN, CLIENT_CMDS, SERVER_CMDS, DEFAULT_SERVER_PORT
import exceptions


def process_request(request_data, vol_manager):
    decoded_request = request_data.decode().strip()
    cmd_split = decoded_request.split()
    cmd_name = cmd_split[0]
    cmd_value = '' if len(cmd_split) == 1 else cmd_split[1]
    response_string = 'SUCCESS'
    if cmd_name not in CLIENT_CMDS:
        raise exceptions.CommandNameException(f'Invalid command received from client: {cmd_name}')

    if cmd_name == 'SET_VOL':
        try:
            vol_value = float(cmd_value)
        except ValueError:
            response_string = 'ERROR'
        vol_manager.set_volume(vol_value)

    elif cmd_name == 'GET_VOL':
        cur_vol_value = vol_manager.get_volume()
        response_string = f'VOL_VAL {cur_vol_value}'

    elif cmd_name == 'MUTE':
        vol_manager.mute(True)

    elif cmd_name == 'UNMUTE':
        vol_manager.mute(False)

    elif cmd_name == 'GET_MUTE':
        mute_value = 1 if vol_manager.get_mute_state() else 0
        response_string = f'MUTE_VAL {mute_value}'

    elif cmd_name == 'CLOSE_CONN':
        response_string = 'CLOSE_CONN'

    return bytes(response_string, encoding='utf-8')


def request_listener(client_socket, vol_manager):
    while True:
        request_data = client_socket.recv(MAX_CMD_LEN)
        response = process_request(request_data, vol_manager)
        if response == b'CLOSE_CONN':
            client_socket.send(b'SUCCESS')
            return
        else:
            client_socket.send(response)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', DEFAULT_SERVER_PORT))
    sock.listen(5)

    vol_manager = VolumeManager()

    while True:
        client_socket, address = sock.accept()
        request_listener(client_socket, vol_manager)


if __name__ == '__main__':
    main()
