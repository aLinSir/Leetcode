#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List

def pivotIndex(nums: List[int]) -> int:
    if not nums: return -1
    left = 0
    right = sum(nums[1:])

    for i in range(0, len(nums)):
        if left == right:
            return i
        elif i != len(nums) - 1:
            left += nums[i]
            right -= nums[i+1]
    return -1

    # if not nums: return -1
    # left = 0
    # all = sum(nums)
    #
    # for i in range(0, len(nums)):
    #     if left * 2 + nums[i] == all:
    #         return i
    #     elif i != len(nums) - 1:
    #         left += nums[i]
    # return -1







x = [1, -1, 2, -3, 5]
y = pivotIndex(x)
print(y)