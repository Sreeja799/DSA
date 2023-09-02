class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ps = []
        for i in range(len(nums)):
            ps.append(sum(nums[:i+1]))
        return ps