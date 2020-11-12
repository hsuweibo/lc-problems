DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # Given an index pair where board[r][c] == 0, do a DFS and return whether the containing region is surrounded by 'X'
        def is_surrounded(board, r, c, region):
            region.add((r, c))

            # check if at borders
            if r == 0 or r == len(board) - 1 or c == 0 or c == len(board[0]) - 1:
                return False

            for d in DIRECTIONS:
                next_r = r + d[0]
                next_c = c + d[1]
                # recursive explore any neighbor that has an 'O', has not been explored before, and is within valid bound.
                if next_r >= 0 and next_r < len(board) and next_c >= 0 and next_c < len(board[0]) \
                        and board[next_r][next_c] == 'O' and (next_r, next_c) not in region:
                    if not is_surrounded(board, next_r, next_c, region):
                        return False

            return True

        # visited is holds the set of coodinates that was originally 'O', and has at the current point been visited.
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    region = set()
                    if is_surrounded(board, i, j, region):
                        for (r, c) in region:
                            board[r][c] = 'X'

                    visited = visited.union(region)
