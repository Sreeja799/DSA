class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        sum_digits = sum(digits)
        prod_digits = 1
        for i in digits:
            prod_digits *= i
        return prod_digits - sum_digits