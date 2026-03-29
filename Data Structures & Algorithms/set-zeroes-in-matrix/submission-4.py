class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row_0 = False
        col_0 = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_0 = True
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                row_0 = True
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if col_0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if row_0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0