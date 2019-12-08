#!/usr/bin/python 
# -*- coding: utf-8 -*-

def countPrimes(n: int) -> int:

    if n < 2:
        return 0

    isPrime = [1] * n
    isPrime[:2] = [0, 0]

    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            tmp = isPrime[i*i: n: i]
            isPrime[i * i: n: i] = [0] * len(tmp)

    return sum(isPrime)








a = 10
b = countPrimes(a)
print(b)