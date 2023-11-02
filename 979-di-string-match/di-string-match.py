class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        arr = [i for i in range(n+1)]
        l = [0 for i in range(n+1)]

        for i in range(len(s)):
            if s[i] == 'D':
                l[i] = max(arr)
                arr.remove(max(arr))
        
        for i in range(len(l)):
            if l[i] == 0 and len(arr) > 0:
                l[i] = arr[0]
                arr.pop(0)
        return l