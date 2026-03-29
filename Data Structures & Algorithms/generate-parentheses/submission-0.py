class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        ans = []
        def dfs(left, right):
            if left == 0 and right == 0:
                ans.append(''.join(path))
                return
            if left > 0:
                path.append('(')
                dfs(left - 1, right)
                path.pop()
            if right > left:
                path.append(')')
                dfs(left, right - 1)
                path.pop()
        dfs(n,n)
        return ans