class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        orig = arr[:]
        n = len(arr)
        win_count = 0
        winner = -1
        runs = 0

        while win_count != k:
            if runs > 100000:
                return winner
            if arr[0] > arr[1]:
                if winner == arr[0]:
                    win_count += 1
                else:
                    win_count = 1
                    winner = arr[0]
                temp = arr[1]
                arr.pop(1)
                arr.append(temp)
                

            else:
                if winner == arr[1]:
                    win_count += 1
                else:
                    win_count = 1
                    winner = arr[1]
                temp = arr[0]
                arr.pop(0)
                arr.append(temp)
            runs += 1

        return winner