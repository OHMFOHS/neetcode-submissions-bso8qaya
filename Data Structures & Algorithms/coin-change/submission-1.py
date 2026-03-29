class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float("inf")] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i, x in enumerate(coins):
            for j in range(amount + 1):
                if j < x:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = min(dp[i][j], dp[i+1][j-x] + 1)
        ans = dp[n][amount]
        return ans if ans < float("inf") else -1