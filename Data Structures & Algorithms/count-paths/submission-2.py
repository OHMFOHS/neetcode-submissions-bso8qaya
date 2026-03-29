class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        for _ in range(m):
            for j in range(n):
                #注意要特判 i = 1, j = 1的情况，不然会被覆盖
                if j == 0:
                    continue
                dp[j+1] = dp[j+1] + dp[j]
        return dp[n]