import unittest

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        # A custom comparator.
        # Given two numeric string s1 s2 that are not substrings of each other,
        # s1 > s2 iff at the first differing index i, s1[i] > s2[i].
        # If however, s1 is a substring of s2, then s1 > s2 iff s1 > s2[|s1|:]
        def cmp(s1, s2):
            i = 0
            while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
                i += 1
            if i == len(s1) and i == len(s2):
                return 0
            elif i == len(s1):
                return cmp(s1, s2[i:])
            elif i == len(s2):
                return cmp(s1[i:], s2)
            elif s1[i] > s2[i]:
                return 1
            else:
                return -1

        def cmp_to_key(mycmp):
            'Convert a cmp= function into a key= function'

            class K(object):
                def __init__(self, obj, *args):
                    self.obj = str(obj)

                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0

                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0

                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0

                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0

                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0

                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0

            return K

        sorted_nums = sorted(nums, key=cmp_to_key(cmp), reverse=True)
        ans = ""
        for n in sorted_nums:
            # a special edge case to not end up with strings like '00'
            if not (ans == '0' and n == 0):
                ans += str(n)

        return ans


class TestLargestNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_0string(self):
        self.assertEqual(self.sol.largestNumber([0, 0, 0]), '0')

    def test_input1(self):
        self.assertEqual(self.sol.largestNumber([3, 9, 64, 65, 656, 0]), '9656656430')

    def test_input2(self):
        self.assertEqual(self.sol.largestNumber([3, 30, 34, 5, 9]), '9534330')


if __name__ == '__main__':
    unittest.main()