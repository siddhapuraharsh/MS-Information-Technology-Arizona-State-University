## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 09/11/2023

import os
import datetime
import getpass

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

class LMC:
    def __init__(self):
        # Memory of size 16 (for the sake of this example)
        self.memory = [0] * 16
        # Accumulator register
        self.accumulator = 0
        # Program counter
        self.pc = 0
        # Output register (just for displaying output)
        self.output = None

    def load_program(self, program):
        # Load the given program into memory
        for i, instruction in enumerate(program):
            self.memory[i] = instruction

    def execute(self):
        while True:
            # Fetch instruction from memory
            instruction = self.memory[self.pc]
            # Increment program counter for the next cycle
            self.pc += 1
            # Decode and execute instruction
            op = instruction // 100
            operand = instruction % 100

            if op == 0:  # LDA
                self.accumulator = self.memory[operand]
            elif op == 1:  # ADD
                self.accumulator += self.memory[operand]
            elif op == 2:  # SUB
                self.accumulator -= self.memory[operand]
            elif op == 3:  # MUL
                self.accumulator *= self.memory[operand]
            elif op == 4:  # OUT
                self.output = self.accumulator
                print(f"Output: {self.output}")
            elif op == 5:  # HLT
                print("Halting...")
                break

if __name__ == '__main__':
    # Define the program
    # LDA 10 (load number from address 10)
    # ADD 11 (add number from address 11)
    # SUB 12 (subtract number from address 12)
    # MUL 13 (multiply by number from address 13)
    # OUT (display result)
    # HLT (halt)
    program = [10, 111, 212, 313, 400, 500]
    # Initialize the LMC and load the program
    computer = LMC()
    computer.load_program(program)
    # Place the numbers to be operated on at memory locations 10, 11, 12, and 13
    computer.memory[10] = 5  # Load 5
    computer.memory[11] = 3  # Add 3
    computer.memory[12] = 2  # Subtract 2
    computer.memory[13] = 4  # Multiply by 4
    # Execute the program
    computer.execute()
