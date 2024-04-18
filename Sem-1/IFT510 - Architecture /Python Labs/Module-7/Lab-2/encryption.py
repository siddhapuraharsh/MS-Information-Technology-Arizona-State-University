# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
 
# Read Public Key from File
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

# Read Plaintext File
with open("plaintext.txt", "rb") as f:
    plaintext = f.read()

# Encrypt Plaintext
encrypted_data = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
 
# Save Encrypted Data to File
with open("encrypted_data.bin", "wb") as f:
    f.write(encrypted_data)