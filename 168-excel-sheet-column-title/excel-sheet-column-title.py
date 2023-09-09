class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s = ''

        while columnNumber:
            s = alpha[(columnNumber % 26)-1] + s
            columnNumber = (columnNumber - 1) // 26
        
        return s