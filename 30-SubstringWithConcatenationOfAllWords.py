import unittest
from collections import Counter
from math import ceil


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # These are helper functions surrounding substrings based on positions
        # A substring at a position is a substring of s with length unit_len, offset by a starting index.
        # Positions starts at 0, and the substring at consecutive positions would be unit_len characters apart
        def get_word_at_pos(pos, start):
            return s[start + pos * unit_len: start + (pos + 1) * unit_len]

        def get_num_pos(start):
            return ceil((len(s) - start) / unit_len)

        def pos_to_index(pos, start):
            return start + pos * unit_len

        if len(words) == 0:
            return []
        unit_len = len(words[0])
        answer = []

        words_freq = Counter(words)
        words_ctr = len(words_freq)

        # The idea is to do a sliding window algorithm at each possible starting offset index
        for start in range(unit_len):
            window_freq = Counter()
            # number of words in window that appears in words and has freq higher than or equal to that in words
            window_ctr = 0

            # The left and right position, these get translated to indices using the helper functions
            left, right = 0, 0

            # If there is at least enough words remaining and the right pointer is inbound
            while get_num_pos(start) >= len(words) and right < get_num_pos(start):
                rw = get_word_at_pos(right, start)
                window_freq[rw] += 1
                if rw in words_freq and window_freq[rw] == words_freq[rw]:
                    window_ctr += 1

                # Once we get to the right window size, start sliding by pushing the left pointer to the right
                if right - left + 1 == len(words):
                    if window_ctr == words_ctr:
                        answer.append(pos_to_index(left, start))
                    lw = get_word_at_pos(left, start)
                    window_freq[lw] -= 1
                    if window_freq[lw] + 1 == words_freq[lw]:
                        window_ctr -= 1
                    left += 1
                right += 1

        return answer


class TestFindSubstr(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(sorted(Solution().findSubstring('barfoothefoobarman', ['foo', 'bar'])), [0, 9])

    def test_input2(self):
        self.assertEqual(sorted(Solution().findSubstring('barfoothefoobarman', ['foo', 'bar', 'the'])), [0, 6])

    def test_input3(self):
        self.assertEqual(sorted(Solution().findSubstring('memymemema', ['me', 'my'])), [0, 2])

    def test_input4(self):
        self.assertEqual(sorted(Solution().findSubstring('meminememymine', ['me'])), [0, 6])

    def test_input5(self):
        self.assertEqual(sorted(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",
                                                         ["fooo", "barr", "wing", "ding", "wing"])), [13])

    def test_input6(self):
        self.assertEqual(sorted(Solution().findSubstring("aaaaaaaaaaaaaa",
                                                         ["aa", "aa"])), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()
