import math
import random
from sympy import primitive_root

# ============= 1. A i B uzgadniają ze sobą w sposób jawny
# ============= wybór dwóch dużych liczb całkowitych
# ============= n – duża liczba pierwsza i g – pierwiastek pierwotny
# ============= modulo n, i gdzie 1<g<n.

def inputN():
    print("Write here n (>1000) -> ", end="")
    n = int(input())
    return findNearestPrime(n)

def getG(n):
    return primitive_root(n)

def findNearestPrime(n):
    if n < 2:
        return 3
    x1 = n
    while x1 <= n:
        if isPrime(x1) and x1 % 4 == 3:
            break;
        else: x1-=1

    x2 = n
    while x2 >= n:
        if isPrime(x2) and x2 % 4 == 3:
            break;
        else: x2+=1

    if abs(x1-n) < (x2 - n):
        return x1
    else: return x2

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
        else: continue
    return True


# =========== 2. A wybiera losową dużą liczbę całkowitą x (tajną) -
# =========== to będzie jej klucz prywatny i oblicza X=gxmod n

def getX(n, g):
    x = random.randint(2, n)
    return pow(g, x) % n


# ============ 3. B	wybiera	losową dużą liczbę całkowitą y (tajną) –
# ============ to będzie klucz prywatny osoby B i oblicza Y=gymod n

def getY(n, g):
    y = random.randint(2, n)
    return pow(g, y) % n


# ============== 4. A i B przesyłają do siebie nawzajem obliczone X i Y.
# ============== 5. A oblicza k= Yxmod n
# ============== 6. B oblicza k= Xymod n

def getK_A(x, y, n):
    return (y * x) % n


def getK_B(x, y, n):
    return (x * y) % n


# ================= 7. Mogą	teraz używać k jako	klucza sesji
# ================= (np. do algorytmu blokowego).







def main():
    n = inputN()
    g = getG(n)
    print(f"n = {n}")
    print(f"g = {g}")

    x = getX(n, g)
    print(f"A's private key = {x}")

    y = getY(n, g)
    print(f"B's private key = {y}")

    k = getK_A(x, y, n)
    print(f"A's key = {k}")

    k = getK_B(x, y, n)
    print(f"B's key = {k}")


if __name__ == '__main__':
    main()