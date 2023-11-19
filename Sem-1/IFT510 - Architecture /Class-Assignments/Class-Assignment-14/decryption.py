# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import serialization

 

# Read Private Key from File

with open("private_key.pem", "rb") as f:

    private_key = serialization.load_pem_private_key(

        f.read(),

        password=None,

        backend=default_backend()

    )

 

# Read Encrypted Data

with open("encrypted_data.bin", "rb") as f:

    encrypted_data = f.read()

 

# Decrypt Encrypted Data

decrypted_data = private_key.decrypt(

    encrypted_data,

    padding.OAEP(

        mgf=padding.MGF1(algorithm=hashes.SHA256()),

        algorithm=hashes.SHA256(),

        label=None

    )

)

 

# Save Decrypted Data to File

with open("Untitled.txt", "wb") as f:

    f.write(decrypted_data)