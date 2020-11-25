import unittest


class Solution:
    # A simple linear time and space algorithm: just perform a DFS on each component
    def countComponents(self, n: int, edges) -> int:
        adj_list = dict()
        for i in range(n):
            adj_list[i] = []

        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        # White means unvisited. Grey means on the DFS recursion stack.
        # Black means visited (when vertex is removed from recursion stack).
        # Technically the grey state is not needed here.

        WHITE = 0
        GREY = 1
        BLACK = 2
        color = [WHITE] * n

        def dfs(root):
            color[root] = GREY
            for neighbor in adj_list[root]:
                if color[neighbor] == WHITE:
                    dfs(neighbor)
            color[root] = BLACK

        count = 0
        for vertex in range(n):
            if color[vertex] == WHITE:
                dfs(vertex)
                count += 1

        return count



class TestComponent(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.countComponents(7, [[1, 2], [3, 1], [2, 4], [5, 6]]), 3)

    def test_input1(self):
        self.assertEqual(self.sol.countComponents(6, [[0, 2], [3, 1], [2, 4], [4, 5]]), 2)


if __name__ == '__main__':
    unittest.main()
