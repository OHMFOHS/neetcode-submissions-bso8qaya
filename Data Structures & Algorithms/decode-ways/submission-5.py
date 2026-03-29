class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = dp2 = 0
        dp1 = 1
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        #最后会把 dp1 变成刚算完的 dp，所以这里返回 dp1
        return dp1


        


