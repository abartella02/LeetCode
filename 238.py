from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums

        answer = [1] * n

        # division is costly, avoid using right/left prod
        right_prod = [1] * n
        left_prod = [1] * n

        for i in range(1, n):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]
            right_prod[n - i - 1] = right_prod[n - i] * nums[n - i]

        for i in range(len(answer)):
            answer[i] = left_prod[i] * right_prod[i]

        return answer


s = Solution()
nums = [0, 0]
print(s.productExceptSelf(nums))
