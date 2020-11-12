import unittest


class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n

        # Keep track of a value for each direction (each rows and cols, and the the two diagonals)
        self.rows = [0] * self.size
        self.cols = [0] * self.size
        self.topleft_botright = 0
        self.botleft_topright = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        # Add 1 to the corresponding directions for each player1 moves. And -1 for each player2 moves.
        # If at anypoint a row/col/diagonal adds up to the size of the board, we know player1 wins.
        # Player2 is similar.

        value = 0
        if player == 1:
            value = 1
        elif player == 2:
            value = -1

        self.rows[row] += value
        self.cols[col] += value

        if row == col:
            self.topleft_botright += value
        if row == (self.size - 1) - col:
            self.botleft_topright += value

        if self.rows[row] == self.size or self.cols[col] == self.size or \
                (row == col and self.topleft_botright == self.size) or (
                row == (self.size - 1) - col and self.botleft_topright == self.size):
            return 1
        elif self.rows[row] == -self.size or self.cols[col] == -self.size or \
                (row == col and self.topleft_botright == -self.size) or (
                row == (self.size - 1) - col and self.botleft_topright == -self.size):
            return 2

        else:
            return 0


class TestTTT(unittest.TestCase):
    def test_input1(self):
        ttt = TicTacToe(3)
        self.assertEqual(ttt.move(0, 0, 1), 0)
        self.assertEqual(ttt.move(0, 1, 2), 0)
        self.assertEqual(ttt.move(0, 2, 1), 0)
        self.assertEqual(ttt.move(1, 1, 2), 0)
        self.assertEqual(ttt.move(2, 1, 1), 0)
        self.assertEqual(ttt.move(1, 2, 2), 0)
        self.assertEqual(ttt.move(1, 0, 1), 0)
        self.assertEqual(ttt.move(2, 2, 2), 0)
        self.assertEqual(ttt.move(2, 0, 1), 1)


if __name__ == '__main__':
    unittest.main()