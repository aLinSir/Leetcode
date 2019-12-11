#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List
def validMountainArray(A: List[int]) -> bool:
    if len(A) < 3: return False

    max_idx = A.index(max(A))
    if max_idx != 0 and max_idx != len(A) - 1:
        if A[max_idx] != A[max_idx-1] and A[max_idx] != A[max_idx+1]:
            left = A[:max_idx]
            right = A[max_idx + 1:]
            if left == sorted(left) and right == sorted(right, reverse=True):
                return len(left) == len(set(left)) and len(right) == len(set(right))

    return False









x = [0,1,2,1,2]
y = validMountainArray(x)
print(y)