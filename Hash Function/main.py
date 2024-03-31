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


def getAllHashes(encodeText, hashFunctions):
    for hashFunc in hashFunctions:
        print(f"{hashFunc.__name__.upper()[8:]}: {generateHash(encodeText, hashFunc)}")


def generateHash(encodeText, hashFunc):
    hash = hashFunc(encodeText)
    return hash.hexdigest()



"""
======================================================================================================
2. Porównaj szybkość działania poszczególnych funkcji oraz długość ciągów wyjściowych. 
Użyj zbioru danych wejściowych o zróżnicowanej długości. 
======================================================================================================
"""


def compareHashFunctions(words, hash_functions):

    for word in words:
        print(f"\nRozmiar ciągu: {len(word)}")
        encodeWord = word.encode()
        for hash_func in hash_functions:
            start_time = time.time()
            hash_value = generateHash(encodeWord, hash_func)
            end_time = time.time()
            print(f"{hash_func.__name__.upper()[8:]} -> (Długość ciągu wyjściowego: {len(hash_value)}\t Czas działania: {end_time - start_time:.6f} s)")


"""
======================================================================================================
3. Wygeneruj skrót dla słowa wejściowego, nie dłuższego niż 4 znaki. 
Skopiuj wartość uzyskaną dla funkcji MD5 i sprawdź, czy wartość wejściowa jest powszechnie znana. 
Co można powiedzieć o bezpieczeństwie skrótów z krótkich haseł składowanych w bazach danych?
======================================================================================================
"""









def main():
    text = inputText()
    print(f"\nPhrase: {text}")
    print(f"Binary representation: {textToBin(text)}\n\n")

    encodeText = text.encode()
    print(">=============> Zadanie 1. <============<")
    print("Hashes:\n")

    hash_functions = [hashlib.md5, hashlib.sha1,
                      hashlib.sha224, hashlib.sha256, hashlib.sha384, hashlib.sha512,
                      hashlib.sha3_224, hashlib.sha3_256, hashlib.sha3_384, hashlib.sha3_512]
    getAllHashes(encodeText, hash_functions)

    print("\n\n>=============> Zadanie 2. <============<")
    words = ["Kot", ''.join(random.choices(string.ascii_letters + string.digits, k=1000)),
                    ''.join(random.choices(string.ascii_letters + string.digits, k=10000))]
    compareHashFunctions(words, hash_functions)

    print("\n\n>=============> Zadanie 3. <============<")





if __name__ == "__main__":
    main()