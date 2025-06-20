from ai_detection.threat_model import train_model, detect_threat
from Encryption.aes_utils import aes_encrypt, aes_decrypt, generate_aes_key
from Encryption.chacha_utils import chacha_encrypt, chacha_decrypt, generate_chacha_key
from Encryption.hybrid_utils import hybrid_encrypt, hybrid_decrypt

def switch_encryption(message, metrics):
    """
    Chooses encryption method based on AI-evaluated threat level.
    metrics: [packet_size, frequency, error_rate, suspicious_score]
    """
    model = train_model()
    threat_level = detect_threat(metrics, model)
    print(f"Threat Level: {threat_level}")

    if threat_level == "Low":
        key = generate_aes_key()
        encrypted = aes_encrypt(message, key)
        decrypted = aes_decrypt(encrypted, key)
        method = "AES"
    elif threat_level == "Moderate":
        key = generate_chacha_key()
        encrypted = chacha_encrypt(message, key)
        decrypted = chacha_decrypt(encrypted, key)
        method = "ChaCha20"
    else:
        encrypted_key, encrypted_message = hybrid_encrypt(message)
        decrypted = hybrid_decrypt(encrypted_key, encrypted_message)
        method = "Hybrid (RSA + AES)"

    return {
        "method": method,
        "decrypted_message": decrypted
    }

# Example usage
if __name__ == "__main__":
    sample_message = "Secure mission orders."
    
    # Try changing these to simulate different threats
    threat_metrics = [200, 4, 0.01, 0]       # Low
    # threat_metrics = [240, 7, 0.03, 0.5]   # Moderate
    # threat_metrics = [300, 10, 0.07, 1]    # High

    result = switch_encryption(sample_message, threat_metrics)

    print(f"Method Used: {result['method']}")
    print(f"Decrypted Message: {result['decrypted_message']}")
