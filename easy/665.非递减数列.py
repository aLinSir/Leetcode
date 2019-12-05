#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List


def checkPossibility(nums: List[int]) -> bool:
    count = 0
    index = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            count += 1
            index = i
        if count == 2:
            return False

    if index == 0 or index == len(nums) - 2:
        return True

    if (nums[index + 1] - nums[index - 1] >= 1) or (nums[index + 2] - nums[index] >= 1):
        return True

    return False

a = [3,4,2,3]
r = checkPossibility(a)
print(r)