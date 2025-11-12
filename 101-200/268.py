"""
Find the missing number
given a range of length n, find the missing number in the range [0, n] (inclusive)
i.e. [0, 1], n == 2, missing number is 2
i.e. [6, 3, 2, 4, 1, 0], n == 6, missing number is 5
"""

from typing import *


# brute force solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 if nums[0] != 0 else 1

        nums.sort()
        for i in range(len(nums) - 1):
            if (nums[i] + 1) != nums[i + 1]:
                return nums[i] + 1

        if nums[0] != 0:
            return 0
        return len(nums)


# using the remainder
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        remainder = (n * (n + 1)) // 2
        for i in nums:
            remainder -= i
        return remainder


# using binary logic
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n ^ n == 0, n ^ 0 == n
        sum_xor = 0
        n = len(nums)
        i = 0
        while i < n:
            sum_xor ^= nums[i]
            sum_xor ^= i
            i += 1

        sum_xor ^= n

        return sum_xor
