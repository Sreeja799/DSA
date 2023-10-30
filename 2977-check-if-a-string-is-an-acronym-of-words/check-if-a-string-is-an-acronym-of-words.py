class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        temp = ''
        for word in words:
            temp += word[0]
        return temp == s