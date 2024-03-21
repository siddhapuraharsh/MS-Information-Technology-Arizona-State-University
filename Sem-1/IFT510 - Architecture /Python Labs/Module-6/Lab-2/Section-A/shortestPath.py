## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 10/23/2023

import os
import getpass
import datetime

def print_system_info():
    # Get user data
    os.system('clear') # os.system('clear') for Linux
    username = getpass.getuser()
    # Get computer information
    computer_info = os.name
    # Get current date and time
    current_time = datetime.datetime.now()
    # Format log message
    log_message = f"User: {username}\nTime:{current_time}\nComputer Info: {computer_info}"
    # Print log message
    print(log_message)
print_system_info()


import sys

# Define the graph using a dictionary of edges and their weights
graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 2, 'E': 6},
    'D': {'E': 1, 'F': 4},
    'E': {'F': 2},
    'F': {}
}

# Implement the Bellman-Ford algorithm
def bellman_ford (graph, source):
    # Step 1: initialize the distance to all nodes to infinity except the source node
    distance = {node: float('infinity') for node in graph}
    distance[source] = 0

    # Step 2: relax edges repeatedly to find the shortest paths
    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                # If the distance to v through u is shorter than the current distance to v, update it
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            if distance[u] + graph[u][v] < distance[v]:
                raise ValueError('Graph contains a negative-weight cycle')
            
    return distance

# Test the program by computing the shortest path routing between node A and node F
try:
    shortest_path = bellman_ford(graph, 'C')
    print('Shortest path routing:', shortest_path)
except ValueError as e:
    print(e)
    sys.exit(1)