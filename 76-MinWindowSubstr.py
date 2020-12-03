from collections import defaultdict
import unittest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = defaultdict(int)
        window_freq = defaultdict(int)

        for char in t:
            t_freq[char] += 1

        # The number of unique characters in t
        t_ctr = len(t_freq)

        # Store the left and right indices of the answer
        answer = None

        # The number of unique characters in the window s[left: right + 1] that appears in t,
        # and whose frequency in the window is higher than or equal to that in t.
        window_ctr = 0
        left = 0
        right = 0
        while right < len(s):
            rc = s[right]
            window_freq[rc] += 1

            # If the right character appears in t, and the addition of this char in the window satisfies the this char's frequency requirement
            if t_freq[rc] > 0 and window_freq[rc] == t_freq[rc]:
                window_ctr += 1

                # If these are equal, the current window contains all the chars in t
                if window_ctr == t_ctr:

                    # Push the left pointer to as right as possible, until there is at least one char in t not in window
                    while left <= right and window_ctr >= t_ctr:
                        lc = s[left]
                        window_freq[lc] -= 1

                        # If the left char appears in t, and reducing its freq in window makes its freq lower than its freq in t
                        if t_freq[lc] > 0 and window_freq[lc] + 1 == t_freq[lc]:
                            window_ctr -= 1

                            window_size = right - left + 1
                            if not answer or window_size < answer[1] - answer[0] + 1:
                                answer = (left, right)

                        left += 1
            right += 1

        if not answer:
            return ""
        else:
            return s[answer[0]: answer[1] + 1]

class TestMinWindowSubstr(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(Solution().minWindow('ADOBECODEBANC', 'ABC'), 'BANC')

    def test_input2(self):
        self.assertEqual(Solution().minWindow('CBBABCDACDCDBA', 'AAB'), 'ABCDA')

    def test_input3(self):
        self.assertEqual(Solution().minWindow("A", "AA"), "")


if __name__ == '__main__':
    unittest.main()