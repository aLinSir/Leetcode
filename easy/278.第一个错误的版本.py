#!/usr/bin/python 
# -*- coding: utf-8 -*-
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """

    left = 0
    right = n
    while True:
        mid = (left + right) // 2
        if isBadVersion(mid) and isBadVersion(mid + 1):
            right = mid
        elif not isBadVersion(mid) and not isBadVersion(mid + 1):
            left = mid
        elif not isBadVersion(mid) and isBadVersion(mid + 1):
            return mid + 1
