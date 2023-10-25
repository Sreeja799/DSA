class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        d = {}
        for i in licensePlate:
            if i.isalpha():
                d[i.lower()] = d.get(i.lower(), 0) + 1
        
        print(d)
        l = []
        for word in words:
            flag = 0
            for i in d:
                if (i not in word) or ((i in word) and d[i] > word.count(i)):
                    flag = 1
                    break
            if flag == 0:
                l.append(word)

        print(l)
        minLen = float('inf')
        for i in l:
            if len(i) < minLen:
                minLen = len(i)
                word = i
        return word      