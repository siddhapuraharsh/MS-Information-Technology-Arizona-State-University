# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
 
# Generate RSA key pair
key = RSA.generate(2048)

# Sender (Alice) signs the message
message = b"Hello Bob, this message is signed by Alice."
hash_message = SHA256.new(message)
signature = pkcs1_15.new(key).sign(hash_message)

pubKey = key.public_key()
file = open('PUB.SKT','wb')
file.write(pubKey.export_key('PEM'))
file.close()
 
# Receiver (Bob) verifies the signature
verifier = pkcs1_15.new(key.publickey())
try:
    verifier.verify(hash_message, signature)
    print("Digital Signature Verified: Message is Authentic.")
except (ValueError, TypeError):
    print("Digital Signature Verification Failed: Message may have been tampered.")