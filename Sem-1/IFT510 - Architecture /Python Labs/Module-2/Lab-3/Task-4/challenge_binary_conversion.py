## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 09/01/2023

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
# Call the function to print the log
print_system_info()

def decimal_to_binary(decimal_num):
    # Convert a decimal number to its binary representation
    binary_repr = bin(decimal_num)[2:]  # Convert to binary and remove '0b' prefix
    return binary_repr

def binary_to_decimal(binary_str):
    # Convert a binary string to its decimal representation
    try:
        decimal_num = int(binary_str, 2)
        return decimal_num
    except ValueError:
        return None

def convert_decimal_to_binary():
    # Convert decimal numbers to binary and vice versa
    while True:
        decimal_user_input = input("Enter a decimal number to convert to binary (q to quit): ")
        if decimal_user_input.lower() == 'q': break

        binary_user_input = input("Enter a binary number to convert to decimal (q to quit): ")
        if binary_user_input.lower() == 'q': break

        try:
            decimal_num = int(decimal_user_input)  # Attempt to convert input to integer
            if decimal_num >= 0:
                binary_repr = decimal_to_binary(decimal_num)  # Convert to binary
                print(f"Binary representation: {binary_repr}")
                if all(bit in '01' for bit in binary_user_input):  # Check if input is a binary number
                    decimal_num = binary_to_decimal(binary_user_input)
                    if decimal_num is not None:
                        print(f"Decimal representation: {decimal_num}")
                else:
                    print("Invalid binary input. Please enter a valid binary number or 'q' to quit.")
            else:
                print("Negative decimal numbers are not supported. Please enter a non-negative decimal number.")
        except ValueError:
            print("Invalid input. Please enter a valid decimal, or 'q' to quit.")

# Start the program by calling convert_decimal_to_binary
convert_decimal_to_binary()