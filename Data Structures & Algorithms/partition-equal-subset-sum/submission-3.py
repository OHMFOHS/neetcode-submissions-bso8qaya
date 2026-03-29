class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        memo = {}

        def dfs(i, amount):
            if i < 0:
                return amount == 0
            if (i, amount) in memo:
                return memo[(i,amount)]
            memo[(i, amount)] = dfs(i-1, amount) or dfs(i-1, amount - nums[i])
            return memo[(i, amount)]

        return dfs(len(nums) - 1, target)
        
            
            