class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = []

        if len(original) != n * m:
            return arr
        
        j = 0
        while j < m*n:
            temp = []
            i = 0
            while i < n:
                temp.append(original[j + i])
                i += 1
            j += n
            arr.append(temp)

        return arr