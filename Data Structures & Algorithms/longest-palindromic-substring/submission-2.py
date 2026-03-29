class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        start = 0
        maxLen = 0
        dp = [[False] * n for  _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for lens in range(1, n + 1):
            for i in range(0, n - lens + 1):
                j = i + lens - 1
                if s[i] == s[j] and (lens <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if dp[i][j] and lens > maxLen:
                        maxLen = lens
                        start = i
        return s[start:start + maxLen]
        