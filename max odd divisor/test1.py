import numpy as np

A = 5
B = 15


def prime_finder(N1, N2):
    # https://stackoverflow.com/questions/46141960/python-prime-number-list#
    pnumber1b = list(range(N1, N2 + 1))
    to_remove = []
    for x in pnumber1b:
        for i in range(2, x):
            if x % i == 0:
                to_remove.append(x)
                break
    for r in to_remove:
        pnumber1b.remove(r)

    return pnumber1b


def diviTimes(N, i):
    count = 0
    while N % i == 0 and N != 0:
        count += 1
        N = N / i
    return count


def isOddDivisor(N, primeList):
    threshold = int(np.sqrt(N))
    if 1 in primeList:
        primeList.remove(1)
    myPrimeList = []
    for i in primeList:
        if i > threshold:
            break
        myPrimeList.append(i)
    for i in myPrimeList:
        if N % i != 0:
            continue
        if diviTimes(N, i) % 2 == 1:
            return False
    return True


output = 0
if A == B:
    if A != 1:
        primeList = prime_finder(1, B)
#         print(primeList)
        if isOddDivisor(A, primeList):
            output += 1
else:
    myList = list(range(A, B + 1))
    print(myList)
    primeList = prime_finder(A, B)
    print(primeList)
    for i in primeList:
        if i in myList:
            # print(i)
            myList.remove(i)
            # print(myList)
            continue
    for i in myList:
        if isOddDivisor(i, primeList):
            print(i)
            output += 1

if A == 1:
    output += 1

print('output:', output)
# print(prime_finder(2, 10))
# print(myList)
print(isOddDivisor(6, primeList))
