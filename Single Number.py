class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answ = 0
        m = {}
        for num in nums:
            m[num] = 0
        for num in nums:
             m[num] += 1
        for num in nums:
            if m[num] == 1:
                answ = num
        return answ