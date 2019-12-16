#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    idx = {}
    for i, num in enumerate(nums):
        if num in idx and i - k <= idx[num]:
            return True
        idx[num] = i

    return False








nums = [1,2,3,1,2,3]
k = 2
y = containsNearbyDuplicate(nums, k)
print(y)