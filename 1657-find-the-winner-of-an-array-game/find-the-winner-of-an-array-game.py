class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        curr = arr[0]
        streak = 0
        m = max(arr)

        for i in range(1, n):
            if curr > arr[i]:
                streak += 1
            else:
                curr = arr[i]
                streak = 1

            if streak == k or curr == m:
                return curr