class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        cur = -n

        # left to right; left side
        for i in range(n):
            if s[i] == c:
                cur = i
            ans[i] = abs(i - cur)

        # right to left; right side
        cur = -n
        for i in range(n-1, -1, -1):
            if s[i] == c:
                cur = i
            ans[i] = min(ans[i], abs(i - cur))

        return ans        