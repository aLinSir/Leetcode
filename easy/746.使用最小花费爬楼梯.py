#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    # f1 代表走，f2 代表不走
    f1, f2 = cost[0], 0
    for v in cost[1:]:
        f1, f2 = v + min(f1, f2), f1
    return min(f1, f2)






cost = [1, 2, 2, 0]
y = minCostClimbingStairs(cost)
print(y)