class Solution:
    def reverseWords(self, s: str) -> str:
        s2 = []
        s_answ = []
        s = list(s)
        for elem in s:
            if elem != " ":
                s2.append(elem)
            else:
                s_answ += s2[::-1]
                s_answ.append(" ")
                s2.clear()
        s_answ += s2[::-1]
        return ''.join(s_answ)