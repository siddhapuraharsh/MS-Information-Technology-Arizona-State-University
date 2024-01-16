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

def compress_directory(input_dir, output_zip):
    # Compresses a directory into a ZIP file
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, input_dir)
                zipf.write(file_path, arcname)

def main():
    # Prompt the user to enter the path to the directory containing files to be compressed
    input_dir = input("Enter the path to the directory to compress: ")
    
    # Check if the input directory exists
    if not os.path.exists(input_dir):
        print("Directory not found.")
        return
    
    # Prompt the user to enter the path and filename for the output ZIP file
    output_zip = input("Enter the path and filename for the output ZIP file: ")

    # Compress the directory
    compress_directory(input_dir, output_zip)

    # Get file sizes
    original_size = sum(os.path.getsize(os.path.join(root, file)) for root, _, files in os.walk(input_dir) for file in files)
    compressed_size = os.path.getsize(output_zip)

    # Calculate compression ratio
    compression_ratio = (compressed_size / original_size) * 100

    # Display file sizes and compression ratio
    print(f"Original directory size: {original_size} bytes")
    print(f"Compressed ZIP file size: {compressed_size} bytes")
    print(f"Compression ratio: {compression_ratio:.2f}%")

    # Print a success message
    print("Directory compression successful.")

if __name__ == "__main__":
    main()
