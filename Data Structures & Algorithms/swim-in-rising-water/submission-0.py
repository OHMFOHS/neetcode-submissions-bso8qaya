class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        visited = set((0,0))
        DIRS = [[0,1], [0,-1],[-1,0],[1,0]]

        while minHeap:
            cur_t, cur_x, cur_y = heapq.heappop(minHeap)
            if cur_x == n - 1 and cur_y == n - 1:
                return cur_t
            for dx, dy in DIRS:
                nx, ny = cur_x + dx, cur_y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
                    new_t = max(cur_t, grid[nx][ny])
                    heapq.heappush(minHeap, [new_t, nx, ny])
                    visited.add((nx, ny))
        