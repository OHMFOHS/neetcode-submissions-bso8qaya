class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float("inf")] * (amount + 1) for _ in range(2)]
        dp[0][0] = 0

        for i, x in enumerate(coins):
            for j in range(amount + 1):
                if j < x:
                    dp[(i+1) % 2][j] = dp[i % 2][j]
                else:
                    dp[(i+1) % 2][j] = min(dp[i % 2][j], dp[(i+1) % 2][j-x] + 1)
        ans = dp[n%2][amount]
        return ans if ans < float("inf") else -1