"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # because dealing with 64 bit number sucks
        # (the above mask limits to 32 bit numbers to stop carry from overflowing)
        while b & mask:
            c = (a & b) << 1
            a = a ^ b
            b = c
        return a & mask if b > 0 else a
