class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = []
        for i in range(left, right+1):
            k = 0
            for j in str(i):
                if int(j) != 0 and i % int(j) == 0:
                    k += 1
            if len(str(i)) == k:
                lst.append(i)
        return lst