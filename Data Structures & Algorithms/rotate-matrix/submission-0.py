class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #水平翻折
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
        #对角线翻折
        for i in range(n):
            for j in range(n - i - 1):
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n-j-1][n-i-1], matrix[i][j]