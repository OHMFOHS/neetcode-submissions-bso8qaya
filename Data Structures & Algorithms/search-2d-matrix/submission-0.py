class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left = -1
        right = m * n
        while left + 1 < right:
            mid = left + (right - left) // 2
            r = mid // n
            c = mid % n
            if matrix[r][c] >= target:
                right = mid
            else:
                left = mid
        ans_r = right // n
        ans_c = right % n
        return True if right != m * n and matrix[ans_r][ans_c] == target else False