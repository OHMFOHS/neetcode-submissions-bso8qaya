class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            n = len(nums)
            f0 = f1 = 0
            for i in range(n):
                    tmp = f1
                    f1 = max(f0 + nums[i], f1)
                    f0 = tmp
            return f1
        return max(nums[0] + rob1(nums[2:-1]), rob1(nums[1:]))