#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    l = [n for n in nums if nums.count(n) == 2]
    for i in range(1, len(nums) + 1):
        if i not in nums:
            l[1] = i

    return l


nums = [1, 2, 2, 4]
y = findErrorNums(nums)
print(y)