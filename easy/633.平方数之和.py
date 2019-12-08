#!/usr/bin/python 
# -*- coding: utf-8 -*-
def judgeSquareSum(c: int) -> bool:
    # if 3 & 3 == 3: return False

    left = 0
    right = int(c ** 0.5)

    while left <= right:
        tmp = left ** 2 + right ** 2
        if tmp == c:
            return True
        elif tmp < c:
            left += 1
        elif tmp > c:
            right -= 1

    return False


x = 0
a = judgeSquareSum(x)
print(a)
