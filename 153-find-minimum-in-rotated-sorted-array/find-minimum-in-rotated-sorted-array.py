class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        ans = nums[0]
        while (start <= end):
            mid = (start + end) // 2
            if (nums[mid] < nums[0]):
                ans = nums[mid]
                end = mid - 1
            else:
                start = mid + 1
        return ans