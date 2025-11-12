from typing import *


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        reverse depth-first search starting from island borders (leafs)
        and going up along branches to find all possible starting points for
        a complete tree

        intersect both sets to find nodes with right and left branches
        that successfully lead to water
        """

        visited_atl = set()
        visited_pac = set()

        rows = len(heights) - 1
        cols = len(heights[0]) - 1

        def dfs(row, col, prev_height, visited):
            if row < 0 or row > rows or col < 0 or col > cols:
                return None

            if (row, col) in visited:
                return None

            cur_height = heights[row][col]
            if cur_height < prev_height:
                # failure condition
                return None

            visited.add((row, col))

            dfs(row + 1, col, cur_height, visited=visited)
            dfs(row - 1, col, cur_height, visited=visited)
            dfs(row, col + 1, cur_height, visited=visited)
            dfs(row, col - 1, cur_height, visited=visited)

        for col in range(cols + 1):
            dfs(0, col, 0, visited=visited_pac)
            dfs(rows, col, 0, visited=visited_atl)

        for row in range(rows + 1):
            dfs(row, 0, 0, visited=visited_pac)
            dfs(row, cols, 0, visited=visited_atl)

        return [list(cell) for cell in visited_pac & visited_atl]
