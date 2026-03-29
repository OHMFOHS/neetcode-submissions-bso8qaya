class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = []#col记录每一行的皇后位置
        
        def valid(r,c):
            for R in range(r):
                C = col[R]
                if r + c == R + C or r - c == R - C:
                    return False
            return True
        
        # r, s 表示当前行 r，可用列集合 s
        def dfs(r,s):
            #已经全部放完
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - c -1 ) for c in col])
            for c in s:
                if valid(r,c):
                    #记录这一行放 c 位置
                    col.append(c)
                    #到下一行， 这一列不再可用
                    dfs(r+1, s-{c})
                    col.pop()
        #传入第 0 行，和 0-n-1表示能用的列
        dfs(0, set(range(n)))
        return ans