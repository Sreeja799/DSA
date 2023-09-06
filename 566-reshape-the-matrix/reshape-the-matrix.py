class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = []
        if ((r * c) != (len(mat) * len(mat[0]))):
            return mat
        
        temp = [j for i in mat for j in i] # flattening
        print(temp)
        ct = 0

        for i in range(r):
            row = []
            for j in range(c):
                row.append(temp[ct])
                ct += 1
            arr.append(row)

        return arr