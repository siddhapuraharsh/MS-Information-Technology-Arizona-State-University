# # Name: Harsh Siddhapura
# # Enrollment No.: 1230169813
# # Date: 10/30/2023

# import os
# import re
# import logging
# from pathlib import Path

# # Configure logging to write to a file
# LOG_FILENAME = 'deletion_log.log'
# logging.basicConfig(level=logging.INFO, filename=LOG_FILENAME, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

# # Define the target extensions and starting names
# TARGET_EXTENSIONS = ('.tmp', '.log', '.bak', '.docx', '.pdf', '.py', '.txt')  # Add or remove extensions as needed
# STARTS_WITH = 'File'  # The pattern the file/folder names should start with

# def delete_matching_files(start_path, dry_run=True):
#     """
#     Deletes files within start_path that have certain extensions and start with a certain name.
#     :param start_path: The directory path to start the search from.
#     :param dry_run: If True, will only print what would be deleted without actually deleting.
#     """
#     for root, dirs, files in os.walk(start_path):
#         # Filter out directories and files based on the criteria
#         dirs[:] = [d for d in dirs if d.startswith(STARTS_WITH)]
#         files = [f for f in files if f.startswith(STARTS_WITH) and f.endswith(TARGET_EXTENSIONS)]

#         # Delete the matched files
#         for file in files:
#             try:
#                 file_path = Path(root) / file
#                 if dry_run:
#                     logging.info(f'Dry run - Would delete: {file_path}')
#                 else:
#                     file_path.unlink()
#                     logging.info(f'Deleted: {file_path}')
#             except Exception as e:
#                 logging.error(f'Error deleting {file_path}: {e}')

#         # Attempt to delete directories if they are empty after file deletion
#         for dir in dirs:
#             try:
#                 dir_path = Path(root) / dir
#                 if dry_run:
#                     if not any(dir_path.iterdir()):
#                         logging.info(f'Dry run - Would delete directory: {dir_path}')
#                     else:
#                         dir_path.rmdir()  # This will only delete empty directories
#                         logging.info(f'Deleted directory: {dir_path}')
#             except OSError as e:
#                 # Directory not empty or other error
#                 logging.error(f'Error deleting directory {dir_path}: {e}')

# # Usage example
# if __name__ == '__main__':
#     base_path = '/Class-Assignment-15/CleanupFolder'
#     delete_matching_files(base_path, dry_run=False)  # Set dry_run to False to actually delete files
#     logging.info(f'Deleted: {base_path}')



import os
import re
import logging
from pathlib import Path

#Configure logging to write to a file
LOG_FILENAME = 'deletion_log.log'
logging.basicConfig(level=logging.INFO, filename=LOG_FILENAME, filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
#Define the target extensions and starting names
TARGET_EXTENSIONS = ('.tmp', '.log', '.bak', '.docx', '.pdf', '.py', '.txt') 
# Add or remove extensions as needed
STARTS_WITH = 'File'
# The pattern the file/folder names should start with

def delete_matching_files(start_path, dry_run=True):
    """
    Deletes files within start_path that have certain extensions and start with a certain name sparam start path: The directory path to start the search from.
    param dry_run: If True, will only print what would be deleted without actually deleting. for root, dirs, files in os.walk(start _path):
    Filter out directories and files based on the criteria
    """
    for root, dirs, files in os.walk(start_path):
        #Filter out directories and files based on the criteria
        dirs[:] = [d for d in dirs if d.startswith(STARTS_WITH)]
        files = [f for f in files if f.startswith(STARTS_WITH) and f.endswith(TARGET_EXTENSIONS)]
        #Delete the matched files 
        for file in files:
            try:
                file_path = Path(root)/file
                if dry_run:
                    logging.info(f'Dry run - Would delete: {file_path}')
                else:
                    file_path.unlink()
                    logging.info(f'Deleted: {file_path}') 
            except Exception as e:
                logging.error(f'Error deleting {file_path}: {e}')
        #Attempt to delete directories if they are empty after file deletion 
        for dir in dirs:
            try:
                dir_path = Path(root) / dir
                if dry_run:
                    if not any(dir_path.iterdir()):
                        logging.info(f'Dry run - Would delete directory: {dir_path}')

                else:
                    dir_path.rmdir() #This will only delete empty directories 
                    logging.info(f'Deleted directory: {dir_path}')
            except OSError as e:
                #Directory not empty or other error
                logging.error(f'Error deleting directory {dir_path}: {e}')

#Usage example
if __name__ == '__main__':
    file_path="Class-Assignment-15\\CleanupFolder"
    logging.info(f'Deleted: {file_path}')
    delete_matching_files(file_path, dry_run=False) #Set dry_run to False to actually delete files