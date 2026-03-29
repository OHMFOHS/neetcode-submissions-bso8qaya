class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] #初始值，可能为负数，所以不能是 0
        curSum = 0

        for n in nums:
            #curSum 表示的是以当前元素结尾的最大子数组和， 先检查是否是负贡献
            #如果是，就从当前 n 重新开始
            if curSum < 0:
                curSum = 0
            curSum += n
            max_sum = max(max_sum, curSum)
        return max_sum