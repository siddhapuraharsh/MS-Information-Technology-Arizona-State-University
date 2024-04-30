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

# Generate or load RSA key pair
private_key = None
public_key = None

try:
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())
except FileNotFoundError:
    # Generate new keys if not found
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key = private_key.public_key()
    
    with open("private_key.pem", "wb") as key_file:
        key_file.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()))
    with open("public_key.pem", "wb") as key_file:
        key_file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))

# Read Plaintext File
with open("longPlaintext.txt", "rb") as f:
    plaintext = f.read()

# Generate a symmetric key for data encryption
symmetric_key = secrets.token_bytes(32)  # You'll need to import the 'secrets' module
iv = secrets.token_bytes(16)

# Encrypt data with the symmetric key (AES encryption)
cipher = Cipher(algorithms.AES(symmetric_key), modes.GCM(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Encrypt the symmetric key with the public key
encrypted_symmetric_key = public_key.encrypt(
    symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save Encrypted Data and Encrypted Symmetric Key to Files
with open("longEncryptedData.bin", "wb") as f:
    f.write(encrypted_symmetric_key)
    f.write(ciphertext)
