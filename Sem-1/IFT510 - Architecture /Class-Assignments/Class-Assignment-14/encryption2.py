# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023


from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives import serialization

 

# Generate Private Key

private_key = rsa.generate_private_key(

    public_exponent=65537,

    key_size=2048,

    backend=default_backend()

)

 

# Save Private Key to File

with open("private_key.pem", "wb") as f:

    f.write(private_key.private_bytes(

        encoding=serialization.Encoding.PEM,

        format=serialization.PrivateFormat.PKCS8,

        encryption_algorithm=serialization.NoEncryption()

    ))

 

# Generate Public Key from Private Key

public_key = private_key.public_key()

 

# Save Public Key to File

with open("public_key.pem", "wb") as f:

    f.write(public_key.public_bytes(

        encoding=serialization.Encoding.PEM,

        format=serialization.PublicFormat.SubjectPublicKeyInfo

    ))

 