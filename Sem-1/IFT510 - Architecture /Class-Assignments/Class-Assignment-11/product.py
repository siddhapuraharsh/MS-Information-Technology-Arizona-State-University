# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

##create a product class with Name, price, quantity, unit, brand,corlor and a total function
class Product:
    def __init__(self, name="na", price=0.00, quantity="1", unit=0, brand='na', color='na'):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.unit = unit
        self.brand = brand
        self.color = color

    def __str__(self):
        return self.name + ", " + str(self.price) + ", " + str(self.quantity) + ", " + self.unit + ", " + self.brand + ", " + self.color
 
    def getName(self):
        return self.name

    def getPrice(self):
        if self.price < 0 :
            self.price = self.price * -1
        return self.price

    def getQuantity(self):
        return self.quantity

    def getUnit(self):
        return self.unit

    def getBrand(self):
        return self.brand

    def getColor(self):
        return self.color

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def setQuantity(self, quantity):
        self.quantity = quantity

    def setUnit(self, unit):
        self.unit = unit

    def setBrand(self, brand):
        self.brand = brand

    def setColor(self, color):
        self.color = color

    def getTotal(self):
        return self.getPrice() * self.quantity

    def getTax(self):
        return self.getPrice() * self.quantity * .08

    def getGrandTotal(self):
        return self.getPrice() * self.quantity * (1 + .08)

    def readDataFromCSV(self, fileName):
        # Open the file
        file = open(fileName, "r")
        # Read the data from the file
        data = file.read()
        # Close the file
        file.close()
        # Return the data
        return data

    #Write data to a text file
    def writeDataToCSV(self, fileName, data):
        # Open the file
        file = open(fileName, "w")
        # Write the data to the file
        for item in data:            
            file.write(item+"\n")
        # Close the file
        file.close()


computer = Product("Computer", 1000, -1, "each", "Apple", "white")
print(computer)
print(computer.getTotal())
print(computer.getTax())
print(computer.getGrandTotal())
print(computer.getName())
print(computer.getPrice())
print(computer.getQuantity())
print(computer.getUnit())
print(computer.getBrand())
print(computer.getColor())

# create an itterable list
products = []

# add 20 data sets using the product class
for i in range(20):
    product = Product(f"Computer-{i}", 1000, i, "each", "Apple", "white")
    products.append(str(product))
   
product = Product(f"Computer-{i}", 1000, i, "each", "Apple", "white")
   
# write product data to csv file
product.writeDataToCSV("product.csv", products)

# read product data from csv file
data = product.readDataFromCSV("product.csv")