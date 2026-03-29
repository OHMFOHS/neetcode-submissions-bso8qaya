class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        f = [False] * (target + 1)
        f[0] = True

        for i in range(len(nums)):
            for j in range(target, -1, -1):
                if nums[i] <= j:
                    f[j] = f[j - nums[i]] or f[j]

        return f[target]
        

        
        
            
            