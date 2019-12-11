#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List

def largestTimeFromDigits(A: List[int]) -> str:
    from itertools import permutations

    Ap = []
    for a,b,c,d in list(permutations(A, 4)):
        if c <= 5 and d <= 9:
            if (a <= 1 and b <= 9) | (a == 2 and b <= 3):
                Ap.append(f'{a}{b}:{c}{d}')

    if Ap:
        return max(Ap)
    else:
        return ''











x = [1,2,3,4]
y = largestTimeFromDigits(x)
print(y)