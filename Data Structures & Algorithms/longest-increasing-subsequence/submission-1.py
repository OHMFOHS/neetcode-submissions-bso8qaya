class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            memo[i] = res + 1
            return res + 1
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))
        return ans
        