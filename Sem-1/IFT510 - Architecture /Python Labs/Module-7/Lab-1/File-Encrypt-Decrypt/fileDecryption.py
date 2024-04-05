# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Load the RSA public key from 'PUB.SKT'
with open('PUB.SKT', 'rb') as file:
    pubKey_data = file.read()
    pubKey = RSA.import_key(pubKey_data)

# Load the message and signature from 'encryptedMessage.txt'
with open('encryptedMessage.txt', 'rb') as file:
    file_contents = file.read()
    message = file_contents[:-256]  # Extract the message part
    signature = file_contents[-256:]  # Extract the signature part

# Verify the signature
hash_message = SHA256.new(message)
verifier = pkcs1_15.new(pubKey)  # Use the loaded public key

try:
    verifier.verify(hash_message, signature)
    print("Digital Signature Verified: Message is Authentic.")
except (ValueError, TypeError):
    print("Digital Signature Verification Failed: Message may have been tampered.")

# Now 'message' contains the original content of 'input.txt'
with open('decryptedMessage.txt', 'wb') as file:
    file.write(message)
    print("Decrypted message saved to 'decryptedMessage.txt'.")
