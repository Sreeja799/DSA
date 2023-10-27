class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                count += d[i]
                d[i] += 1
                
        return count        