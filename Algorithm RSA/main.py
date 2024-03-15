import math


# ======================== 1. Wybieramy dwie liczby pierwsze p i q

def inputNumbers():
    print("Write here first number (p) -> ", end="")
    num_1 = int(input())
    print("Write here second number (q) -> ", end="")
    num_2 = int(input())
    return findNearestPrime(num_1), findNearestPrime(num_2)


def findNearestPrime(num):
    if num < 2:
        return 3
    x1 = num
    while x1 <= num:
        if isPrime(x1) and x1 % 4 == 3:
            break;
        else: x1-=1

    x2 = num
    while x2 >= num:
        if isPrime(x2) and x2 % 4 == 3:
            break;
        else: x2+=1

    if abs(x1-num) < (x2 - num):
        return x1
    else: return x2


def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
        else: continue
    return True


# ============================ 2. Obliczamy n = p · q

def getN(p, q):
    return p * q


# ============================ 3. Obliczamy phi = (p − 1) · (q − 1)

def getPhi(p, q):
    return (p - 1) * (q - 1)


# ========================= generujemy e jako liczbę względnie pierwszą
# ========================= z phi czyli taką, która jest liczbą pierwszą i
# ========================= dla której największy wspólny dzielnik z phi wynosi 1

def getE(phi):
    for i in range(2, phi):
        if math.gcd(i, phi) == 1:
            return i


# ========================== generujemy d w taki sposób, aby spełniona
# ========================== była zależność: iloczyn e i d przystaje do 1
# ========================== modulo phi. Co oznacza, że phi dzieli
# ========================== wyrażenia e · d – 1.

def getD(e, phi):
    return pow(e, -1, phi)


# ========================== szyfrowanie RSA

def encrypt(m, e, n):
    return pow(m, e) % n


# ========================== deszyfrowanie RSA

def decrypt(c, d, n):
    return pow(c, d) % n






def main():
    p, q = inputNumbers()
    n = getN(p, q)
    phi = getPhi(p, q)

    print(f"p = {p}, q = {q},\nn = {n},\nphi = {phi}")

    e = getE(phi)
    print(f"Public key = {e}, {n}")

    d = getD(e, phi)
    print(f"Private key = {d}, {n}")

    m = int(input("Enter message: "))
    c = encrypt(m, e, n)
    print(f"Encrypted message: {c}")

    m = decrypt(c, d, n)
    print(f"Decrypted message: {m}")



if __name__ == "__main__":
    main()