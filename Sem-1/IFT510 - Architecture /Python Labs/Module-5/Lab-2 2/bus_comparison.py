# Name: Harsh Siddhapura
# Enrollment No.: 1230169813

import os
import getpass
import datetime
import time

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


def simulate_serial_transfer(data_size, transmission_speed):
    start_time = time.time()

    # Calculate the time required for the serial data transfer
    transfer_time = data_size * 8 / transmission_speed

    # Simulate the serial data transfer by sleeping for the calculated time
    time.sleep(transfer_time)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate throughput in bits per second
    throughput = (data_size * 8) / elapsed_time
    return throughput


def simulate_parallel_transfer(data_size, transmission_speed):
    start_time = time.time()

    # Assuming an 8-bit parallel bus, calculate the number of iterations required
    iterations = data_size * 8 / 8  # Divide by 8 bits per iteration

    # Calculate the time required for the parallel data transfer
    transfer_time = iterations / transmission_speed

    # Simulate the parallel data transfer by sleeping for the calculated time
    time.sleep(transfer_time)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate throughput in bits per second
    throughput = (data_size * 8) / elapsed_time
    return throughput


def analyze_results (serial_throughput, parallel_throughput):
    print("Serial Bus Throughput:", serial_throughput, "bits per second")
    print("Parallel Bus Throughput:", parallel_throughput, "bits per second")


# Main program
if __name__ == '__main__':
    for i in range(10):
        data_size = 10**i # size of data to be transferred in bytes
        transmission_speed = 100**i # Transmission speed in bits per second
        
        # Simulate serial data transfer
        serial_throughput = simulate_serial_transfer(data_size, transmission_speed)
        
        # Simulate parallel data transfer
        parallel_throughput = simulate_parallel_transfer(data_size, transmission_speed)
        
        # Analyze and compare the results
        analyze_results (serial_throughput, parallel_throughput)