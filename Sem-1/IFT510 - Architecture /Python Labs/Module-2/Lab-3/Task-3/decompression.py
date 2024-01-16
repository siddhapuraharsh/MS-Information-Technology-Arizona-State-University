## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 09/01/2023

import os
import getpass
import datetime
import zipfile

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

def decompress_zip(zip_file, extract_path):
    # Decompress a ZIP file to the specified directory
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def main():
    # Prompt the user to enter the path to the ZIP file to be decompressed
    zip_file = input("Enter the path to the ZIP file to be decompressed: ")

    # Check if the ZIP file exists
    if not os.path.exists(zip_file):
        print("ZIP file not found.")
        return

    # Prompt the user to enter the path for extracting the contents
    extract_path = input("Enter the path for extracting the contents: ")

    # Check if the extraction path exists or create it if not
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    # Decompress the ZIP file
    decompress_zip(zip_file, extract_path)

    # Print a success message
    print("ZIP file extraction successful.")

if __name__ == "__main__":
    main()
