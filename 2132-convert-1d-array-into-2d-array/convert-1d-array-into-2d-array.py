class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = []

        if len(original) == n * m:  
            j = 0
            for i in range(0, len(original), n):
                arr.append(original[i:i+n])

        return arr