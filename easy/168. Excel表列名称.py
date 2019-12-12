#!/usr/bin/python 
# -*- coding: utf-8 -*-

def convertToTitle(n: int) -> str:
    re = ''

    while n:
        n -= 1
        re = chr(n % 26 + 65) + re
        n = n // 26
    return re


x = 676
y = convertToTitle(x)
print(y)





