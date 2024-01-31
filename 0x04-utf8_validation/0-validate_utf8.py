#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    '''Define validUTF8'''
    num = 0
    for b in data:
        if num == 0:
            if b >> 5 == 0b110:
                num = 1
            elif b >> 4 == 0b1110:
                num = 2
            elif b >> 3 == 0b11110:
                num = 3
            elif b >> 7 == 0b0:
                num = 0
            else:
                return False
        else:
            if b >> 6 != 0b10:
                return False
            num -= 1
    return num == 0
