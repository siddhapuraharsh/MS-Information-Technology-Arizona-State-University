# Name: Harsh Siddhapura
# Enrollment No.: 1230169813

import curses
import os
import getpass
import datetime

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
print_system_info()

def numericKeyPresses(key_presses):
    return [char for char in key_presses if char.isnumeric()]

def alphabetsKeyPresses(key_presses):
    return [char for char in key_presses if char.isalpha()]

# Initialize a curses screen
stdscr = curses.initscr()
curses.noecho()  # Disable automatic echoing of keypresses
stdscr.keypad(1)  # Enable keypad mode

# Initialize a list to store key presses
key_presses = []

try:
    stdscr.addstr("Press any keys combination of numeric and non-numeric characters (Press Enter to stop):")
    # stdscr.refresh()

    # Read key presses until Enter Key is pressed
    while True:
        key = stdscr.getch()
        key_presses.append(chr(key))
        if key == 10:  # Enter key
            break

    # Display the recorded key presses
    stdscr.addstr("\nKey presses: " + " ".join(key_presses))
    stdscr.refresh()

    # Display the recorded key presses in a single line without non-numeric characters
    numeric_key_presses = numericKeyPresses(key_presses)
    alphabets_key_presses = alphabetsKeyPresses(key_presses)
    stdscr.addstr("\nOnly numeric characters: " + "".join(numeric_key_presses))
    stdscr.addstr("\nOnly alphabetic characters: " + "".join(alphabets_key_presses))
    stdscr.refresh()
    stdscr.getch()  # Wait for a key press before exiting

finally:
    # Clean up curses
    curses.endwin()