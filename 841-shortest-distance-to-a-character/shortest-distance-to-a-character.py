class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0 for i in range(n)]

        for i in range(n):
            if s[i] != c:
                temp1 = temp2 = float('inf')
                for j in range(i):
                    if s[j] == c:
                        temp1 = (i-j)

                for j in range(i+1, n):
                    if s[j] == c:
                        temp2 = (j-i)
                        break
                ans[i] = min(temp1, temp2)
        return ans        