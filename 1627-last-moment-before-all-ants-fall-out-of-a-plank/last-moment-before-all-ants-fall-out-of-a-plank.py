class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        temp = [n-i for i in right]
        m1 = 0
        m2 = 0
        if temp:
            m1 = max(temp)
        if left:
            m2 = max(left)
        return max(m1, m2)