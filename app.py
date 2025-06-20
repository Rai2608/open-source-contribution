from encryption_switch import switch_encryption

def main():
    print("\n🔐 ShieldNet AI - Secure Communication Prototype 🔐")

    message = input("\nEnter the message to encrypt: ")

    print("\n📊 Enter threat metrics:")
    try:
        packet_size = float(input("→ Packet Size (e.g. 200): "))
        frequency = float(input("→ Transmission Frequency (e.g. 4): "))
        error_rate = float(input("→ Error Rate (e.g. 0.01): "))
        suspicious_score = float(input("→ Suspicious Content Score (0–1): "))
    except ValueError:
        print("\n❌ Invalid input. Please enter numeric values.")
        return

    metrics = [packet_size, frequency, error_rate, suspicious_score]

    result = switch_encryption(message, metrics)

    print("\n✅ Encryption Process Complete:")
    print(f"🔒 Method Used: {result['method']}")
    print(f"🔓 Decrypted Message: {result['decrypted_message']}\n")

if __name__ == "__main__":
    main()

