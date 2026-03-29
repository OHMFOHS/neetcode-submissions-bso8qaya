class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        n = len(nums) + 1
        for i in range(n + 1):
            cnt[i] = 0
        for num in nums:
            cnt[num] += 1
        for i in range(n + 1):
            if cnt[i] == 0:
                return i
            
        
            