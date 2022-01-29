class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        k = 0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if stones[i] == jewels[j]:
                    k +=1
        return k