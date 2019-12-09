#!/usr/bin/python
#-*- coding: utf-8 -*-


def repeatedStringMatch(A: str, B: str) -> int:
    count = 1
    tmp = A
    while len(A) <= len(B) + len(A):
        print(A)
        if B in A and len(A) >= len(B):
            return count
        count += 1
        A += tmp
    return -1




A = "bb"
B = "bbbbbbb"
y = repeatedStringMatch(A, B)
print(y)