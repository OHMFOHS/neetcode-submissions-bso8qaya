class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        f = [0] * n
        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            f[i] = max(f[i-2] + nums[i], f[i-1])
        return f[-1]
  