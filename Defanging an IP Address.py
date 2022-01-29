
class Solution:
    def defangIPaddr(self, address: str) -> str:
        lst = list(address)
        for i in range(len(lst)):
            if lst[i] == ".":
                lst[i] = "[.]"
        return ''.join([str(i) for i in lst])
        
