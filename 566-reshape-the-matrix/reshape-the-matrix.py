class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = []
        if ((r * c) != (len(mat) * len(mat[0]))):
            return mat

        rowi = 0
        coli = 0

        for _ in range(r):
            temp = []
            for i in range(c):
                temp.append(mat[rowi][coli])
                coli += 1
                if coli == len(mat[0]):
                    coli = 0
                    rowi += 1
            arr.append(temp)

        return arr