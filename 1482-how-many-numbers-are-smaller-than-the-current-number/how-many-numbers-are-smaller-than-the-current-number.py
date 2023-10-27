class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = sorted(nums)
        ans = []
        for i in nums:
            ans.append(l.index(i))
        return ans     