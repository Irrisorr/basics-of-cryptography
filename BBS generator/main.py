import math
import random


#================= 1. Wyznacz wartość iloczynu N dwóch dużych liczb	pierwszych, takich że:

def getBlum(p, q):
    return p * q


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


# ===================== 2.	Wybierz	w	sposób	losowy	taką	liczbę	x taką, że	x i	N są	względnie	pierwsze


def getX(n):
    while True:
        x = random.randint(2, n*10)
        if math.gcd(x, n) == 1:
            return x


# =========================================== 3. Wyznacz	wartość	pierwotną	generatora:
# ============================================ 4.  Powtarzaj w pętli

def generateSequence(x, n):
    random_sequence = ''
    for i in range(0, 20000):
        x = pow(x, 2) % n
        # print(f"x_{i} = {x}")
        random_sequence += '1' if x & 1 else '0'
    return random_sequence



# ================================================================== Test pojedynczych bitów

def firstTest(sequence):
    print("\n\n>==================> Test pojedynczych bitów <================<")
    bit = sequence.count('1')
    print(f"W ciągu mamy - {bit} jedynek")
    print("musi być 9725 < n(1) < 10275 -> ", end="")
    print("true" if 9725 < bit < 10275 else "false")


# ================================================================== Test serii

def secondTest(sequence):
    print("\n\n>==================> Test serii <=================<")
    sequence += '0'
    count = 0
    series = {}
    for i in range(len(sequence)):
        if sequence[i] == '1':
            count += 1
        else:
            if count >= 6:
                series[6] = series.get(6, 0) + 1
            else:
                series[count] = series.get(count, 0) + 1
            count = 0

    intervals = {1: (2315, 2685), 2: (1114, 1386), 3: (527, 723), 4: (240, 384), 5: (103, 209), 6: (103, 209)}

    print("Seria | przedział | mamy | poprawna?")
    for length, interval in intervals.items():
        count = series.get(length, 0)
        lower, upper = interval
        result = "true" if lower <= count <= upper else "false"
        print(f"    {length} | {lower}-{upper} | {count} | {result}")


# ===================================================== Test długiej serii

def thirdTest(sequence):
    print("\n\n>==================> Test długiej serii <=================<")
    sequence += '0'
    count = 0
    max = 0
    char = sequence[0]
    for i in range(1, len(sequence)):
        if char == sequence[i]:
            count += 1
            if count >= 26:
                print(f"Seria przekroczyła 26 '{char}' - ciag jest błędny")
                break
        else:
            if count > max:
                max = count
            count = 0
            char = sequence[i]
    print(f"Ciag jest poprawny\nNajdłuższa seria ma {max} '{char}'")




# ==========================================================================================================

if __name__ == "__main__":

    p, q = inputNumbers()
    print(f"p = {p}, q = {q}")

    n = getBlum(p, q)
    print(f"n (Blum) = {n}")

    x = getX(n)
    print(f"x = {x}")

    random_sequence = generateSequence(x, n)
    print(f"Random sequence: {random_sequence}")
    print(f"Sequence length: {len(random_sequence)}")



    firstTest(random_sequence)
    secondTest(random_sequence)
    thirdTest(random_sequence)