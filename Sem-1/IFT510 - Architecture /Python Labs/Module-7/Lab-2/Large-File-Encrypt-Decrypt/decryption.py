# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/30/2023

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import secrets

# Load the private key
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())

# Read the encrypted data from the file
with open("longEncryptedData.bin", "rb") as f:
    encrypted_symmetric_key = f.read(256)
    ciphertext = f.read()

# Decrypt the symmetric key with the private key
symmetric_key = private_key.decrypt(
    encrypted_symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

iv = secrets.token_bytes(16)

# Decrypt the data with the symmetric key (AES decryption with GCM mode)
cipher = Cipher(algorithms.AES(symmetric_key), modes.GCM(iv), backend=default_backend())  # Use the same IV you used for encryption
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext)

with open("longDecryptedText.txt", "wb") as f:
    f.write(plaintext)