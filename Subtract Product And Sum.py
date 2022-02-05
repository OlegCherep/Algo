class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        prod = 1
        sum = 0
        for i in range(len(n)):
            x = int(n[i])
            prod *= x
            sum += x
        return prod - sum  