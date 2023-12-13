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
import queue

def read_part_of_file(section, q):
    start, end, source_file = section
    with open(source_file, 'r') as f:
        f.seek(start)
        data = f.read(end - start)
        q.put((start, data))

#Consumer function
def write_to_file(dest_file, q):
    items = []
    while True:
        item = q. get()
        if item is None:
            break
        items.append(item)

    items.sort(key=lambda x: x[0])
    with open(dest_file, 'w') as f:
        for _, data in items:
            f.write(data)

if __name__ == "__main__":
    file_size = os.path.getsize('source.txt')
    chunk_size = file_size // 3
    offsets = [(i*chunk_size, (i+1)*chunk_size, 'source.txt') for i in range(3)]

    q = queue.Queue()

    #Start producer threads
    for off in offsets:
        t= threading.Thread(target=read_part_of_file, args=(off, q))
        t.start()
    
    #Start consumer thread
    writer_thread = threading.Thread(target=write_to_file, args=('destination_queue.txt',q))
    writer_thread.start()

    #wait for producer threads to finish
    for off in offsets:
        t.join()

    #Signal consumer thread that all producers are done
    q.put(None)

    #Wait for consumer thread to finish
    writer_thread.join()

    print("Operation completed.")
    
       