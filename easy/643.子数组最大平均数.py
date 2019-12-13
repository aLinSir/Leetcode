#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    re = score = sum(nums[0: k])
    for i in range(0, len(nums) - k):
        head = nums[i]
        tail = nums[i + k]
        score = score - head + tail
        re = max(re, score)
    return re / k


x = [4,2,1,3,3]
k = 1
y = findMaxAverage(x, k)
print(y)