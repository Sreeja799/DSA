class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        d = {}
        count = 0
        for i in words:
            if i[::-1] in d:
                count += 1
            else:
                d[i] = 1
        return count       