class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        d = {}
        for i in allowed:
            d[i] = 1

        for word in words:
            flag = 0
            for char in word:
                if char not in d:
                    flag = 1
                    break
            if flag == 0:
                count += 1

        return count        