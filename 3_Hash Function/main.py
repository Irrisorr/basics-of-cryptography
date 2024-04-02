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


def findHashMD5(word, filename):
    hash = generateHash(word.encode(), hashlib.md5)
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if generateHash(line.encode(), hashlib.md5) == hash:
                print(f"Znaleziono słowo: {line}")
                return
    print("Nie znaleziono słowa w pliku.")


"""
5. Dla wybranej przez siebie funkcji skrótu, zbadaj kolizje na pierwszych 12 bitach	skrótu.
"""


def checkHashCollisions(hash_func, num_bits=12):
    print("\n Kolizje na pierwszych 12 bitach dla funkcji " + hash_func.__name__.upper()[8:])
    collisions = {}
    count = 0
    while True:
        count += 1
        text = "".join(random.choices(string.ascii_letters + string.digits, k=4))
        hashValue = generateHash(text.encode(), hash_func)
        skrot = hashValue[:num_bits//4]

        if skrot in collisions:
            print(f"Kolizja {skrot} znaleziona po {count} probach u {text} i {collisions[skrot]}")
            break
        else:
            collisions[skrot] = text


"""
6. Losowość wyjścia funkcji skrótu (kryterium SAC – Strict Avalanche Criteria) – 
przy zmianie pojedynczego bitu na wejściu, wszystkie bity wyjściowe powinny 
zmienić się z prawdopodobieństwem 0,5 każdy. 
Dla wybranej funkcji skrótu zbadaj tę własność
"""


def checkSAC(hash_func, word):
    print("\nWlasnosc kryterium SAC dla funkcji " + hash_func.__name__.upper()[8:])
    firstHash = generateHash(word.encode(), hash_func)
    hashLength = len(firstHash) * 4
    bitChanges = [0] * hashLength

    for i in range(len(word)):
        for bit in range(8):
            newWord = word[:i] + chr(ord(word[i]) ^ (1 << bit)) + word[i + 1:]
            newHash = generateHash(newWord.encode(), hash_func)

            origBits = int(firstHash, 16)
            newBits = int(newHash, 16)
            bitDiff = bin(origBits ^ newBits).count('1')

            for j in range(hashLength):
                bitChanges[j] += ((newBits ^ origBits) >> j) & 1

    totalTrials = len(word) * 8
    for i in range(hashLength):
        bitChanges[i] /= totalTrials
    print(bitChanges)







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
    word = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 4)))
    print(f"Word: {word}")
    print(f"Hash: {generateHash(word.encode(), hashlib.md5)}")

    print("\n\n>=============> Zadanie 5. <============<")
    checkHashCollisions(hashlib.md5)

    print("\n\n>=============> Zadanie 6. <============<")
    checkSAC(hashlib.sha256, word)





if __name__ == "__main__":
    main()