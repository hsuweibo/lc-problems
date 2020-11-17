class Solution:
    # A linear time, linear space solution
    def calcEquation(self, equations, values, queries):
        # Construct a graph out of the given input.
        # In particular, add two edges for every entry in equations
        # If (A, B) is an entry, add an edge from A to B, with value values[i],
        # and another edge from B to A, with value 1/values[i]
        adj_list = dict()
        for i in range(len(equations)):
            edge = equations[i]
            dividend = edge[0]
            divisor = edge[1]
            if dividend in adj_list:
                adj_list[dividend].add((divisor, values[i]))
            else:
                adj_list[dividend] = set()
                adj_list[dividend].add((divisor, values[i]))

            if divisor in adj_list:
                adj_list[divisor].add((dividend, 1 / values[i]))
            else:
                adj_list[divisor] = set()
                adj_list[divisor].add((dividend, 1 / values[i]))

        vertices = adj_list.keys()
        visited = set()

        # Perform a DFS at the src vertex, and visit all vertex in this component
        # As we visit each vertex V, we mark V as visited, and calculate src divided by V
        # We store this result in div_res
        # We also store which component V belongs in, by storing src in src_map
        def dfs(root, visited, mult, div_res, src_map, src):
            visited.add(root)
            div_res[root] = mult
            src_map[root] = src

            for edge in adj_list[root]:
                vertex = edge[0]
                value = edge[1]
                if vertex not in visited:
                    dfs(vertex, visited, mult * value, div_res, src_map, src)

        src_map = dict()
        div_table = dict()
        for vertex in vertices:
            # For each vertex V1, we visit all vertex V2 in the same component and calculate V1/V2.
            # The result is stored in div_table
            if vertex not in visited:
                div_res = dict()
                dfs(vertex, visited, 1, div_res, src_map, vertex)
                div_table[vertex] = div_res

        res = [0] * len(queries)
        for i in range(len(queries)):
            qry = queries[i]
            dividend = qry[0]
            divisor = qry[1]

            if dividend not in vertices or divisor not in vertices:
                res[i] = -1.0
            else:
                dividend_src = src_map[dividend]
                divisor_src = src_map[divisor]
                if dividend_src != divisor_src:
                    res[i] = -1.0
                else:
                    src = dividend_src
                    src_divided_by_dividend = div_table[src][dividend]
                    src_divided_by_divisor = div_table[src][divisor]
                    res[i] = src_divided_by_divisor / src_divided_by_dividend
        return res
