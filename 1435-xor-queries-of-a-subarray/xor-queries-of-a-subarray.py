class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
      prefix = [arr[0]]

      for i in range(1, len(arr)):
        prefix.append((prefix[i-1]) ^ (arr[i]))
      
      l = []
      for query in queries:
        if query[0] == 0:
          l.append(prefix[query[1]])
        else:
          l.append(prefix[query[0] - 1] ^ prefix[query[1]])
      return l
        