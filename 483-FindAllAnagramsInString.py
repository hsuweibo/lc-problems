import unittest
from collections import Counter, defaultdict


class Solution(object):
    def findAnagrams(self, s, p):
        # Keep tracks of a mapping from char to freq in p and the current sliding window
        p_freq, window_freq = Counter(p), defaultdict(int)
        # p_ctr is the number of uniq char in p.
        # window_ctr is the number of uniq char in the window that appears in p and has the same freq as in p
        p_ctr, window_ctr = len(p_freq.keys()), 0
        left, right = 0, 0
        answer = []

        while right < len(s):
            rc = s[right]
            window_freq[rc] += 1
            if rc in p_freq and window_freq[rc] == p_freq[rc]:
                window_ctr += 1
            if right - left + 1 == len(p):
                if window_ctr == p_ctr:
                    answer.append(left)
                lc = s[left]
                window_freq[lc] -= 1
                if lc in p_freq and window_freq[lc] + 1 == p_freq[lc]:
                    window_ctr -= 1

                left += 1
            right += 1

        return answer


class TestFindAnagrams(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(Solution().findAnagrams('cbaebabacd', 'abc'), [0, 6])

    def test_input2(self):
        self.assertEqual(Solution().findAnagrams('bbacacaa', 'aac'), [2, 4, 5])

    def test_input3(self):
        self.assertEqual(Solution().findAnagrams('fffddabff', ''), [])

    def test_input4(self):
        self.assertEqual(Solution().findAnagrams('ffdbf', 'f'), [0, 1, 4])


if __name__ == '__main__':
    unittest.main()
