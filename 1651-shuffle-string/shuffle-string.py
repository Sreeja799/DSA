class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        l = [0 for i in range(n)]

        for i in range(n):
            l[indices[i]] = s[i]
        return ''.join(l)