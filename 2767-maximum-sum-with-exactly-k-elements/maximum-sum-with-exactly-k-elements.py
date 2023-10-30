class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        sum = 0
        while k > 0:
            m = max(nums)
            i = nums.index(m)

            nums[i] += 1
            sum += m
            k -= 1
        return sum
        