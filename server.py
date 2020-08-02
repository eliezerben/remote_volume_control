import socket


PORT = 55000

def process_requests(client_socket):
    while True:
        data = client_socket.recv(1024)
        print('Recieved Data:', data)
        client_socket.send(b'Hi from Server.')

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', PORT))
    sock.listen(5)

    while True:
        client_socket, address = sock.accept()
        process_requests(client_socket)

if __name__ == '__main__':
    main()
