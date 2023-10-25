class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for i in chars:
            d[i] = d.get(i, 0) + 1

        sum = 0
        for word in words:
            flag = 0
            for i in word:
                if (i not in d) or ((i in d) and d[i] < word.count(i)):
                    flag = 1
                    break
            if flag == 0:
                sum += len(word)
        return sum        