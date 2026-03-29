from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dfs(i, amount) = dfs(i-1, amount) + dfs(i, amount - coins[i])
        @cache
        def dfs(i, amount):
            if i < 0:
                return 1 if amount == 0 else 0
            if coins[i] > amount:
                return dfs(i-1, amount)
            return dfs(i-1, amount) + dfs(i, amount - coins[i])
        return dfs(len(coins) - 1, amount)
