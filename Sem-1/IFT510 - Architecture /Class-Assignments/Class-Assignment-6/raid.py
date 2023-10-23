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

# Data structures
disks = [
    [1,2,3,4],  # Disk 1
    [5,6,7,8],  # Disk 2
    [9,10,11,12],  # Disk 3
    [13,14,15,16],  # Disk 4
]
parity_disk_index = 0

# Mutex lock for RAID operations
raid_lock = threading.Lock()

# XOR function for parity calculation
def xor(*args):
    result = 0
    for arg in args:
        result ^= arg
    return result

# Write function
def write_to_raid(data_blocks):
    global parity_disk_index
    parity = xor(*data_blocks)
    with raid_lock:
        for i, block in enumerate(data_blocks):
            disks[i].append(block)
        disks[parity_disk_index].append(parity)
        # Move the parity disk index for the next write
        parity_disk_index = (parity_disk_index + 1) % 4

# Read function
def read_from_raid(stripe_number):
    with raid_lock:
        return [disk[stripe_number] for disk in disks]


# Simulate disk failure
def simulate_disk_failure(disk_number):
    for i in range(len(disks[disk_number])):
        disks[disk_number][i] = -1

# Recover data function
def recover_data(stripe_number, failed_disk_number):
    data = read_from_raid(stripe_number)
    lost_data = xor(*[x for i, x in enumerate(data) if i != failed_disk_number])
    with raid_lock:
        disks[failed_disk_number][stripe_number] = lost_data

def worker(task_queue):
    while True:
        task, args = task_queue.get()
        if task == "write":
            write_to_raid(*args)
        elif task == "read":
            print(f"Stripe {args[0]} data: {read_from_raid(*args)}")
        elif task == "fail":
            simulate_disk_failure(*args)
            print(f"Disk {args[0] + 1} has failed!")
        elif task == "recover":
            recover_data(*args)
            print(f"Data recovered for stripe {args[0]} on Disk {args[1] + 1}!")
        task_queue.task_done()
        return

if __name__ == "__main__":
    task_queue = queue.Queue()
    raid_thread = threading.Thread(target=worker, args=(task_queue,))
    raid_thread.start()

    # Sample tasks
    task_queue.put(("write", ([5, 6, 7],)))
    task_queue.put(("write", ([10, 11, 12],)))
    task_queue.put(("read", (0,)))
    task_queue.put(("fail", (2,)))
    task_queue.put(("read", (1,)))
    task_queue.put(("recover", (1, 2)))
    task_queue.put(("read", (1,)))

    # Wait for all tasks to be done
    task_queue.join()

    # Stop the thread
    raid_thread.join()