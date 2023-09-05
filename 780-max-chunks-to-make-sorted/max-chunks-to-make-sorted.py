class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunkCount = 0
        expectedSum = 0
        currSum = 0

        for i in range(len(arr)):
            expectedSum += i
            currSum += arr[i]

            if (currSum == expectedSum):
                chunkCount += 1
        return chunkCount        