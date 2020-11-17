class Solution:
    def isBipartite(self, graph) -> bool:
        vertex_side = dict()
        used_edges = set()

        # Do a DFS starting at src, marking each node as either on the left (side=0) or right side (side=1)
        # The DFS visits a vertex, marking its side, then recurse to any node reachable using a yet-used edge
        def backtracking(src, side):
            # If the node has been visited and marked with a side before,
            # and the side enforced by propagation is not the same, the graph can't be bipartite
            if src in vertex_side and side != vertex_side[src]:
                return False

            vertex_side[src] = side
            for dst in graph[src]:
                used = (src, dst) in used_edges or (dst, src) in used_edges
                if not used:
                    used_edges.add((src, dst))
                    res = backtracking(dst, (side + 1) % 2)
                    if not res:
                        return False
            return True

        for src in range(len(graph)):
            # Do backtracking on each disconnect component
            if src not in vertex_side:
                if not backtracking(src, 0):
                    return False

        return True
