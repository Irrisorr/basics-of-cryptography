from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import time
import os


"""
==============================================================================================================
1. Przeanalizuj dostępne tryby pracy szyfrów blokowych w wybranym środowisku programowania i 
zmierz czasy szyfrowania i deszyfrowania dla 3 różnej wielkości plików we wszystkich 5 podstawowych trybach 
ECB, CBC, OFB, CFB, i CTR. Zinterpretuj otrzymane wyniki.
==============================================================================================================
"""
def encrypt(cipher, data):
    cipher = Cipher(algorithms.AES(os.urandom(32)), cipher)
    encryptor = cipher.encryptor()
    start_time = time.time()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    encrypt_time = time.time() - start_time

    return encrypt_time, encrypted_data


def decrypt(cipher, encrypted_data):
    cipher = Cipher(algorithms.AES(os.urandom(32)), cipher)
    decryptor = cipher.decryptor()
    start_time = time.time()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    decrypt_time = time.time() - start_time

    return decrypt_time, decrypted_data




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
            decrypt_time, decrypted_data = decrypt(cipher, encrypted_data)
            print(f"\nCipher: {cipher.__class__.name}")
            print(f"  Time of encryption: {encrypt_time:.6f} sec")
            print(f"  Time of decryption: {decrypt_time:.6f} sec")
            print(f"  Encrypted data: {encrypted_data.hex()[:32]}...")
            print(f"  Decrypted data: {decrypted_data.hex()[:32]}...")





if __name__ == "__main__":
    main()