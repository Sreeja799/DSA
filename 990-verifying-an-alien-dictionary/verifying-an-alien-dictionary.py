class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            m = min(len(words[i]), len(words[i+1]))
            for j in range(m):
                if order.find(words[i][j]) < order.find(words[i+1][j]):
                    break
                elif order.find(words[i][j]) > order.find(words[i+1][j]):
                    print(i, j)
                    return False
                elif words[i].startswith(words[i+1]) and len(words[i]) > len(words[i+1]):
                    return False
        
        return True        