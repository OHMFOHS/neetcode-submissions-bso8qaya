from functools import cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dfs(i):
            if i >= len(nums)-1:
                return True
            for length in range(1, nums[i] + 1):
                if dfs(i + length):
                    return True
            return False
        return dfs(0)