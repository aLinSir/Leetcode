#!/usr/bin/python 
# -*- coding: utf-8 -*-

def validPalindrome(s: str) -> bool:
    for i in range(len(s) // 2 + 1):
        if s[i] != s[-i-1]:
            s1 = s[:i] + s[i+1:]
            s2 = s[:-i-1] + s[-i:] if i != 0 else s[:-i-1]
            return s1 == s1[::-1] or s2 == s2[::-1]

    return True







x = "eccer"
y = validPalindrome(x)
print(y)