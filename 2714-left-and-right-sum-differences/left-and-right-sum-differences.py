class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = 0
        suffix = sum(nums)

        for i in nums:
            prefix += i
            ans.append(abs(suffix - prefix))
            suffix -= i
        return ans        