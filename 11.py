"""
You are given an integer array height of length n. There are n vertical lines drawn such
that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import *


class Solution:
    def maxAreaBruteForce(self, height: List[int]) -> int:
        gbl_max = 0
        i = 0
        while i < (len(height) - 1):
            j = i + 1
            while j < len(height):
                a = min(height[i], height[j]) * (j - i)
                if a > gbl_max:
                    gbl_max = a
                j += 1
            i += 1

        return gbl_max

    def maxArea(self, height: List[int]) -> int:
        """
        flow:
            two pointer
            start at ends of arr
            move the lowest pointer towards middle to the next entry
        """

        def area(r, l):
            return min(height[r], height[l]) * (r - l)

        n = len(height)
        left, right = 0, n - 1
        max_a = 0

        while right > left:
            r, l = height[right], height[left]
            max_a = max(max_a, area(right, left))
            if r < l:
                right -= 1
            else:
                left += 1

        return max_a
