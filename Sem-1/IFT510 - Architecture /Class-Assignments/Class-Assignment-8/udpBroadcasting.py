# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/16/2023

import socket

def broadcast_udp_message(message, port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Enable broadcasting
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Broadcast the message
    udp_socket.sendto(message.encode(), ('<broadcast>', port))
    
    # Close the socket
    udp_socket.close()

if __name__ == "__main__":
    message = "This is a UDP broadcast message"
    port = 12345  # Choose a UDP port for broadcasting
    
    broadcast_udp_message(message, port)
