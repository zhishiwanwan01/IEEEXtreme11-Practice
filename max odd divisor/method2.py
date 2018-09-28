# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:03:16 2018

@author: yz001
"""

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

primeSet = np.array(prime_finder(2,int(np.sqrt(B))));
expo2 = primeSet**2
expo4 = []

for i in expo2:
    for j in expo2:
        if i*j > 1000:
            continue
        expo4.append(i*j)
        
expo4 = list(set(expo4))
expo4.sort()
expo6 = []

for i in expo2:
    for j in expo4:
        if i*j > 1000:
            continue
        expo6.append(i*j)
expo6 = list(set(expo6))
expo6.sort()
expo8 = []
for i in expo2:
    for j in expo6:
        if i*j > 1000:
            continue
        expo8.append(i*j)
expo8 = list(set(expo8))
expo8.sort()

totalList = list(expo2) + expo4 + expo6 + expo8 + [1]
totalList.sort()
output = 0
for i in range(A,B+1):
    if i in totalList:
        output += 1
        
print(output)