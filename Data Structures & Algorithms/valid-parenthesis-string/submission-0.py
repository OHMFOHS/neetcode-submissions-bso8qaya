from functools import cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        #open 代表还有多少没匹配的 (
        @cache
        def dfs(i, open):
            if open < 0:
                return False
            #匹配完，并且 open 刚好为 0，才返回 True
            if i == n:
                return open == 0
            
            if s[i] == '(':
                return dfs(i+1, open + 1)
            elif s[i] == ')':
                return dfs(i+1, open - 1)
            else:
                return dfs(i + 1, open) or dfs(i+1, open + 1) or dfs(i+1, open - 1)
        return dfs(0,0)

            

