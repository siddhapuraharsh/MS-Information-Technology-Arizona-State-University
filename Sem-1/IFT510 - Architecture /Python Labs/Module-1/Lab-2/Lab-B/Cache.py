## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 08/20/2023

class SimpleCPU:
    def fetch(self):
        return "FETCH INSTRUCTION"

    def decode(self, instruction):
        return "DECODE INSTRUCTION"
    
    def execute(self, instruction):
        return "EXECUTE INSTRUCTION"
    
    def run(self):
        instruction = self.fetch()
        decoded_instruction = self.decode(instruction)
        result = self.execute(decoded_instruction)
        print(result)

cpu = SimpleCPU()
cpu.run()