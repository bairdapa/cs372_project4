# This is the client application for project 4
# Sources:
# I did not use any online sources for this project, instead opting to reference
# my previous work in this class.

import socket
import sys

# create vars to store host info
HOST = "127.0.0.1"
PORT = 3304

# create the socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server and print info
client_socket.connect((HOST, PORT))
print("connected to: " + HOST + ":" + str(PORT) + "\ntype /q to quit")
    
while 1:
    # prompt for message to send
    client_message = input(">")
    
    # check if the client quits
    if client_message == "/q":
        print("client quitting...")

        # close socket and exit loop
        client_socket.close()
        break
    
    # send request to server
    client_socket.sendall(str.encode(client_message))
    
    # receive and print the server's response
    server_response = client_socket.recv(4096)
    print(server_response.decode())

# close socket and exit
client_socket.close()
sys.exit()
