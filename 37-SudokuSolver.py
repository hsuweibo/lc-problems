import unittest

class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Given a row and col, return the next logical position
        def next(row, col):
            if col == 8:
                return row + 1, 0
            else:
                return row, col + 1

        # Test if the given position is the end position
        def reach_end(row, col):
            return row == 9 and col == 0

        def backtrack(row, col):
            # Find next empty cell, unless we reached end
            while not reach_end(row, col) and board[row][col] != ".":
                row, col = next(row, col)

            # No more empty cells. Board is solved, return true.
            if reach_end(row, col):
                return True

            for num in range(1, 10):
                if not row_set[row][num] and not col_set[col][num] and not square_set[get_square(row, col)][num]:
                    for s in [row_set[row], col_set[col], square_set[get_square(row, col)]]:
                        s[num] = True

                    board[row][col] = str(num)
                    if backtrack(row, col):
                        return True
                    board[row][col] = "."

                    for s in [row_set[row], col_set[col], square_set[get_square(row, col)]]:
                        s[num] = False

            return False

        # Get the square index of a position
        def get_square(row, col):
            return (row // 3 * 3) + col // 3

        # These are use to store for each row, square, and column, which numbers are present. #
        # col_set[i][j] == True would mean the number j is already present in the i'th column
        # The first index (e.g., col_set[i][0]) is always False.
        square_set = [[False] * 10 for i in range(9)]
        row_set = [[False] * 10 for i in range(9)]
        col_set = [[False] * 10 for i in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num = int(board[row][col])
                    row_set[row][num] = True
                    col_set[col][num] = True
                    square_set[get_square(row, col)][num] = True

        backtrack(0, 0)


class TestSolver(unittest.TestCase):
    def test_input1(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        answer = [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                  ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                  ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                  ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                  ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
        Solution().solveSudoku(board)
        self.assertEqual(board, answer)


if __name__ == '__main__':
    unittest.main()