import math
import random


#================= 1.	Wyznacz	wartość	iloczynu	N	dwóch	dużych	liczb	pierwszych,	takich	że:

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
# ============================================ 4. ================================  Powtarzaj w pętli

def generateSequence(x, n):
    random_sequence = ''
    for i in range(0, 20000):
        x = pow(x, 2) % n
        # print(f"x_{i} = {x}")
        random_sequence += '1' if x & 1 else '0'
    return random_sequence



# ================================================================== Test pojedynczych bitów

def firstTest(sequence):
    print("\n\nTest pojedynczych bitów")
    bit = sequence.count('1')
    print(f"W ciągu mamy - {bit} jedynek")
    print("musi być 9725 < n(1) < 10275 -> ", end="")
    print("true" if 9725 < bit < 10275 else "false")


# ================================================================== Test serii

def secondTest(sequence):
    print("\n\nTest serii")
    seria = [0, 0, 0, 0, 0, 0]
    count = 0
    sequence +='0'
    for i in range(len(sequence)):
        if sequence[i] == '1':
            count += 1
        else:
            if count == 1:
                seria[0] += 1
            elif count == 2:
                seria[1] += 1
            elif count == 3:
                seria[2] += 1
            elif count == 4:
                seria[3] += 1
            elif count == 5:
                seria[4] += 1
            elif count >= 6:
                seria[5] += 1
            count = 0
    print(f"Seria: | przedział | mamy | poprawna?\n",
          f"   1 | 2315-2685 | {seria[0]} | true\n" if seria[0] >= 2315 and seria[0] <= 2685 else f"1 | 2315-2685 | {seria[0]} | false\n ",
          f"   2 | 1114-1386 | {seria[1]} | true\n" if seria[1] >= 1114 and seria[1] <= 1386 else f"2 | 1114-1386 | {seria[1]} | false\n ",
          f"   3 | 527-723   | {seria[2]}  | true\n" if seria[2] >= 527 and seria[2] <= 723 else f"3   | 527-723 | {seria[2]}  | false\n ",
          f"   4 | 240-384   | {seria[3]}  | true\n" if seria[3] >= 240 and seria[3] <= 384 else f"4   | 240-384 | {seria[3]}  | false\n ",
          f"   5 | 103-209   | {seria[4]}  | true\n" if seria[4] >= 103 and seria[4] <= 209 else f"5   | 103-209 | {seria[4]}  | false\n ",
          f"   6 | 103-209   | {seria[5]}  | true\n" if seria[5] >= 103 and seria[5] <= 209 else f"6   | 103-209 | {seria[5]}  | false\n")



def thirdTest(sequence):
    print("\n\nTest serii")

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