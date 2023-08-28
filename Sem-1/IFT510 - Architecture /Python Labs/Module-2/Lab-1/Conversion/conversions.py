## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 08/20/2023

# Decimal to Binary Conversion

# Step 1: Get the decimal number as input from the user
decimal_num = int(input("Enter a decimal number: "))

# Step 2: Create an empty list to store the binary digits
binary_digits = []

# Step 3: Perform the decimal to binary conversion
while decimal_num > 0:
    remainder = decimal_num % 2
    binary_digits.append(remainder)
    decimal_num //= 2

# Step 4: Reverse the order of binary digits
binary_digits.reverse()

# Step 5: Convert the binary digits list to a string
binary_str = ''.join(str(digit) for digit in binary_digits)

# Step 6: Print the binary representation of the decimal number
print("Binary representation:", binary_str)


# Binary to Decimal Conversion

# Step 1: Get the binary number as input from the user
binary_str = input("Enter a binary number: ")

# Step 2: Calculate the decimal value of the binary number
decimal_num = 0
power = len(binary_str) - 1

for digit in binary_str:
    decimal_num += int(digit) * (2 ** power)
    power -= 1

# Step 3: Print the decimal value of the binary number
print ("Decimal representation:", decimal_num)