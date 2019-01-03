import socket
import uuid
from threading import Thread
import json

PORT = 54632


def register_client(client_connection, client_info):
    print "Client %s talking to us from port %d" % client_info
    client_uuid = uuid.uuid4()
    client_connection.send("%s\n" % str(client_uuid))
    client_json = client_connection.recv(1024)
    print "Client sent:", client_json
    client_connection.close()


def main():
    listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listening_socket.bind(("0.0.0.0", PORT))
    listening_socket.listen(5)
    print "Server listening on port %d..." % PORT
    while 1:
        connection, info = listening_socket.accept()
        handle_client = Thread(target=register_client, args=(connection, info))
        handle_client.start()


if __name__ == '__main__':
    main()

