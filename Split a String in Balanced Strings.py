class Solution:
    def balancedStringSplit(self, s: str) -> int:
        k = 0
        answ = 0
        for i in range(len(s)):
            if s[i] == "R":
                k += 1
            else:
                k -= 1
            if k == 0:
                answ += 1
        return answ