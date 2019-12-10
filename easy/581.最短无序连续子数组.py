#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List
def findUnsortedSubarray(nums: List[int]) -> int:
    sn = sorted(nums, reverse=False)

    left, right = 0, 0
    con_l, con_r = False, False
    for i in range(len(nums)):
        if nums[i] != sn[i] and not con_l:
            left = i
            con_l = True
        if nums[-i-1] != sn[-i-1] and not con_r:
            right = len(nums) - i
            con_r = True

    return right - left




x = [1,2,3,5,4]
y = findUnsortedSubarray(x)
print(y)