import heapq
import unittest


class Solution:
    def minCost(self, costs) -> int:
        if len(costs) == 0:
            return 0

        for row in range(1, len(costs)):
            # hard code the cases
            for col in range(3):
                if col == 0:
                    smallest = min(costs[row - 1][col + 1], costs[row - 1][col + 2])
                elif col == 1:
                    smallest = min(costs[row - 1][col - 1], costs[row - 1][col + 1])
                else:
                    smallest = min(costs[row - 1][col - 1], costs[row - 1][col - 2])

                costs[row][col] += smallest

        return min(costs[-1])


class TestPaintHouse(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]), 10)



if __name__ == '__main__':
    unittest.main()