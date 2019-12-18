#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List


def isBoomerang(points: List[List[int]]) -> bool:
    def slope(l1, l2):
        if l1[0] == l2[0]:
            return 'zero'
        elif l1[1] == l2[1]:
            return 'inf'
        else:
            return str(round((l1[1] - l2[1]) / (l1[0] -l2[0]), 4))

    k = []
    k.append(slope(points[0], points[1]))
    k.append(slope(points[0], points[2]))
    k.append(slope(points[1], points[2]))


    return len(set(k)) == 3




x = [[1,1],[2,2],[3,3]]
y = isBoomerang(x)
print(y)