class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for elem in nums:
            ans = ans ^ elem
        return ans
