class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(target, i, start, end):
            while start <= end:
                mid = (start + end) // 2
                if i[mid] == target:
                    return True
                elif i[mid] < target:
                    start = mid+1
                else:
                    end = mid-1
            return False


        for i in matrix:
            print(i)
            if binarySearch(target, i, 0, len(matrix[0])-1):
                return True
        return False