import unittest


class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        adj_list = dict()

        for i in range(1, N + 1):
            adj_list[i] = set()

        for edge in dislikes:
            v1 = edge[0]
            v2 = edge[1]
            adj_list[v1].add(v2)
            adj_list[v2].add(v1)

        # A dict that keep tracks of the color of each vertex. Also used to keep track of which vertex has been visited.
        color = dict()

        for i in range(1, N + 1):
            # Do a BFS on vertex i, if i has not been not visited before
            if i not in color:
                # The '#' in the queue is a pseudo-vertex (a marker).
                # when it is popped off, the depth of the search tree has increase by 1
                color[i] = 0
                queue = [i, '#']

                curr_color = 0
                while len(queue) > 1:
                    vertex = queue.pop(0)

                    if vertex == '#':
                        curr_color = (curr_color + 1) % 2
                        queue.append('#')
                        continue

                    for neighbor in adj_list[vertex]:
                        if neighbor in color:
                            if (curr_color + 1) % 2 != color[neighbor]:
                                return False
                        else:
                            color[neighbor] = (curr_color + 1) % 2
                            queue.append(neighbor)

        return True


class TestPossibleBipartitions(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertFalse(self.sol.possibleBipartition(5, [[1, 2], [3, 4], [4, 5], [3, 5]]))

    def test_input2(self):
        self.assertFalse(self.sol.possibleBipartition(3, [[1, 2], [2, 3], [1, 3]]))

    def test_input3(self):
        self.assertTrue(self.sol.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))

if __name__ == '__main__':
    unittest.main()