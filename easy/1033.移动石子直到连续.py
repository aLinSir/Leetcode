#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List

def numMovesStones(a: int, b: int, c: int) -> List[int]:
    a,b,c = sorted([a,b,c])
    left = b - a
    right = c - b
    if left <= 1 and right <= 1: return [0, 0]

    if left <= 2 or right <= 2:
        min_step = 1
    else:
        min_step = 2

    max_step = c - a - 2
    return [min_step, max_step]




x = 3
y = 5
z = 1
re = numMovesStones(x,y,z)
print(re)