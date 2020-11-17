
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        def dfs(root, cache):
            if root.val in cache:
                return cache[root.val]

            new_node = Node(root.val)
            cache[root.val] = new_node

            new_neighbors = []
            for node in root.neighbors:
                new_neighbors.append(dfs(node, cache))

            if len(new_neighbors) > 0:
                new_node.neighbors = new_neighbors

            return new_node

        if not node:
            return None
        else:
            cache = dict()
            return dfs(node, cache)