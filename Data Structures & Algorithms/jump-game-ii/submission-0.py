from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            if i > len(nums) - 1:
                return float("inf")
            ans = float("inf")
            for step in range(1, nums[i] + 1):
                ans = min(ans, 1 + dfs(i+step))
            return ans

        return dfs(0)
        
