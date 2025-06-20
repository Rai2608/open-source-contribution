from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate a random 256-bit AES key (32 bytes)
def generate_aes_key():
    return os.urandom(32)

# AES Encrypt
def aes_encrypt(plaintext, key):
    # Add padding
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    iv = os.urandom(16)  # 128-bit IV for AES
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return iv + ciphertext  # Return IV + ciphertext together

# AES Decrypt
def aes_decrypt(ciphertext_with_iv, key):
    iv = ciphertext_with_iv[:16]
    ciphertext = ciphertext_with_iv[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()

# Example usage
if __name__ == "__main__":
    key = generate_aes_key()
    message = "This is a secret message."
    encrypted = aes_encrypt(message, key)
    decrypted = aes_decrypt(encrypted, key)

    print("Original:", message)
    print("Decrypted:", decrypted)
