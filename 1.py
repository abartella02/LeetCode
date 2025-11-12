"""
Two sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List


class BadSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def bin_search(nums, target):
            if len(nums) == 1:
                return 0
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid].num >= target:
                    high = mid
                else:
                    low = mid + 1
            return low - 1 if low == len(nums) else low

        class El:
            def __init__(self, idx, num):
                self.idx = idx
                self.num = num

        nums = [El(idx, num) for idx, num in enumerate(nums)]
        nums.sort(key=lambda element: element.num)

        for i in range(len(nums)):
            a = nums[i]
            n = nums[:i] + nums[i + 1 :]
            j = bin_search(n, target - a.num) + 1  # because we removed an element
            b = nums[j]
            if (a.num + b.num) == target:
                return sorted([a.idx, b.idx])


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, el in enumerate(nums):
            subtarget = target - el
            if subtarget in seen.keys():
                return [i, seen[subtarget]]
            seen[el] = i


nums, target = [3, 2, 3], 6
s = Solution()
ans = s.twoSum(nums, target)
print(ans)
