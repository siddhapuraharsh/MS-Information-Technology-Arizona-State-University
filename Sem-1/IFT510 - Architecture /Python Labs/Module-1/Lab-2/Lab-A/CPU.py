## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 08/20/2023

class CPU:
    def execute(self, instruction):
        print(f"Executing: {instruction}")

class OperatingSystem:
    def run_program(self, program):
        print("OS starting program...")
        cpu = CPU()
        for instruction in program:
            cpu.execute(instruction)

program = ["LOAD A, 5", "ADD B", "STORE C"]
os = OperatingSystem()
os.run_program(program)