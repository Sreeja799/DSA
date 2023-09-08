# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        x = rand7() - 1
        y = rand7()
        s = x*7 + y

        if s <= 40:
            return s % 10 + 1
        return self.rand10()