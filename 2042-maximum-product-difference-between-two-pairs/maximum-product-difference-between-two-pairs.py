class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max = 0
        smax = 0
        min = float('inf')
        smin = float('inf')

        for i in nums:
            if i > max:
                smax = max
                max = i
            elif i > smax:
                smax = i
        
        for i in nums:
            if i < min:
                smin = min
                min = i
            elif i < smin:
                smin = i
        

        return (max * smax) - (min * smin)