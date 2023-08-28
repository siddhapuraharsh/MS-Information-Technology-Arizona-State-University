## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 08/20/2023

class Cache:
    def retrieve_data(self, address):
        return f"Data from cache at address {address}"

class RAM:
    def retrieve_data(self, address):
        return f"Data from RAM at address {address}"

class MemoryHierarchy:
    def __init__(self):
        self.cache = Cache()
        self.ram = RAM()

    def get_data(self, address):
        print(self.cache.retrieve_data(address))
        print(self.ram.retrieve_data(address))

memory = MemoryHierarchy()
memory.get_data("0X1234")