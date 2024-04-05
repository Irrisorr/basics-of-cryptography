from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import time
import os


def encrypt(cipher, data):
    start_time = time.time()
    cipher = Cipher(algorithms.AES(os.urandom(32)), cipher)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    encrypt_time = time.time() - start_time

    return encrypt_time, encrypted_data




def main():
    data1 = os.urandom(1024)
    data2 = os.urandom(10240)
    data3 = os.urandom(102400)
    ciphers = [modes.ECB(), modes.CBC(os.urandom(16)), modes.OFB(os.urandom(16)),
               modes.CFB(os.urandom(16)), modes.CTR(os.urandom(16))]

    print("\n\n>=============> Zadanie 1. <============<")
    for data in [data1, data2, data3]:
        print(f"\nLength of data: {len(data)} bytes")
        for cipher in ciphers:
            encrypt_time, encrypted_data = encrypt(cipher, data)
            print(f"{cipher.__class__.name}:")
            print(f"  Time of encryption: {encrypt_time:.6f} sec")
            print(f"  Encrypted data: {encrypted_data.hex()[:32]}...")





if __name__ == "__main__":
    main()