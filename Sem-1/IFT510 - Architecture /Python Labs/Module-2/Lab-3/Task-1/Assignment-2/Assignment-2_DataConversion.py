## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 09/01/2023

import math
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

# Input from the user as a decimal number
decimal_number = float(input("Enter a decimal number: "))

# Convert the decimal number to binary, octal, and hexadecimal representations
binary_representation = bin(int(decimal_number))
octal_representation = oct(int(decimal_number))
hexadecimal_representation = hex(int(decimal_number))

# Separate the integer and fractional parts
integer_part = int(decimal_number)
fractional_part = decimal_number - integer_part

# Convert the fractional part to binary
binary_fractional = ""
while fractional_part > 0:
    fractional_part *= 2
    bit = int(fractional_part)
    binary_fractional += str(bit)
    fractional_part -= bit

# Convert the fractional part to octal and hexadecimal
octal_fractional = ""
hexadecimal_fractional = ""

for _ in range(6):  # Assuming a maximum of 6 digits in fractional part
    fractional_part *= 8  # Use 8 for octal
    digit = int(fractional_part)
    octal_fractional += str(digit)
    fractional_part -= digit

    fractional_part *= 16  # Use 16 for hexadecimal
    digit = int(fractional_part)
    hexadecimal_fractional += str(hex(digit)[2:])  # Convert to hex and remove '0x'
    fractional_part -= digit

print("Binary representation:", str(binary_representation[2:]) + '.' + str(binary_fractional))
print("Octal representation:", str(octal_representation[2:]) + '.' + str(octal_fractional))
print("Hexadecimal representation:", str(hexadecimal_representation[2:]) + '.' + str(hexadecimal_fractional))

# Round the decimal number to a specific number of decimal places
decimal_places = int(input("Enter the number of decimal places to round to: "))
rounded_number = round(decimal_number, decimal_places)
print(f"Rounded to {decimal_places} decimal places:", rounded_number)

# Calculate the square root and cube root of the decimal number
square_root = math.sqrt(decimal_number)
cube_root = decimal_number ** (1/3)

print("Square root:", square_root)
print("Cube root:", cube_root)