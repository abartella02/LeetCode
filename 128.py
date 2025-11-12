from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        prev = nums[0]
        cnt = [1]
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur == (prev + 1):
                cnt[-1] += 1
            elif cur == prev:
                pass  # proceed to next number, ignore duplicates in the sequence
            else:
                cnt.append(1)
            prev = cur

        return max(cnt)


nums = [1, 0, 1, 2]
s = Solution()
ans = s.longestConsecutive(nums)
print(ans)
