class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        f = [0] * (len(t) + 1)
        f[0] = 1
        
        for i in range(len(s)):
            for j in range(len(t) - 1, -1, -1):
                f[j+1] = f[j+1]
                if s[i] == t[j]:
                    f[j+1] += f[j]
        return f[-1]
