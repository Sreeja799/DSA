class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        count = 0
        for i in range(n):
            temp = ''
            for word in strs:
                temp += word[i]
            if ''.join(sorted(temp)) != temp:
                count += 1
        return count        