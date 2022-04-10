class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lena = len(s)
        for i in range(lena//2):
            tmp = s[i]
            s[i] = s[lena-1-i]
            s[lena-1-i] = tmp