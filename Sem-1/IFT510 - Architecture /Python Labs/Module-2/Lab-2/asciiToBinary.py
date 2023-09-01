## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 09/01/2023

# Step 1: Input Collection
def get_key_input():
    key = input("Press a key: ")
    if len(key) != 1:
        print("Please press only one key.")
        return get_key_input()
    return key


# Step 2: Processing
def ascii_mapping(key) :
    return ord(key)

def convert_to_binary(ascii_value):
    return bin(ascii_value)[2:]


# Step 3: Output Display
def display_binary(binary_value):
    print(f"Binary representation: {binary_value}")


# Main Program
def main():

    # Simulate key press and get ASCII mapping
    key = get_key_input()
    ascii_val = ascii_mapping(key)
    print(f"ASCII value of '{key}': {ascii_val}")

    # Convert ASCII value to binary
    binary_val = convert_to_binary(ascii_val)

    # Display binary representation
    display_binary(binary_val)

if __name__ == "__main__":
    main()