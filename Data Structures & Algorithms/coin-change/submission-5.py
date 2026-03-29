class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = float("inf")
            for c in coins:
                if amount - c >= 0:
                    res = min(res, dfs(amount - c) + 1)
            memo[amount] = res
            return res
        minCoins = dfs(amount)
        return minCoins if minCoins < float("inf") else -1