class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev = 0
        m = 0
        for i in range(len(gain)):
            prev += gain[i]
            m = max(m, prev)

        return m     