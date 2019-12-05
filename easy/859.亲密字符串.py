#!/usr/bin/python
#-*- coding: utf-8 -*-

def buddyStrings(A: str, B: str) -> bool:
    if len(A) != len(B): return False

    if A == B and len(set(A)) < len(A): return True

    ins = [(a ,b) for a, b in zip(A, B) if a != b]

    return len(ins) == 2 and ins[0] == ins[1][::-1]


A = "abab"
B = "abab"
a = buddyStrings(A, B)
print(a)