from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p 是选择正号的数
        # s - p就是选择为负号的数
        # 那么可得 p - (s - p) = target
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        #f[i+1][target] = f[i][target] + f[i][target - nums[i]]

        f = [0] * (target + 1)
        f[0] = 1

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                if nums[i] <= j:
                    f[j] = f[j] + f[j - nums[i]]
        return f[-1]

