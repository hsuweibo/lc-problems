
import unittest
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or len(s) == 0:
            return 0

        # keep tracks of the frequency of each char in the current window
        window_freq = defaultdict(int)

        # number of uniq characters in the window
        window_size = 0

        left, right = 0, 0
        answer = 0

        # Keep moving right until we see k + 1 distinct chars, at which point,
        # we start moving the left pointer until there is only k distinct characters.
        while right < len(s):
            rc = s[right]
            if window_freq[rc] == 0:
                window_size += 1
            window_freq[rc] += 1

            if window_size == k + 1:
                answer = max(right - left, answer)
                while window_size == k + 1:
                    lc = s[left]
                    window_freq[lc] -= 1
                    if window_freq[lc] == 0:
                        window_size -= 1

                    left += 1
            right += 1

        answer = max(right - left, answer)

        return answer


class TestSolution(unittest.TestCase):
    def test_input1(self):
        # ddefddf is the longest substr
        self.assertEqual(Solution().lengthOfLongestSubstringKDistinct("aabcddefddfc", 3), 7)

    def test_input2(self):
        self.assertEqual(Solution().lengthOfLongestSubstringKDistinct("abbbcc", 2), 5)

    def test_input3(self):
        self.assertEqual(Solution().lengthOfLongestSubstringKDistinct("aaa", 2), 3)


if __name__ == '__main__':
    unittest.main()
