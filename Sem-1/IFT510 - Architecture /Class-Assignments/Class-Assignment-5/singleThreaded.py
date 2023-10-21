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

import time

def single_process_read_write(source_file, dest_file):
    with open (source_file, 'r') as f:
        content = f.read()

    with open (dest_file, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    start_time = time.time ()
    single_process_read_write('source.txt', 'destination.txt')
    end_time = time.time ()
    print(f"Single process duration: {end_time - start_time} seconds.")