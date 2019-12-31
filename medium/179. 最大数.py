#!/usr/bin/python 
# -*- coding: utf-8 -*-
from typing import List


# def largestNumber(nums: List[int]) -> str:
#     nums = list(map(str, nums))
#     for i in range(len(nums) - 1):
#         for j in range(len(nums)- 1 - i):
#             x, y = nums[j], nums[j + 1]
#             if (x + y) < (y + x):
#                 nums[j], nums[j + 1] = y, x
#
#     return ''.join(nums).lstrip('0') or '0'

class Helper(str):
    def __lt__(x, y):
        return x + y > y + x


def largestNumber(nums: List[int]) -> str:
    nums = sorted(map(str, nums), key=Helper)
    return ''.join(nums).lstrip('0') or '0'


def quick_sort(nums):
    if len(nums) >= 2:
        mid = nums[len(nums) // 2]
        left, right = [], []
        nums.remove(mid)
        for n in nums:
            if n <= mid:
                left.append(n)
            else:
                right.append(n)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return nums




if __name__ == '__main__':
    x = [3, 30, 34, 5, 9]
    y = largestNumber(x)
    print(y)
    g = quick_sort(x)
    print(g)