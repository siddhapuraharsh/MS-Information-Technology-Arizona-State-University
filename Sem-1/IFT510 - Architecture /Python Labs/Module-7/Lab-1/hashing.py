# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

import hashlib

def generate_hash(message):
    encodedMessage = message.encode()
    print("Encoded Message:", encodedMessage)
    hash_object = hashlib.sha256(message.encode())
    return hash_object.hexdigest()

# User Input
user_input = input("Enter a message to hash: ")
hash_value = generate_hash(user_input)
print("Hash Value:", hash_value)