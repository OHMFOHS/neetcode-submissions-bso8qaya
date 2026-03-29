class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        #是否包含 0 存在第一行和第一列，要区分第一行列没有 0 的情况，所有单独创建
        #两个变量表示原本是否有 0
        first_row_0 = first_col_0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_0 = True
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_0 = True
 
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_0:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_0:
            for i in range(m):
                matrix[i][0] = 0
        