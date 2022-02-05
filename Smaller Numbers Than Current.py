class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    m = {}
    for num in nums:
      m[num] = []
    for i in range(len(nums)):
      m[nums[i]].append(i)
    lst = [0] * len(nums)
    nums = sorted(list(set(nums)))
    k = 0
    for i in range(len(nums)):
      for j in m[nums[i]]:
        lst[j] = k
      k += len(m[nums[i]])
    return lst
