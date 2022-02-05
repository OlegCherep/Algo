class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)-len(nums)//2):
            freq = nums[2*i]
            val = nums[2*i+1]
            for j in range(freq):
                lst.append(val)
        return lst