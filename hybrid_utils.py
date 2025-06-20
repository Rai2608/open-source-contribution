import os
import os
from .aes_utils import aes_encrypt, aes_decrypt
from .rsa_utils import load_public_key, load_private_key, rsa_encrypt, rsa_decrypt

# Encrypt using Hybrid Encryption (RSA + AES)
def hybrid_encrypt(message, public_key_path="backend/keys/public_key.pem"):
    # Load RSA public key
    public_key = load_public_key(public_key_path)

    # Generate AES key
    aes_key = os.urandom(32)

    # Encrypt message with AES key
    encrypted_message = aes_encrypt(message, aes_key)

    # Encrypt AES key with RSA public key
    encrypted_key = rsa_encrypt(aes_key.hex(), public_key)  # Convert bytes to hex string for encryption

    return encrypted_key, encrypted_message

# Decrypt using Hybrid Decryption (RSA + AES)
def hybrid_decrypt(encrypted_key, encrypted_message, private_key_path="backend/keys/private_key.pem"):
    # Load RSA private key
    private_key = load_private_key(private_key_path)

    # Decrypt AES key using RSA private key
    decrypted_key_hex = rsa_decrypt(encrypted_key, private_key)
    aes_key = bytes.fromhex(decrypted_key_hex)

    # Decrypt message using AES key
    message = aes_decrypt(encrypted_message, aes_key)
    return message

# Example usage
if __name__ == "__main__":
    # Encrypt
    enc_key, enc_msg = hybrid_encrypt("ShieldNet AI Prototype")
    
    # Decrypt
    decrypted_msg = hybrid_decrypt(enc_key, enc_msg)

    print("Decrypted Message:", decrypted_msg)
