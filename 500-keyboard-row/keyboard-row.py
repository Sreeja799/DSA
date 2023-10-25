class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f = set("qwertyuiop")
        s = set("asdfghjkl")
        t = set("zxcvbnm")

        l = []
        for word in words:
            word_temp = set(word.lower())
            if (word_temp <= f) or (word_temp <= s) or (word_temp <= t):
                l.append(word)
            
        return l