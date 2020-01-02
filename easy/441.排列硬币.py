#!/usr/bin/python
#-*- coding: utf-8 -*-
def arrangeCoins(n: int) -> int:
    # if n == 0 or n == 1: return n
    max_num = int((2 * n) ** 0.5)
    for c in range(max_num, 0, -1):
        tmp = c * (c + 1) / 2
        if tmp <= n:
            return c
    return 0




x = 0
y = arrangeCoins(x)
print(y)