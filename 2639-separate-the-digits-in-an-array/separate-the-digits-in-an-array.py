class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        d = []
        for i in nums:
            i = str(i)
            for j in i:
                d.append(int(j))
        return d        