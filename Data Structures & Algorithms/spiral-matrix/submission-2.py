class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            if top > bottom or left > right:
                break

            for j in range(right, left - 1, -1):
                ans.append(matrix[bottom][j])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        return ans