"""
You are given an array of non-overlapping intervals intervals where
intervals[i] = [start_i, end_i] represent the start and the end of the ith interval
and intervals is sorted in ascending order by start_i. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order
by start_i and intervals still does not have any overlapping intervals (merge overlapping
intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.


Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

from typing import *


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        _intervals = intervals.copy()
        _newInterval = newInterval.copy()

        res = []
        n = len(intervals)
        i = 0
        while i < n:
            if _newInterval[0] <= intervals[i][1]:
                # possible overlap detected at interval i
                # newInterval = (a, b), i = (c, d) --> a <= d
                break
            res.append(intervals[i])  # append intervals with no chance of overlapping
            i += 1

        # overlap detection
        start, end = _newInterval
        while (
            i < n
        ):  # if above loop exits without breaking, i == n and this loop is never entered
            if _newInterval[1] < intervals[i][0]:
                # possible overlap detected in above loop, but this `if` checks to make sure
                # there is actual overlap
                # newInterval = (a, b) i = (c, d) --> we know already a <= d, check b < c
                # if b < c, there is no more overlap
                break
            start = min(start, intervals[i][0])  # track overlap start
            end = max(end, intervals[i][1])  # track overlap end
            i += 1

        res.append([start, end])
        return res + intervals[i:]
