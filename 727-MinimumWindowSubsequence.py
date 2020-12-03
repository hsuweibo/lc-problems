import unittest


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # represents a substr with inclusive end: S[start], S[start + 1], ..., S[end]
        class Pair:
            def __init__(self, start, end):
                self.start = start
                self.end = end

        # Given an index s_i in S, dp[j] would contain, if there exists one, a substring (a Pair object)
        # S[start], ..., S[end] of S[0], S[1], ..., S[s_i - 1] such that:
        # 1. T[0], T[1], ..., T[j-1], T[j] is a subsequence of S[start],... , S[end]
        # 2. S[start],... , S[end] is the one with the right-most end index (but still end <= s_i - 1)

        dp = [None] * len(T)

        # T[0], ..., T[progress-1] is the longest substr of T
        # for which we found a substring in S which T[0], ...,  T[progress - 1] is a subsequence of
        progress = 0

        # The current index in S
        s_i = 0

        answer = None

        # At the beginning of each iteration, we maintain the dp invariant listed above
        while s_i < len(S):
            s_ch = S[s_i]

            # We want to start matching s_ch with T[progress], then with T[progress - 1], ..., with T[0], and so on.
            # If progress = len(T), a substring which T is a subsequence of has been found already, but it may not be the shortest
            # So we start matching s_ch with T[len(T)], T[len(T) - 2], ... T[0] and so on.

            match_bound = min(len(T) - 1, progress)
            for match in range(match_bound, -1, -1):
                match_ch = T[match]
                if match_ch == s_ch:
                    if match == 0:
                        dp[match] = Pair(s_i, s_i)
                    else:
                        dp[match] = Pair(dp[match - 1].start, s_i)

            if progress < len(T) and s_ch == T[progress]:
                progress += 1

            if progress == len(T) and s_ch == T[-1]:
                # if the current char s_ch matches with last char of T, then dp[-1] contains
                # the most right-end substring of S upto current index of which T is a subsequence.
                # Now test to see if this is smaller than the one we have found before (if there is one)
                if not answer or dp[-1].end - dp[-1].start + 1 < answer.end - answer.start + 1:
                    answer = dp[-1]

            s_i += 1

        if not answer:
            return ""
        else:
            return S[answer.start: answer.end + 1]



class TestSolution(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(Solution().minWindow("abcdbde", 'bdde'), "bcdbde")

    def test_input2(self):
        self.assertEqual(Solution().minWindow("abcdebdde", 'bde'), "bcde")

    def test_input3(self):
        self.assertEqual(Solution().minWindow("ffynmlzesdshlvugsigobutgaetsnjlizvqjdpccdylclqcbghhixpjihximvhapymfkjxyyxfwvsfyctmhwmfjyjidnfryiyajmtakisaxwglwpqaxaicuprrvxybzdxunypzofhpclqiybgniqzsdeqwrdsfjyfkgmejxfqjkmukvgygafwokeoeglanevavyrpduigitmrimtaslzboauwbluvlfqquocxrzrbvvplsivujojscytmeyjolvvyzwizpuhejsdzkfwgqdbwinkxqypaphktonqwwanapouqyjdbptqfowhemsnsl", "ntimcimzah"), "nevavyrpduigitmrimtaslzboauwbluvlfqquocxrzrbvvplsivujojscytmeyjolvvyzwizpuhejsdzkfwgqdbwinkxqypaph")



if __name__ == '__main__':
    unittest.main()
