class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRS = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque()
        fresh = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        time = 0
        while fresh > 0 and q:
            l = len(q)
            for _ in range(l):
                curx, cury = q.popleft()
                for dx, dy in DIRS:
                    nx, ny = curx + dx, cury + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append([nx,ny])
            time += 1
        return time if fresh == 0 else -1