class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        # Get all the websites visited by each user
        visited_by = dict()
        for i in range(len(username)):
            if username[i] not in visited_by:
                visited_by[username[i]] = [(timestamp[i], website[i])]
            else:
                visited_by[username[i]].append((timestamp[i], website[i]))

        # For each user's visit websites, sort by visited time
        for i in range(len(username)):
            visited_by[username[i]].sort()

        # Get all 3-subseuence, given a user's time-sorted list of visited websites
        def get_all_seq(l):
            def backtrack(prog, start):
                if len(prog) == 3:
                    res.append(tuple(prog))
                    return

                remaining = 3 - len(prog)
                for i in range(start, len(l) - remaining + 1):
                    prog.append(l[i][1])
                    backtrack(prog, i + 1)
                    prog.pop()

            res = []
            backtrack([], 0)
            return res

        sequences = dict()
        max_cnt = 0
        max_seq = None

        # Get all 3 subsequence, and find the one with the maximum user visits
        for usr in visited_by:
            for seq in set(get_all_seq(visited_by[usr])):
                if seq in sequences:
                    sequences[seq] += 1
                else:
                    sequences[seq] = 1

                # Update if current seq has higher count than the max cnt so far,
                # or they are the same but current seq is lexiocographically smaller
                if sequences[seq] > max_cnt or sequences[seq] == max_cnt and seq < max_seq:
                    max_cnt = sequences[seq]
                    max_seq = seq

        return list(max_seq)


Solution().mostVisitedPattern(["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"],
                              [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930],
                              ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"])