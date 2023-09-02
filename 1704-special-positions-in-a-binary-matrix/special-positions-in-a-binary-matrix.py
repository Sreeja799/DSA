class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        count = 0

        for i in range(n):
            for j in range(m):

                if mat[i][j] == 1:
                    flag = 0

                    for b in range(n):
                        if mat[b][j] == 1 and b != i:
                            flag = 1
                            break

                    for b in range(m):
                        if mat[i][b] == 1 and b != j:
                            flag = 1
                            break    
                    if flag != 1:
                        count += 1
        return count                     