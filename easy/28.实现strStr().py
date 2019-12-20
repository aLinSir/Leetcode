#!/usr/bin/python
#-*- coding: utf-8 -*-

def strStr(haystack: str, needle: str) -> int:
    try:
        return haystack.index(needle)
    except:
        return -1





haystack = "hello"
needle = ""
y = strStr(haystack, needle)
print(y)