class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        fmax = nums[0]
        fmin = nums[0]
        #初始化成nums[0],因为之后的遍历从 1开始，防止漏掉 0
        ans = nums[0]
        for i in range(1, n):
            #同时更新，防止更新 fmin 的时候，fmax 被更新过了
            fmax, fmin = max(nums[i], fmax * nums[i], fmin * nums[i]), min(nums[i], fmax * nums[i], fmin * nums[i])
            ans = max(ans, fmax)
        return ans