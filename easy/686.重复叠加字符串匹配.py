#!/usr/bin/python
#-*- coding: utf-8 -*-


def repeatedStringMatch(A: str, B: str) -> int:
    n = int(len(B) / len(A))
    print(n)
    if B in A * n: return n
    elif B in A * (n + 1): return n + 1
    elif B in A * (n + 2): return n + 2
    else: return -1

A = "aa"
B = "a"
y = repeatedStringMatch(A, B)
print(y)