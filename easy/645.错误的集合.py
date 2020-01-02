#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    n = len(nums)
    a = sum(nums) - sum(set(nums))
    b = n * (n + 1) // 2 - sum(set(nums))
    return [a, b]


nums = [1, 2, 2, 4]
y = findErrorNums(nums)
print(y)