class Solution:
    # top down recursive dp solution, with memoization
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]

        def helper(start, end):
            if start > end:
                return 0
            elif start == end:
                return 1
            else:
                if dp[start][end] != -1:
                    return dp[start][end]

                if s[start] == s[end]:
                    dp[start][end] = helper(start + 1, end - 1) + 2
                else:
                    dp[start][end] = max(helper(start + 1, end), helper(start, end - 1))

                return dp[start][end]

        return helper(0, len(s) - 1)

    # bottom up dp with tabulation
    def bot_longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] would store the longest palindromic subsequence in the substring s[i],...,s[j]
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        # loop through the diagonals in the table. Equivalent, loop through substrings of length 2, then length 3, and so on.
        # d is the difference of column-row
        for d in range(1, len(s)):
            r = 0
            while r + d < len(s):
                start, end = r, r + d

                if s[start] == s[end]:
                    dp[start][end] = 2 + (dp[start + 1][end - 1] if start + 1 <= end - 1 else 0)
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

                r += 1

        return dp[0][-1]
