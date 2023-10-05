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

import psutil

def get_process_memory_info():
    # Get a list of all running processes
    processes = psutil.process_iter(attrs=['pid', 'name', 'memory_info'])

    # print the header
    print(f"{'PID':<10}{'Process Name':<50}{'RSS (MB)':<10}{'VMS (MB)':<10}")
    print("="*80)

    for process in processes:
        pid = process.info['pid']
        name = process.info['name']
        mem_info = process.info['memory_info']
        
        # Check if mem_info is not None before accessing its attributes
        if mem_info is not None:
            rss_mem = mem_info.rss / (1024 * 1024)
            vms_mem = mem_info.vms / (1024 * 1024)
            print(f"{pid:<10}{name:<50}{rss_mem:<10.2f}{vms_mem:<10.2f}")
        else:
            # Handle the case where memory_info is None (optional)
            print(f"{pid:<10}{name:<50}{'N/A':<10}{'N/A':<10}")

if __name__ == "__main__":
    get_process_memory_info()