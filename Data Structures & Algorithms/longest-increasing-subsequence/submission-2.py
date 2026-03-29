from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []
        for num in nums:
            i = bisect_left(g, num)
            if i < len(g):
                g[i] = num
            else:
                g.append(num)
        return len(g)