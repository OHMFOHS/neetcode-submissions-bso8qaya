class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        q_pacific = deque()
        q_atlantic = deque()
        DIRS = [[0,1],[0,-1], [-1,0],[1,0]]
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        for i in range(m):
            q_pacific.append([i,0])
            q_atlantic.append([i,n-1])
            pacific[i][0] = True
            atlantic[i][n-1] = True
        for j in range(n):
            q_pacific.append([0,j])
            q_atlantic.append([m-1, j])
            pacific[0][j] = True
            atlantic[m-1][j] = True


        def bfs(q, ocean):
            while q:
                l = len(q)
                for _ in range(l):
                    curx, cury = q.popleft()
                    for dx, dy in DIRS:
                        nx, ny = curx + dx, cury + dy
                        if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[curx][cury] and ocean[nx][ny] != True:
                            ocean[nx][ny] = True
                            q.append([nx,ny])
        bfs(q_pacific, pacific)
        bfs(q_atlantic, atlantic)
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
        return res




        