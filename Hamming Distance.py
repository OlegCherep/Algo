class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = list(format(x, 'b'))
        b = list(format(y, 'b'))
        n1 = a[::-1]
        n2 = b[::-1]
        if len(n1) > len(n2):
            for i in range(len(n1) - len(n2)):
                n2.append('0')
        else:
            for i in range(len(n2) - len(n1)):
                n1.append('0')
        k = 0
        for i in range(len(n1)):
            if n1[i] != n2[i]:
                k += 1
        return k