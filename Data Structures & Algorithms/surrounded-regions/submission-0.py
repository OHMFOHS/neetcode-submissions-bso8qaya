class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return
            board[x][y] = 'T'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        for r in range(m):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][n-1] == 'O':
                dfs(r, n-1)
        
        for c in range(n):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[m-1][c] == 'O':
                dfs(m-1, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'