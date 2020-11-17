class Solution:
    def alienOrder(self, words) -> str:

        # construct a graph by comparing adjacent words. Add an edge from letter A to B if A < B. 
        def construct_graph(words, adj_list):
            prev_word = None
            for curr_word in words:
                if prev_word:
                    # A special case. If we have a sequence like ['abcd', 'abc'], the sequence is not lexico-ordered
                    # Return false to indicate the input is invalid
                    if len(prev_word) > len(curr_word) and prev_word.startswith(curr_word):
                        return False

                    # Get the first character that is different, and add an edge representing a partial order
                    i = 0
                    for i in range(min(len(prev_word), len(curr_word))):
                        if prev_word[i] != curr_word[i]:
                            if curr_word[i] not in adj_list[prev_word[i]]:
                                adj_list[prev_word[i]].add(curr_word[i])
                            break
                prev_word = curr_word

            return True

        # Do a topological sort based on the indegree of the vertices (kahn's algorithm)
        def topological_sort(adj_list):
            result = []
            queue = []
            in_degree = dict()

            for char in adj_list:
                in_degree[char] = 0

            for char in adj_list:
                for dst in adj_list[char]:
                    in_degree[dst] += 1

            for char in adj_list:
                if in_degree[char] == 0:
                    queue.append(char)

            while len(queue) > 0:
                char = queue.pop(0)
                result.append(char)
                for neighbor in adj_list[char]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            if len(result) != len(adj_list.keys()):
                return ""
            else:
                return "".join(result)

        # Initialize graph
        adj_list = dict()
        for word in words:
            for char in word:
                if char not in adj_list:
                    adj_list[char] = set()

        if not construct_graph(words, adj_list):
            return ""
        else:
            return topological_sort(adj_list)



