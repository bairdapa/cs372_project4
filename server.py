# This is the server application for project 4

import socket
import sys

# create vars to store host info
HOST = "127.0.0.1"
PORT = 3304

# create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket
server_socket.bind((HOST, PORT))

# print info
print("created server on " + HOST + ":" + str(PORT))

# listen for incoming connections
server_socket.listen(5)

# loop to process requests as they come in
while 1:
    # accept a connection and store client info
    (client_socket, client_address) = server_socket.accept()

    # print info of client who just connected
    print("client connected: " + str(address) + "\n")

    # read the message the client sent
    client_message = client_socket.recv(4096)

    # print the received message
    print(str(address) + " says:")
    print(client_message)

    # prompt for a reply
    server_reply = input("\nwhat should the server say back?")

    # check for quit command
    if server_reply == "/q":
        # close socket and exit loop
        client_socket.close()
        break

    # send reply
    client_socket.sendall(server_reply)

    # close socket to end connection
    client_socket.close()
        
# close server socket
server_socket.close()

# quit server
sys.exit()
