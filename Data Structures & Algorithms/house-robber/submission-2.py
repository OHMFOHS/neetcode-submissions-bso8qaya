class Solution:
    def rob(self, nums: List[int]) -> int:
                n = len(nums)
                f0 = f1 = 0
                for i in range(n):
                        tmp = f1
                        f1 = max(f0 + nums[i], f1)
                        f0 = tmp
                return f1