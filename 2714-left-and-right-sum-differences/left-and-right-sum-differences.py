class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        ltor = [nums[0]]
        n = len(nums)
        if n == 1:
            return [0]

        for i in range(1, n):
            ltor.append(ltor[i-1] + nums[i])

        rtol = [nums[-1]]
        for i in range(n-2, -1, -1):
            rtol.insert(0, rtol[0] + nums[i])
        
        print(ltor, rtol)
        ans.append(rtol[1])
        for i in range(1, n-1):
            ans.append(abs(ltor[i-1] - rtol[i+1]))
        ans.append(ltor[n-2])
        return ans        