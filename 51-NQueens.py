
class Solution:
    def solveNQueens(self, n: int):
        ret = []

        def place_queen(board, row, col, from_left, from_right, from_above):
            # Place the queen
            board[row][col] = 'Q'

            # Calculate the new greyed_out columns for the next row
            new_from_left = [False for i in range(len(from_left))]
            new_from_right = [False for i in range(len(from_right))]
            new_from_above = from_above[:]
            new_from_above[col] = True

            for i in range(1, len(from_left)):
                new_from_left[i] = from_left[i - 1]
            if col < len(from_left) - 1:
                new_from_left[col + 1] = True

            for i in range(len(from_right) - 1):
                new_from_right[i] = from_right[i + 1]
            if col > 0:
                new_from_right[col - 1] = True

            return new_from_left, new_from_right, new_from_above

        # The reverse of place_queen
        def remove_queen(board, row, col):
            board[row][col] = '.'

        # from_left, from_right, and from_above are columns that are greyed out because of a previously positioned queen
        # from_left[j] would mean board[row][j] can't be a queen due to a previous queen placed diagonally top left.
        def backtrack(board, from_left, from_right, from_above, row):
            if row == n:
                ret.append(["".join(board[i]) for i in range(n)])
            else:
                for col in range(n):
                    if not from_left[col] and not from_right[col] and not from_above[col]:
                        # Place queen and calculate the new greyed out columns for the next row
                        new_left, new_right, new_above = place_queen(board, row, col, from_left, from_right, from_above)

                        backtrack(board, new_left, new_right, new_above, row + 1)

                        # Remove the queen
                        remove_queen(board, row, col)

        backtrack([["."] * n for i in range(n)], [False] * n, [False] * n, [False] * n, 0)
        return ret



print(Solution().solveNQueens(4))

