class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            temp = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    temp += 1
            l.append(temp)
        return l        