class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        l = []
        for i in image:
            l.append(i[::-1])
        
        for i in range(len(l)):
            for j in range(len(l)):
                l[i][j] = 1 if l[i][j] == 0 else 0
        return l      