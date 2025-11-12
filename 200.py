"""
200. Number of Islands

Given an m x n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if (r, c) in seen:
                return

            if not (r in range(m) and c in range(n)):
                return

            if grid[r][c] == "0":
                return

            seen.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen:
                    count += 1
                    dfs(i, j)

        return count
