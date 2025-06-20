from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import os

# Generate a 256-bit ChaCha20 key
def generate_chacha_key():
    return os.urandom(32)

# Encrypt using ChaCha20
def chacha_encrypt(plaintext, key):
    nonce = os.urandom(16)  # 128-bit nonce
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode())
    return nonce + ciphertext  # Prepend nonce for decryption

# Decrypt using ChaCha20
def chacha_decrypt(ciphertext_with_nonce, key):
    nonce = ciphertext_with_nonce[:16]
    ciphertext = ciphertext_with_nonce[16:]
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext)
    return plaintext.decode()

# Example usage
if __name__ == "__main__":
    key = generate_chacha_key()
    message = "Secure message via ChaCha20."
    encrypted = chacha_encrypt(message, key)
    decrypted = chacha_decrypt(encrypted, key)

    print("Original:", message)
    print("Decrypted:", decrypted)
