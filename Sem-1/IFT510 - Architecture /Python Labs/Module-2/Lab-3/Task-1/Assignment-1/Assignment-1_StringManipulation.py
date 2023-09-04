## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 09/01/2023

import os
import datetime

def print_system_info():
    # Get user data
    os.system('clear') # os.system('clear') for Linux
    username = os.getlogin()
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

# Input from the user
user_input = input("Enter a string: ")

# Print the length of the string
length = len(user_input)
print("Length of the string:", length)

# Convert the string to uppercase and lowercase
uppercase = user_input.upper()
lowercase = user_input.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

# Check if the string contains only alphabetic characters
is_alphabetic = user_input.isalpha()
print("Contains only alphabetic characters:", is_alphabetic)

# Replace a specific substring with another substring
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the replacement substring: ")
replaced_string = user_input.replace(old_substring, new_substring)
print("String after replacement:", replaced_string)

# Split the string into a list of words
words = user_input.split()
print("List of words:", words)