import hashlib
import random
import string
import time

def inputText():
    print("Write here your phrase -> ", end="")
    text = input()
    return text


def textToBin(text):
    return " ".join(bin(ord(i))[2:] for i in text)


"""
======================================================================================================
1. Przygotuj aplikację, która pozwoli na wygenerowanie wartości skrótu zapisanego
szesnastkowo na podstawie tekstowego wejścia, zadanego przez użytkownika.
Skorzystaj z bibliotek natywnie dostępnych w wybranym środowisku
programistycznym. Uwzględnij funkcje skrótu MD5, SHA-1, wszystkie warianty SHA-2 oraz SHA-3.
======================================================================================================
"""


def getAllHashFuncs(text):
    dict = {}
    dict["MD5"] = hashlib.md5(text.encode())
    dict["SHA-1"] = hashlib.sha1(text.encode())
    dict["SHA2-224"] = hashlib.sha224(text.encode())
    dict["SHA2-256"] = hashlib.sha256(text.encode())
    dict["SHA2-384"] = hashlib.sha384(text.encode())
    dict["SHA2-512"] = hashlib.sha512(text.encode())
    dict["SHA3-224"] = hashlib.sha3_224(text.encode())
    dict["SHA3-256"] = hashlib.sha3_256(text.encode())
    dict["SHA3-384"] = hashlib.sha3_384(text.encode())
    dict["SHA3-512"] = hashlib.sha3_512(text.encode())
    return dict


"""
======================================================================================================
2. Porównaj szybkość działania poszczególnych funkcji oraz długość ciągów wyjściowych. 
Użyj zbioru danych wejściowych o zróżnicowanej długości. 
======================================================================================================
"""


def main():
    text = inputText()
    print(f"Phrase: {text}")
    print(f"Binary representation: {textToBin(text)}\n\n")

    encodeText = text.encode()
    print(">=============> Zadanie 1. <============<")
    print("Hashes:\n")
    hashFuncs = getAllHashFuncs(text)
    for hashFunc in hashFuncs:
        print(f"{hashFunc}: {hashFuncs[hashFunc].hexdigest()}")

    print("\n\n>=============> Zadanie 2. <============<")


if __name__ == "__main__":
    main()