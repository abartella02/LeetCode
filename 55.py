from typing import *


class Solution:
    def canJumpBruteForce(self, nums: List[int]) -> bool:
        """O(n^2) time, O(1) space"""

        def find(nums, idx):
            if idx == 0:
                return True

            i = idx
            j = 1
            target = None
            while i - j >= 0:
                steps_available = nums[i - j]
                steps_required = j
                if steps_available >= steps_required:
                    target = i - j
                j += 1

            if target is None:
                return False
            else:
                return find(nums, target)

        end = len(nums) - 1
        return find(nums, end)

    def canJump(self, nums: List[int]) -> bool:
        """
        Gas and car approach: don't use the next jump distance if it is not > the previous
        O(n) time O(1) space
        """
        end = len(nums) - 1
        i = 0
        gas = 0
        while i < end:
            if nums[i] > gas:
                gas = nums[i]
            if gas <= 0:
                return False
            gas -= 1
            i += 1

        return True


nums = [2, 3, 1, 1, 4]
s = Solution()
s.canJump(nums)
