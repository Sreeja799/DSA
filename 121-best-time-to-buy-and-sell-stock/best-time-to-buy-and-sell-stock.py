class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        left = 0
        right = 1
        m = 0

        while right < n:
            if prices[left] >= prices[right]:
                left = right
                right += 1
            elif prices[left] < prices[right]:
                m = max(m, prices[right] - prices[left])
                right += 1
        return m


        