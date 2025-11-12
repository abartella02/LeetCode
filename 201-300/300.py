"""
Longest increasing subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""

from typing import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # use binary search to determine where to insert/replace an element O(log(n))
        def bisect_left(arr, a):
            # binary search and insertion
            _arr = arr.copy()
            n = len(_arr)
            bounds = (0, n)

            while bounds[1] - bounds[0] > 0:
                i = sum(bounds) // 2
                if a == _arr[i]:
                    # if found in arr, return index of existing el
                    return i
                elif a < _arr[i]:
                    bounds = (bounds[0], i)
                else:
                    bounds = (i + 1, bounds[1])

            return bounds[0]  # if not found, idx of next largest number

        res = []
        for i, el in enumerate(nums):
            if not res or el > res[-1]:
                res.append(el)
            elif el in res:
                pass  # skip, no repeats can be part of the sequence
            else:  # el < res[-1]
                # our number belongs in the sequence
                # where in the sequence? where it can make the most impact:
                #   if 5 belongs in the sequence, and we have [4, 6, 10]
                #   then 6 should be replaced with 5
                #   since there could be another 6 down the line that would
                #   end up replacing 10
                #   then we'd have [4, 5, 6]
                #   if we hadn't done this, if we encountered two numbers < 10
                #   they wouldn't be added to the sequence,
                #   even though they should ( [4, 5, 6, 7] > [4, 6, 10] )
                #
                #   basically, we are kicking out the numbers that are fucking
                #   up our sequence, and we end up with the longest sequence
                #   possible by doing that

                idx = bisect_left(res, el)
                res[idx] = el

        return len(res)
