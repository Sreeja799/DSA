class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divCount(n):
            div = []
            count = 0
            for i in range(1, int(n**0.5)+1):
                if n % i == 0:
                    if i != (n//i):
                        count += 2
                        div.append(i)
                        div.append(n//i)
                    else:
                        count += 1
                        div.append(i)
                    if count > 4:
                        return 0, []
            return count, div

        sum_ = 0
        for i in nums:
            count, div = divCount(i)
            if count == 4:
                sum_ += sum(div)
        return sum_