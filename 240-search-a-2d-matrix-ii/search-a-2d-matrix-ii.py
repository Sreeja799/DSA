import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)         # no. of rows
        n = len(matrix[0])      # no. of columns
        
        i = 0
        j = n-1

        while (i <= m-1 and j >= 0):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False