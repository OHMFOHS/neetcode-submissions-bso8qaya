class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        f = [[-1] * (target + 1) for _ in range(len(nums))]
        f[0][0] = True
        for j in range(1, target + 1):
            f[0][j] = False
        for i in range(1, len(nums)):
            for amount in range(target + 1):
                if amount < nums[i]:
                    f[i][amount] = f[i-1][amount]
                else:
                    f[i][amount] = f[i-1][amount] or f[i-1][amount - nums[i]]
        return f[len(nums)-1][target]
        
        
            
            