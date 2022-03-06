class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                x = nums[i]
                return x