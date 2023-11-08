# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return (nonce, ciphertext, tag)

# User Input
user_input = input("Enter a message to encrypt: ")
key = get_random_bytes(16)  # 16 bytes key for AES-128
nonce, ciphertext, tag = encrypt_message(user_input, key)

print("Encrypted Message:", ciphertext)
print("Encryption Key:", key)