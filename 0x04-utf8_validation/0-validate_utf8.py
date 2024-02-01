#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    '''Define validUTF8'''
    num = 0
    byte1 = 1 << 7
    byte2 = 1 << 6
    for b in data:
        if num == 0:
            i = 1 << 7
            while i & b:
                num += 1
                i = i >> 1
            if num == 0:
                continue
            if num == 1 or num > 4:
                return False
        else:
            if not (b & byte1 and not (b & byte2)):
                return False
        num -= 1
    return num == 0
