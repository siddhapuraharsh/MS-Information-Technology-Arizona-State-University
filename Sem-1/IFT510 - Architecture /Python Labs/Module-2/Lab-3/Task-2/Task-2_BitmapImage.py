## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 09/01/2023

import os
import datetime

def print_system_info():
    # Get user data
    os.system('clear') # os.system('clear') for Linux
    username = os.getlogin()
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

import os
from PIL import Image

def process_bitmap_image(image_path):
    # Load the image
    image = Image.open(image_path)
    width, height = image.size

    # Convert to grayscale
    grayscale_image = image.convert("L")
    grayscale_image.save("grayscale_image.bmp")

    # Resize to half dimensions
    resized_image = image.resize((width // 2, height // 2))
    resized_image.save("resized_image.bmp")

    # Display dimensions
    gray_width, gray_height = grayscale_image.size
    resize_width, resize_height = resized_image.size
    print("Original image dimensions:", width, "x", height)
    print("Grayscale image dimensions:", gray_width, "x", gray_height)
    print("Resized image dimensions:", resize_width, "x", resize_height)

    # Total number of pixels
    print("Original image pixels:", width * height)
    print("Grayscale image pixels:", gray_width * gray_height)
    print("Resized image pixels:", resize_width * resize_height)

    # Compare file sizes
    original_size = os.path.getsize(image_path)
    grayscale_size = os.path.getsize("grayscale_image.bmp")
    resized_size = os.path.getsize("resized_image.bmp")
    print("File sizes:")
    print("Original image size:", original_size, "bytes")
    print("Grayscale image size:", grayscale_size, "bytes")
    print("Resized image size:", resized_size, "bytes")

    # Display images
    image.show(title="Original Image")
    grayscale_image.show(title="Grayscale Image")
    resized_image.show(title="Resized Image")

image_path = input("Enter the path to the bitmap image: ")
process_bitmap_image(image_path)