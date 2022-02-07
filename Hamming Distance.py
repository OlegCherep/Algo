class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        lst = list(format(x ^ y, 'b'))
        k = 0
        for i in range(len(lst)):
            if lst[i] == '1':
                k += 1
        return k
