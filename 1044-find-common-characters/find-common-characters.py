class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l = list(words[0])

        ans = []
        for i in range(len(l)):
            temp = l[i]
            flag = 0
            for j in range(len(words)):
                if l[i] not in words[j]:
                    flag = 1
                    break
                words[j] = words[j].replace(l[i], '', 1)
                
            if flag == 0:
                ans.append(temp)
        return ans       