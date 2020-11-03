import unittest

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Sort the words according to length
        words.sort(key=len)
        # dp is a table mapping each word in words to the length of of a longest chain that ends at that word
        dp = dict()

        # for every word, try removing one char, and see if the resulting word is in the hashtable.
        # if yes, some previous chain can be extended.
        for w in words:
            max_chain_len = 0
            for i in range(len(w)):
                deleted = w[:i] + w[i+1:]
                if deleted in dp and dp[deleted] > max_chain_len:
                    max_chain_len = dp[deleted]
            dp[w] = max_chain_len + 1

        max_chain_len = 0
        for w in dp:
            if dp[w] > max_chain_len:
                max_chain_len = dp[w]
        return max_chain_len


class TestLongestStrChain(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_input1(self):
        self.assertEqual(self.solution.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]), 4)

    def test_input2(self):
        self.assertEqual(self.solution.longestStrChain(["acd", 'a', 'cd', 'ac', 'cde']), 3)

    def test_input_empty(self):
        self.assertEqual(self.solution.longestStrChain([]), 0)

    def test_input_single(self):
        self.assertEqual(self.solution.longestStrChain(['abc']), 1)


if __name__ == '__main__':
    unittest.main()