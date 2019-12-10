#!/usr/bin/python 
# -*- coding: utf-8 -*-
def reverse(x: int) -> int:
    neg = lambda x: x < 0 and x >= -2 ** 31
    pos = lambda x: x > 0 and x <= 2 ** 31 -1
    if x == 0: return 0

    xstr = str(abs(x)).strip('0')[::-1]
    
    if neg(x):
        if neg(-int(xstr)):
            return '-' + xstr
    if pos(x):
        if pos(int(xstr)):
            return xstr
    return 0











x = 1534236469
y = reverse(x)
print(y)