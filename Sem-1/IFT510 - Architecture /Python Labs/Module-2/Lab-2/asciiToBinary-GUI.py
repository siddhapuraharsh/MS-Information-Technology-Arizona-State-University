## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 09/01/2023

import tkinter as tk
from tkinter import messagebox

# Step 1: Input Collection
def get_key_input():
    key = entry.get()
    if len(key) != 1:
        messagebox.showerror("Error", "Please press only one key.")
    else:
        return key
    
# Step 2: Processing
def ascii_mapping(key):
    return ord(key)

def convert_to_binary(ascii_value):
    return bin(ascii_value)[2:]

# Step 3: Output Display
def display_binary(binary_value):
    print(f"Binary representation: {binary_value}")
    binary_label.config(text=f"Binary representation: {binary_value}")

# Main Program
def process_input():
    key = get_key_input()
    if key:
        ascii_val = ascii_mapping(key)
        ascii_label.config(text=f"ASCII value of '{key}': {ascii_val}")
        print(f"ASCII value of '{key}': {ascii_val}")
        binary_val = convert_to_binary(ascii_val)
        display_binary(binary_val)

# Create the main window
root = tk.Tk()
root.title("Binary Converter")
root.configure(bg="yellow")

# Create GUI elements
instruction_label = tk.Label(root, text="Press a key:")
instruction_label.pack()

entry = tk.Entry(root)
entry.pack()

convert_button = tk.Button(root, text="Convert", command=process_input)
convert_button.pack()

ascii_label = tk.Label(root, text="")
ascii_label.pack()

binary_label = tk.Label(root, text="")
binary_label.pack()

# Start the GUI event loop
root.mainloop()