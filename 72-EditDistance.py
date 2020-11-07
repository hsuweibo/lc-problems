import unittest
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        ld = [[-1 for i in range(len2)] for j in range(len1)]
        for c2 in range(len2):
            ld[0][c2] = c2
        for c1 in range(len1):
            ld[c1][0] = c1

        for c1 in range(1, len1):
            for c2 in range(1, len2):
                left = ld[c1][c2-1]
                top = ld[c1-1][c2]
                top_left = ld[c1-1][c2-1]
                if word1[c1-1] == word2[c2-1]:
                    ld[c1][c2] = min(left + 1, top + 1, top_left)
                else:
                    ld[c1][c2] = min(left + 1, top + 1, top_left + 1)

        return ld[-1][-1]


class TestMinDistance(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_input1(self):
        self.assertEqual(self.solution.minDistance('horse', 'ros'), 3)
    def test_input2(self):
        self.assertEqual(self.solution.minDistance('ABCDE', 'BCDEE'), 2)


if __name__ == '__main__':
    unittest.main()