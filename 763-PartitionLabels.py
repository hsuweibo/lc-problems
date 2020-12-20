class Solution:
    # my first solution: linear time linear space solution
    def my_partitionLabels(self, S: str):
        def ind(ch):
            return ord(ch) - ord('a')

        # Maintain the index of the first occurence of each character
        first = [None] * 26

        # Maintain the start index of each partition, with start_stack[-1] being the start of the most recent partition
        start_stack = []

        end = 0
        while end < len(S):
            if first[ind(S[end])] is None:
                first[ind(S[end])] = end
                start_stack.append(end)
            else:
                # If the current char appeared before, get its first appeared index,
                # and pop existing partitions off from stack until the char's first appearance is in the latest partition
                first_occur_at = first[ind(S[end])]
                while first_occur_at < start_stack[-1]:
                    start_stack.pop()

            end += 1

        ret = []
        for i in range(1, len(start_stack)):
            ret.append(start_stack[i] - start_stack[i - 1])
        ret.append(len(S) - start_stack[-1])

        return ret

    def partitionLabels(self, S):
        def ind(ch):
            return ord(ch) - ord('a')

        last = [None] * 26
        for i, c in enumerate(S):
            last[ind(c)] = i

        ret = []
        # S[start] .. S[end] represents the current window
        start, end = 0, 0
        for curr in range(len(S)):
            last_occured_at = last[ind(S[curr])]
            # for the current character, which lies in S[start]...S[end], merge the
            # interval S[curr], ..., S[last_occurred_at] with S[start]...S[end] by extending end to last_occurred_at
            end = max(end, last_occured_at)

            # curr == end would signify that for all char before curr, those chars' last positions are all before curr.
            # So S[start]...S[end] would now form a partition that is as small as possible.
            if curr == end:
                ret.append(end - start + 1)
                start = end + 1

        return ret

