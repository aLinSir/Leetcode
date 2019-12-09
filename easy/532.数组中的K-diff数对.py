#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List

def findPairs(nums: List[int], k: int) -> int:
    if k < 0: return 0
    origin = set()
    diff = set()
    for n in nums:
        if n - k in origin:
            diff.add(n - k)
        if n + k in origin:
            diff.add(n)
        origin.add(n)

    return len(diff)





x = [1,2,3,4,5]
k = 1
y = findPairs(x, k)
print(y)