"""
Three sum
find three distinct elements in a list add to zero
elements can have the same value but not the same index
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        for i, target in enumerate(nums):
            seen = {}
            jnums = nums[:]
            jnums.pop(i)
            for j, el in enumerate(jnums):
                subtarget = -(target + el)
                if subtarget in seen.keys() and (
                    seen[subtarget] != i and seen[subtarget] != j
                ):
                    if sorted([target, el, subtarget]) not in triplets:
                        triplets.append(sorted([target, el, subtarget]))
                seen[el] = j
        return triplets


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i, ii in enumerate(nums):
            if ii > 0:
                break

            if i > 0 and ii == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                jj, kk = nums[j], nums[k]
                triple = [ii, jj, kk]

                if sum(triple) < 0:
                    j += 1

                elif sum(triple) > 0:
                    k -= 1
                else:
                    triplets.append(triple)
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1

        return triplets


arr = [-1, 0, 1, 2, -1, -4]
s = Solution()
ans = s.threeSum(arr)
print(ans)
