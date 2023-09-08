class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for i in range(left, right+1):
            flag = 0
            digits = [int(j) for j in str(i)]
            for k in digits:
                if k == 0 or i % k != 0:
                    flag = 1
                    break
            if flag == 0:
                l.append(i)
            
        return l