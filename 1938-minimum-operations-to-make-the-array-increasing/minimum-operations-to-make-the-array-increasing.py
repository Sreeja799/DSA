class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                count += (nums[i-1] + 1 - nums[i])
                nums[i] = nums[i-1] + 1
        return count                     