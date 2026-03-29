class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxLen = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                #两边相等并且长度 <= 3就一定回文
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if dp[i][j] and j - i + 1 > maxLen:
                        start = i
                        maxLen = j - i + 1
        return s[start: start + maxLen]
