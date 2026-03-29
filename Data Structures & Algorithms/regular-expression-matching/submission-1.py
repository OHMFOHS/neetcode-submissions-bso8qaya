from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        @cache
        def dfs(i, j):
            if i >= m and j >= n:
                return True
            if j >= n:
                return False
            
            match = i < m and (s[i] == p[j] or p[j] == '.')
            if (j+1) < n and p[j+1] == '*':
                return dfs(i, j+2) or (match and dfs(i + 1, j))
            
            if match:
                return dfs(i+1, j+1)
            return False
        return dfs(0,0)

