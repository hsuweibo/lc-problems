import unittest


class Solution:
    # A bruteforce DFS
    # n^2 time because we stop at each start index at most once, and at each start index, checking if prefix is in wd another O(|wd|).
    # (extracting the substring also takes linear time)
    def wordBreak(self, s, wordDict):
        def dfs(s, wd, visited, start):
            visited.add(start)

            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start: end] in wd and end not in visited:
                    if dfs(remaining, wd, visited, end):
                        return True
            return False

        # Stores the set of words that have been tried by their starting index.
        # So if i is in visited, s[i:] has been tried before.
        visited = set()
        return dfs(s, wordDict, visited, 0)

    # A DP approach
    def wordBreak(self, s: str, wd) -> bool:
        self.res = [False for i in range(len(s) + 1)]
        self.res[0] = True
        if len(wd) == 0:
            return False

        max_word_len = max([len(w) for w in wd])
        for r in range(1, len(s) + 1):
            start_index = max(0, r - max_word_len)
            for l in range(start_index, r):
                if s[l:r] in wd and self.res[l]:
                    self.res[r] = True
                    break

        return self.res[len(s)]


class TestWordBreak(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertTrue(self.sol.wordBreak('leetcode', ['leet', 'code']))

    def test_input2(self):
        self.assertTrue(self.sol.wordBreak('applepenapple', ['pen', 'apple']))

    def test_input3(self):
        self.assertFalse(self.sol.wordBreak('catsandog', ['cats', 'and', 'dog', 'cat', 'sand']))




if __name__ == '__main__':
    unittest.main()