class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answ = ""
        k = 0
        i = 0
        for j in range(len(s)):
            if s[j] == "(":
                k += 1
            else:
                k -= 1
                if k == 0:
                    answ += s[i+1:j] 
                    i = j + 1
        return answ