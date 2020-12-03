import unittest

class Solution:
    def brute_force_updateMatrix(self, matrix):
        # Do a single-source BFS algorithm at each grid position with a 1.
        def find_dist(row, col):
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            visited = set()
            marker = '#'
            queue = [(row, col), marker]
            visited.add((row, col))
            level = 0

            while len(queue) > 0:
                curr = queue.pop(0)
                if curr == marker:
                    level += 1
                    if len(queue) > 0:
                        queue.append(marker)
                else:
                    curr_r, curr_c = curr
                    if matrix[curr_r][curr_c] == 0:
                        return level

                    for dir in directions:
                        next_r = curr_r + dir[0]
                        next_c = curr_c + dir[1]
                        if is_inbound(next_r, next_c) and (next_r, next_c) not in visited:
                            visited.add((next_r, next_c))
                            queue.append((next_r, next_c))

        def is_inbound(row, col):
            return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])

        dist = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dist[i][j] = find_dist(i, j)

        return dist

    # A multi-source BFS, where level 0 contains all the grid positions with a 0
    def updateMatrix(self, matrix):
        def is_inbound(row, col):
            return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dist = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]
        marker = '#'
        queue = []
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        queue.append(marker)
        level = 0

        while len(queue) > 0:
            curr = queue.pop(0)
            if curr == marker:
                level += 1
                if len(queue) > 0:
                    queue.append(marker)
            else:
                curr_r, curr_c = curr
                dist[curr_r][curr_c] = level
                for dir in directions:
                    next_r = curr_r + dir[0]
                    next_c = curr_c + dir[1]
                    if is_inbound(next_r, next_c) and (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        queue.append((next_r, next_c))
        return dist


class Test01Matrix(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]), [[0, 0, 0], [0, 1, 0], [1, 2, 1]])


if __name__ == '__main__':
    unittest.main()