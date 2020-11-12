import unittest

class Solution:
    def letterCombinations(self, digits: str):
        if digits == '':
            return []

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res = []

        # a standard backtrack DFS. s is the digit string.
        # start is the index of the next char in s to parse.
        # Curr is the current search progress (the string to be constructed).
        def backtrack(curr, start, s):
            if start == len(s):
                res.append(curr)
            else:
                for c in mapping[s[start]]:
                    backtrack(curr + c, start + 1, s)

        backtrack("", 0, digits)
        return res

class TestSol(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.letterCombinations('23'), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])



if __name__ == '__main__':
    unittest.main()
