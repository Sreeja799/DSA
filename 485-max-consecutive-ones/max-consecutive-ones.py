class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        temp = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                temp += 1
            else:
                max_count = max(max_count, temp)
                temp = 0
            i += 1
        return max(max_count, temp)