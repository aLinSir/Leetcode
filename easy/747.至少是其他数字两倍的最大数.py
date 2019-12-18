#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List

def dominantIndex(nums: List[int]) -> int:
    if len(nums) == 1: return 0
    s_nums = sorted(nums, reverse=True)
    if s_nums[0] >= 2 * s_nums[1]:
        return nums.index(s_nums[0])
    else:
        return -1








nums = [3, 6, 1, 0]
y = dominantIndex(nums)
print(y)