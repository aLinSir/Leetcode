#!/usr/bin/python
#-*- coding: utf-8 -*-
def checkPerfectNumber(num: int) -> bool:
    if num <= 1: return False
    mid = int(num ** 0.5) + 1
    p_list = [1]
    for i in range(2, mid):
        v, m = divmod(num, i)
        if m == 0: p_list.extend([i, v])

    return sum(p_list) == num




x = 1
y = checkPerfectNumber(x)
print(y)