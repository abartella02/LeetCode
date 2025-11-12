"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. Y
ou are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have
finished course 1. So it is impossible.
"""

from typing import *


class Solution:
    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Use DFS to find if there is a cycle in the graph.
        If a has prereq b and b has prereq a, then completing a and b is impossible.
        """
        nodes = {}
        for i, j in prerequisites:
            if nodes.get(i, None):
                nodes[i].append(j)
            else:
                nodes[i] = [j]

        seen = set()

        def dfs(node):
            next = nodes.get(node, None)

            if not next:
                return True  # no cycle

            if node in seen:
                return False  # cycle

            seen.add(node)

            for child in next:
                if not dfs(child):
                    return False

            nodes[node] = []  # no cycles associated with this course
            return True

        return all([dfs(i) for i in nodes.keys()])
