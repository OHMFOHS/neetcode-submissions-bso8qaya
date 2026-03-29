class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, hold):
            if i < 0:
                memo[(i, hold)] = -float("inf") if hold else 0
                return memo[(i, hold)]
            if hold:
                memo[(i, hold)] = max(dfs(i-1, 1), dfs(i-2,0) - prices[i])
                return memo[(i, hold)]
            memo[(i, hold)] = max(dfs(i-1, 0), dfs(i-1,1) + prices[i])
            return memo[(i, hold)]
        return dfs(len(prices) - 1, 0)
        