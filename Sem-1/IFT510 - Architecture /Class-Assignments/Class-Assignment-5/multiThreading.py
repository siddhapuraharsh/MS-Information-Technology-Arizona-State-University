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

import threading
import time
def threaded_read_part_of_file(section, results):
    start, end, source_file = section
    with open (source_file, 'r') as f:
        f. seek(start)
        data = f. read (end - start)
        results [start] = data
def multi_threaded_read_write(source_file, dest_file):
    file_size = os.path.getsize (source_file)
    chunk_size = file_size // 3

    threads = []
    results = {}
    offsets = [(i*chunk_size, (i+1)*chunk_size, source_file) for i in range (3)]

    for off in offsets:
        t = threading.Thread(target=threaded_read_part_of_file, args=(off, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join ()

    combined_data = sorted (results. items () , key=lambda x: x [0])
    with open (dest_file, 'w') as f:
        for _, data in combined_data:
            f.write(data)

if __name__ == "__main__":
    start_time = time. time()
    multi_threaded_read_write('source.txt', 'destination threaded.txt')
    end_time = time. time ()
    print(f"Multi-threaded duration: {end_time - start_time} seconds.")