class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def check(ch):
            f = "qwertyuiop"
            s = "asdfghjkl"
            t = "zxcvbnm"

            if f.find(ch) != -1:
                r = f
            elif s.find(ch) != -1:
                r = s
            else:
                r = t
            return r

        l = []
        for word in words:
            word_temp = word.lower()
            flag = True
            r = check(word_temp[0])
            for i in range(1, len(word_temp)):
                if word_temp[i] not in r:
                    flag = False
                    break

            if flag == True:
                l.append(word)
        return l