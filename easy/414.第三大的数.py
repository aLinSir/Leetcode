#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List
def thirdMax(nums: List[int]) -> int:
    l = sorted(set(nums), reverse=True)
    return l[2] if len(l) >=3 else l[0]





x = [1,2]
y = thirdMax(x)
print(y)