from typing import *


class Solution:  # inefficient solution
    def minOperations(self, nums: List[int], k: int) -> int:
        def binToArr(num):
            n = num
            arr = []
            while n:
                arr.append(n & 1)
                n = n >> 1
            return arr

        def xorList(arr):
            total = 0
            for i in arr:
                total = total ^ i
            return total

        nums = binToArr(xorList(nums))
        k = binToArr(k)

        maxlen = max(len(nums), len(k))

        while len(k) < maxlen:
            k.append(0)
        while len(nums) < maxlen:
            nums.append(0)

        count = 0
        for i, j in zip(nums, k):
            if i != j:
                count += 1

        return count


class Solution:  # much better
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0
        for i in nums:
            total = total ^ i
        return bin(total ^ k).count("1")
        # return (total ^ k).bit_count()
