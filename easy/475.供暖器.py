#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List


def findRadius(houses: List[int], heaters: List[int]) -> int:

    for house in houses:
        left = 0
        right = len(heaters) - 1

        while left < right:
            mid = left + (right - left) // 2
            if heaters[mid] < house:
                left



x = [1,2,3,4]
y = [10]
s = findRadius(x, y)


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        # 每个房子被供暖需要的最小半径
        for house in houses:

            left = 0
            right = len(heaters) - 1
            while left < right:
                middle = left + (right - left) // 2
                if heaters[middle] < house:
                    left = middle + 1
                else:
                    right = middle

            # 供暖器和房子的位置相等
            if heaters[left] == house:
                house_res = 0
            # 此时是最接近房子的供暖器
            elif heaters[left] < house:
                house_res = house - heaters[left]
            # 供暖器不一定是最接近房子的
            else:
                # 第一个供暖器
                if left == 0:
                    house_res = heaters[left] - house
                else:
                    # 这个供暖器和前一个供暖期哪个更接近
                    house_res = min(heaters[left] - house, house - heaters[left - 1])

            res = max(house_res, res)

        return res

