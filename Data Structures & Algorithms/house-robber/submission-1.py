class Solution:
    def rob(self, nums: List[int]) -> int: 
        n = len(nums)
        if n < 2:
            return nums[0]      
        f0 = nums[0]
        f1 = max(nums[0], nums[1])
        for i in range(2, n):
            tmp = f1
            f1 = max(f0 + nums[i], f1)
            f0 =tmp
        return f1