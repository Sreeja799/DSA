class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        count = 0
        d = {}
        for i in range(n):
            d[nums[i]] = i

        for i in range(n):
            if (nums[i] + diff in d) and (d[nums[i]+diff] > i):
                print('ff')
                if (nums[i] + 2 * diff in d and d[nums[i] + 2 * diff] > i):
                    count += 1

        return count       