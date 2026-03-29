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
            #判断当前i，j位置是否能匹配上
            match = i < m and (s[i] == p[j] or p[j] == '.')
            if (j+1) < n and p[j+1] == '*':
                #如果碰到'*'有两个选择，一个是不用，一个是用，分别对应 dfs(i, j+2) 和 dfs(i+1, j) 注意要用的话需要匹配才能
                return dfs(i, j+2) or (match and dfs(i+1, j))
            if match: #如果没有*, 就正常匹配
                return dfs(i+1, j+1)
            return False
        
        return dfs(0,0)