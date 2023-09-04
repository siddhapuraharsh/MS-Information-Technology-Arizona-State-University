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

# Function to count alphanumeric characters, digits, punctuation marks, and special characters
def count_characters(input_string):
    alphanumeric_count = 0
    digit_count = 0
    punctuation_count = 0
    special_count = 0

    for char in input_string:
        if char.isalpha():
            alphanumeric_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in [',','.','"',"'",':',';','?','/','!','-','(',')','[',']','{','}']:
            punctuation_count += 1
        else:
            special_count += 1

    return alphanumeric_count, digit_count, punctuation_count, special_count

# Input from the user
user_input = input("Enter some input: ")

# Call the function to count characters
alphanumeric, digits, punctuation, special = count_characters(user_input)

# Print the counts for each category
print("Alphanumeric characters:", alphanumeric)
print("Digits:", digits)
print("Punctuation marks:", punctuation)
print("Special characters:", special)