from typing import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                row_el = matrix[row][col]
                col_el = matrix[col][row]
                matrix[row][col] = col_el
                matrix[col][row] = row_el

        # reverse rows
        for row in range(n):
            matrix[row] = list(reversed(matrix[row]))

        return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
s.rotate(matrix)
