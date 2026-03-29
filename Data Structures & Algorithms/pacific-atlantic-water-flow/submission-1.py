class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(x, y, visit, prevHeight):
            if (x,y) in visit or x < 0 or y < 0 or x >= m or y >= n or heights[x][y] < prevHeight :
                return
            visit.add((x,y))
            dfs(x + 1, y, visit, heights[x][y])
            dfs(x - 1, y, visit, heights[x][y])
            dfs(x, y + 1, visit, heights[x][y])
            dfs(x, y - 1, visit, heights[x][y])
        
        for r in range(m):
            dfs(r,0,pac, heights[r][0])
            dfs(r, n - 1, atl, heights[r][n-1])
        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m-1, c, atl, heights[m-1][c])
        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res