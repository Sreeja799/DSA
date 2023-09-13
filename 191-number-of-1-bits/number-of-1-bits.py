class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))[2:]
        l = len(n)
        count = 0

        for i in range(l):
            if n[i] == '1':
                count += 1
        return count
        