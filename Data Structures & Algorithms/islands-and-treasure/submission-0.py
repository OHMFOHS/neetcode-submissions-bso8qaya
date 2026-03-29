class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        q = deque()
        DIRS = [[0,1], [0,-1], [-1, 0], [1,0]]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])

        while q:
            l = len(q)
            for _ in range(l):
                curx, cury = q.popleft()
                for dx, dy in DIRS:
                    nx, ny = curx + dx, cury + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == inf:
                        grid[nx][ny] = grid[curx][cury] + 1
                        q.append([nx,ny])
        


