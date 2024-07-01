from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

# Simulating a database of email addresses and associated public/private keys
database = {
    "harsh@example.com": {
        "public_key": None,
        "private_key": None,
    },
    "asu@example.com": {
        "public_key": None,
        "private_key": None,
    },
}

# Generate public and private keys for each email address
for email, keys in database.items():
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048
    )
    keys["private_key"] = private_key
    keys["public_key"] = private_key.public_key()

def show_dialog(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show a dialog box
    messagebox.showinfo(title, message)

def encrypt_message(recipient_email, subject, message):
    # Intermediate processing dialog
    show_dialog("Intermediate Processing", "Encrypting message...")

    # Simulate sending an email
    if recipient_email in database:
        recipient_public_key = database[recipient_email]["public_key"]
        if recipient_public_key:
            # Encrypt the subject and message with the recipient's public key
            cipherSubject = recipient_public_key.encrypt(
                subject.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            cipherMessage = recipient_public_key.encrypt(
                message.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )

            # Encryption dialog
            show_dialog("Encryption", f"Encrypted Subject: {cipherSubject.hex()}\nEncrypted Message: {cipherMessage.hex()}")

            return cipherSubject, cipherMessage
        else:
            show_dialog("Error", "Recipient's public key not found.")
    else:
        show_dialog("Error", "Recipient email not found in the database.")

def decrypt_message(email, cipherSubject, cipherMessage):
    # Intermediate processing dialog
    show_dialog("Intermediate Processing", "Decrypting message...")

    # Simulate receiving an email
    if email in database:
        private_key = database[email]["private_key"]
        if private_key:
            # Decrypt the subject and message with the recipient's private key
            plainSubject = private_key.decrypt(
                cipherSubject,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            plainMessage = private_key.decrypt(
                cipherMessage,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )

            # Decryption dialog
            show_dialog("Decryption", f"Decrypted Subject: {plainSubject.decode()}\nDecrypted Message: {plainMessage.decode()}")

            return plainSubject.decode(), plainMessage.decode()
        else:
            show_dialog("Error", "Private key not found.")
    else:
        show_dialog("Error", "Email not found in the database.")

# Example usage
sender_email = "harsh@example.com"
recipient_email = "asu@example.com"
subject = "Subject of Email"
message = "This is the content of the email."

# Encrypt and send the message
cipherSubject, cipherMessage = encrypt_message(recipient_email, subject, message)

# Simulate receiving the message and decrypting it
plainSubject, plainMessage = decrypt_message(recipient_email, cipherSubject, cipherMessage)
