class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        new = [[0 for _ in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                new[j][i] = matrix[i][j]
        return new        