import unittest

class Solution(object):
    # dp solution, with |t|*|s| runtime
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dp[i][j] stores whether s[:i] is a subsequence of t[:j]
        dp = [[False for i in range(len(t) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False
        for i in range(1, len(t) + 1):
            dp[0][i] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if dp[i][j-1]:
                    dp[i][j] = True
                elif s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False

        return dp[-1][-1]

    # recursive solution, with 2^|t| worst case runtime
    def rec_isSubsequence(self, s, t):
        if s == '':
            return True
        elif len(t) < len(s):
            return False
        else:
            return (s[-1] == t[-1] and self.rec_isSubsequence(s[: -1], t[:-1])) or self.rec_isSubsequence(s, t[:-1])


class TestIsSubsequence(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_input1(self):
        self.assertTrue(self.solution.isSubsequence('abc', 'abcbcbccc'))

    def test_input2(self):
        self.assertFalse(self.solution.isSubsequence('abcbb', 'abbcbccc'))


if __name__ == "__main__":
    unittest.main()