class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] == 0:
                            continue
                        matrix[k][j] = float("inf")
                    for l in range(n):
                        if matrix[i][l] == 0:
                            continue
                        matrix[i][l] = float("inf")
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0