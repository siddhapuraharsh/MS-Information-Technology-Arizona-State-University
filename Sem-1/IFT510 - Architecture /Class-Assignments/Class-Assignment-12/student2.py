# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

# Student Class Definition
class Student:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def __str__(self):
        return self.name + " " + self.id + " " + self.major

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getMajor(self):
        return self.major

    def setName(self, name):
        self.name = name

    def setId(self, id):
        self.id = id

    def setMajor(self, major):
        self.major = major

# Functions to read and write data from/to a CSV file
def writeDataToCSV(fileName, data):
    import csv
    with open(fileName, "w") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

def readDataFromCSV(fileName):
    import csv
    data = []
    with open(fileName, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Sample data creation
students = [Student("Student" + str(i), "ID" + str(i), "Major" + str(i % 5)) for i in range(20)]
student_data = [[student.getName(), student.getId(), student.getMajor()] for student in students]

# Write data to CSV
writeDataToCSV("students.csv", student_data)

# Read data from CSV
read_data = readDataFromCSV("students.csv")

# Display read data (for demonstration)
for student in read_data:
    print(student)