class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row = [set() for _ in range(9)]
        check_col = [set() for _ in range(9)]
        check_box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                if c in check_row[i] or c in check_col[j] or c in check_box[(i//3)*3 + j // 3]:
                    return False
                check_row[i].add(c)
                check_col[j].add(c)
                check_box[(i//3)*3 + j // 3].add(c)
        return True

