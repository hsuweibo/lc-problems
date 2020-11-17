import unittest

class Solution:
    def findItinerary(self, tickets):

        # An adjacency list. Each item in the list is a list: [dest, used].
        # The used field tracks whether or not the edge is used in the current path during DFS
        adj_list = dict()
        for i in range(len(tickets)):
            edge = tickets[i]
            if edge[0] in adj_list:
                adj_list[edge[0]].append([edge[1], False])
            else:
                adj_list[edge[0]] = [[edge[1], False]]

        # sort each adj list based on the dest's lexical order
        for src in adj_list:
            adj_list[src].sort(key=lambda item: item[0])

        def dfs(start, length):
            if length == len(tickets):
                return [start]
            if start not in adj_list:
                return None

            # For each adj edge, find one that has not been used yet, and recurse
            for edge_item in adj_list[start]:
                if not edge_item[1]:
                    edge_item[1] = True
                    res = dfs(edge_item[0], length + 1)
                    edge_item[1] = False
                    if res is not None:
                        res.insert(0, start)
                        return res

            return None

        used = [False] * len(tickets)
        return dfs("JFK", 0)


class TestFindItinerary(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]),
                         ["JFK", "MUC", "LHR", "SFO", "SJC"])

    def test_input2(self):
        self.assertEqual(
            self.sol.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]),
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])


if __name__ == '__main__':
    unittest.main()