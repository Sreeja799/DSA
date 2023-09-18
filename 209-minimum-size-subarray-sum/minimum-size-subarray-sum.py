class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        ans = 0
        if nums[0] >= target:
            return 1
            
        while (l <= r):
            mid = (l + r) // 2
            sum_ = sum(nums[:mid])
            print(l, r, mid, target, ans, sum_)
            for i in range(mid, len(nums)+1):
                if target <= sum_:
                    ans = mid
                    break
                elif i < len(nums):
                    sum_ = sum_ + nums[i] - nums[i-mid]

            if ans == mid:
                r = mid-1
            else:
                l = mid+1
            
        

        return ans