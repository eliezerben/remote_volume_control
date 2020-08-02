from enum import Enum

DEFAULT_SERVER_PORT = 55000

MAX_CMD_LEN = 200


CLIENT_CMDS = [
    'SET_VOL',
    'GET_VOL',
    'MUTE',
    'UNMUTE',
    'GET_MUTE',
    'CLOSE_CONN',
]

SERVER_CMDS = [
    'ERROR',
    'SUCCESS',
    'VOL_VAL',
    'MUTE_VAL',
]