class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        DIRS = {(0,1), (0,-1), (1,0), (-1,0)}
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        def dfs(x, y):
            if memo[x][y] != 0:
                return memo[x][y]
            res = 1 #默认长度是 1 
            for dx, dy  in DIRS:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    res = max(res, 1 + dfs(nx, ny))
            memo[x][y] = res
            return res
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))
        return ans