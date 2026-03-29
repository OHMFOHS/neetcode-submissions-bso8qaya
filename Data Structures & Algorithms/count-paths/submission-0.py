class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #dfs(i, j) = dfs(i-1, j) +  dfs(i, j-1)
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                memo[(i,j)] = 1
                return 1
            memo[(i,j)] = dfs(i-1, j) + dfs(i, j - 1)
            return memo[(i,j)]
        
        return dfs(m - 1, n - 1)
            
            