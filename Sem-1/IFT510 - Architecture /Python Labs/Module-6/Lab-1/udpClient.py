## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 10/23/2023

import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'  # Server's IP address (localhost in this case)
port = 12345       # The same port as used by the server

client_socket.connect((host, port))

while True:
    message = input("Enter a message to send to the server (type 'exit' to quit): ")
    
    if message.lower() == 'exit':
        break
    
    # Send the message to the server
    client_socket.send(message.encode('utf-8'))

    # Receive the server's response
    response = client_socket.recv(1024).decode('utf-8')
    print("Server response:", response)

# Close the client socket
client_socket.close()


