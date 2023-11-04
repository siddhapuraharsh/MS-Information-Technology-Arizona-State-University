# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

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



def writeDataToCSV(fileName, data):
    # Import the CSV module
    import csv
    # Open the file
    file = open(fileName, "w")
    # Write the data to the file
    writer = csv.writer(file)
    # Loop through each row in the data
    for row in data:
        # Write the row to the file
        writer.writerow(row)
    # Close the file
    file.close()
   
#read data from csv file
def readDataFromCSV(fileName):
    # Import the CSV module
    import csv
    # Open the file
    file = open(fileName, "r")
    # Create a list to hold the data
    data = []
    # Read the data from the file
    reader = csv.reader(file)
    # Loop through each row in the file
    for row in reader:
        # Add the row to the data list
        data.append(row)
    # Close the file
    file.close()
    # Return the data
    return data

students = [
    Student("Harsh","1001","Computer Science"),
    Student("Het","1002","IT"),
    Student("Dhruv","1003","IT"),
    Student("Riya","1004","IT"),
    Student("Ramya","1005","IT"),
    Student("Sai","1006","IT"),
    Student("Venkata","1007","IT"),
    Student("Vineetha","1008","IT"),
    Student("Aruna","1009","IT"),
    Student("Div","1010","IT"),
    Student("Smit","1011","IT"),
    Student("Harsh","1012","IT"),
    Student("Piya","1013","IT"),
    Student("Khushi","1014","Computer Science"),
    Student("Drashti","1015","Law"),
    Student("Mancy","1016","Computer Science"),
    Student("Prachi","1017","Computer Science"),
    Student("Het","1018","Computer Science"),
    Student("Dravy","1019","Computer Science"),
    Student("Moksh","1020","Computer Science")
]   

student_data = [[student.getName(), student.getId(), student.getMajor()] for student in students]


writeDataToCSV("students.csv", student_data)


read_data = readDataFromCSV("students.csv")

# Display read data (for demonstration)
for student in read_data:
    print(student)