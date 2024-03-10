## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 10/23/2023

import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '127.0.0.1'  # localhost
port = 12345       # You can choose any available port

server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening on {}:{}".format(host, port))

# Accept connections from clients
client_socket, client_address = server_socket.accept()
print("Accepted connection from {}:{}".format(client_address[0], client_address[1]))

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')

    if not data:
        break

    print("Received from client:", data)

    # Send a response back to the client
    response = "Server received your message: " + data
    client_socket.send(response.encode('utf-8'))

# Close the client socket and server socket
client_socket.close()
server_socket.close()
