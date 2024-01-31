## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 09/01/2023

import os
import datetime

def print_system_info():
    # Get user data
    os.system('clear') # os.system('clear') for Linux
    username = os.getlogin()
    # Get computer information
    computer_info = os.name
    # Get current date and time
    current_time = datetime.datetime.now()
    # Format log message
    log_message = f"User: {username}\nTime:{current_time}\nComputer Info: {computer_info}"
    # Print log message
    print(log_message)
# Call the function to print the log
print_system_info()

def decimal_to_binary(decimal_num):
    # Convert a decimal number to its binary representation
    binary_repr = bin(decimal_num)[2:]  # Remove '0b' prefix
    return binary_repr

def convert_decimal_to_binary():
    # Convert decimal numbers to binary
    while True:
        user_input = input("Enter a decimal number (q to quit): ")
        if user_input.lower() == 'q':
            break  # Exit the loop if 'q' is entered
        
        try:
            decimal_num = int(user_input)  # Attempt to convert input to integer
            binary_repr = decimal_to_binary(decimal_num)  # Convert to binary
            print(f"Binary representation: {binary_repr}")
        except ValueError:
            print("Invalid input. Please enter a valid decimal number or 'q' to quit.")

convert_decimal_to_binary()