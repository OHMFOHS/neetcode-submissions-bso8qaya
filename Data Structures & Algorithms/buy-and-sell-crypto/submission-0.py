class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        ans = 0
        for p in prices:
            if p < min_p:
                min_p = p
            ans = max(ans, p - min_p)
        return ans