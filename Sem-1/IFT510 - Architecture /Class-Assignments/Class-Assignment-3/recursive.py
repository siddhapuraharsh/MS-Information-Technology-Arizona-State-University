## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 09/01/2023

import os
import datetime
import getpass

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

import sys

def recursive_function():
    if(sys.getrecursionlimit() == 1000):
        return
    return recursive_function()

if __name__ == '__main__':
    print("Recursion Limit: ", sys.getrecursionlimit())
    recursive_function()

