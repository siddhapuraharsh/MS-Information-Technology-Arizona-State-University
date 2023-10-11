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

sys.setrecursionlimit(100000)
    
def factorial_iterative(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    if n == 0:
        return 1  # 0! is defined as 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
# Test cases
test_numbers = [0, 1, 4, 5, 100, 1000]
for num in test_numbers:
    print (f"Factorial of {num} is: {factorial_iterative (num)}")