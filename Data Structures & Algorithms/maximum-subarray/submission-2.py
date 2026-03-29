class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")
        pre_sum = 0
        min_pre_sum = 0
        for n in nums:
            pre_sum += n
            ans = max(ans, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)
        return ans