class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i, n):
                count += len(list(set(nums[i:j+1]))) ** 2
        
        return count        