## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 11/23/2023

import os
from datetime import datetime

def traverse_directory(folder_path, output_file):
    with open(output_file, "w") as file:
        for root, dirs, files in os.walk(folder_path):
            file.write(f"Folder: {root}\n")
            for directory in dirs:
                directory_path = os.path.join(root, directory)
                folder_name = os.path.basename(directory_path)
                file.write(f" - {folder_name}\n")
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_name = os.path.basename(file_path)
                file_extension = os.path.splitext(file_name)[1]
                file_stats = os.stat(file_path)
                file_size = file_stats.st_size
                file_modified = file_stats.st_mtime
                file_modified_date = datetime.fromtimestamp(file_modified).strftime("%Y-%m-%d %H:%M:%S")
                file.write(f" - {file_name} ({file_extension}) - Size: {file_size} bytes, Modified: {file_modified_date}\n")
            file.write("\n")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to traverse: ")
    output_file = input("Enter the name of the output file: ")
    traverse_directory(folder_path, output_file)
    print("Traversal completed. The results are saved in", output_file)
