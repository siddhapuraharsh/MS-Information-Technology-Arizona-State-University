# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
 
# Generate RSA key pair
key = RSA.generate(2048)

# Load the plaintext from a file
with open('input.txt', 'rb') as file:
    message = file.read()

hash_message = SHA256.new(message)
signature = pkcs1_15.new(key).sign(hash_message)

pubKey = key.public_key()
with open('PUB.SKT', 'wb') as file:
    file.write(pubKey.export_key('PEM'))

# Save the message and signature to an 'encrypt.txt' file
with open('encryptedMessage.txt', 'wb') as file:
    file.write(message)
    file.write(signature)

print("Data is hashed, signed and saved to 'encryptedMessage.txt'")