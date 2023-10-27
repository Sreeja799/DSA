class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = sorted(nums)
        d = {}
        ans = []
        for i in range(len(l)):
            if l[i] not in d:
                d[l[i]] = i

        for i in nums:
            ans.append(d[i])
        return ans     