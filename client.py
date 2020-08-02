import time
import socket

SERVER_PORT = 55000

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.0.100', SERVER_PORT))
    while True:
        sock.send(b'HELLO')
        data = sock.recv(1024)
        print(data)
        time.sleep(5)

if __name__ == '__main__':
    main()
