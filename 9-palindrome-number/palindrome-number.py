class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)[::-1]
        return str(x) == temp