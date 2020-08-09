# 编写一个程序，通过已填充的空格来解决数独问题。

# 一个数独的解法需遵循如下规则：

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 空白格用 '.' 表示。
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def solve(board):
            for row in range(len(board)):
                for col in range(len(board[0])):

                    if board[row][col] == '.':
                        candidates = self.find_candidates(board, row, col)

                        for c in candidates:
                            board[row][col] = c
                            if solve(board):
                                return True

                            board[row][col] = '.'

                        return False
            return True

        solve(board)

    def find_candidates(self, board, row, col):
        potential = list(map(str, list(range(1, 10))))
        candidates = [i for i in potential]

        col_vals = []
        for i in range(len(board[0])):
            if board[row][i].isdigit():
                col_vals.append(board[row][i])

        row_vals = []
        for i in range(len(board)):
            if board[i][col].isdigit():
                row_vals.append(board[i][col])

        square_vals = []
        r, c = row // 3 * 3, col // 3 * 3
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if board[i][j].isdigit():
                    square_vals.append(board[i][j])

        for p in potential:
            if p in col_vals:
                candidates.remove(p)
            elif p in row_vals:
                candidates.remove(p)
            elif p in square_vals:
                candidates.remove(p)

        return candidates