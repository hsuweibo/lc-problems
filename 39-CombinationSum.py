import unittest

class Solution:
    def combinationSum(self, candidates, target: int):
        candidates.sort()
        cache = [[None for j in range(target + 1)] for i in range(len(candidates))]
        for val in range(target + 1):
            if val < candidates[0]:
                cache[0][val] = []
            elif val == candidates[0]:
                cache[0][val] = [[candidates[0]]]
            else:
                cache[0][val] = [(comb + [candidates[0]]) for comb in cache[0][val - candidates[0]]]

        for curr in range(1, len(candidates)):
            for val in range(target + 1):
                if val < candidates[curr]:
                    use_curr_coin = []
                elif val == candidates[curr]:
                    use_curr_coin = [[candidates[curr]]]
                else:
                    use_curr_coin = [(comb + [candidates[curr]]) for comb in cache[curr][val - candidates[curr]]]

                dont_use_curr_coin = cache[curr - 1][val]
                cache[curr][val] = use_curr_coin + dont_use_curr_coin

        return cache[-1][-1]


# test if two list of combinations are semantically equivalent
# e.g., [[1,2,2,2], [3, 5, 2, 1], [2, 2, 4, 1]] and [[2, 1, 2, 2], [4, 1, 2, 2], [5, 3, 2, 1]] are equivalent
def test_equal(list_a, list_b):
    # Given two sorted list, compare them lexicographically
    def compare_list(list_a, list_b):
        i = 0
        while i < len(list_a) and i < len(list_b) and list_a[i] == list_b[i]:
            i += 1

        if i < min(len(list_a), len(list_b)):
            if list_a[i] < list_b[i]:
                return -1
            else:
                return 1
        else:
            if len(list_a) == len(list_b):
                return 0
            elif len(list_a) < len(list_b):
                return -1
            else:
                return 1

    def cmp_to_key(mycmp):
        'Convert a cmp= function into a key= function'

        class K:
            def __init__(self, obj, *args):
                self.obj = obj

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

    if len(list_a) != len(list_b):
        return False

    for comb in list_a:
        comb.sort()
    for comb in list_b:
        comb.sort()

    list_a.sort(key=cmp_to_key(compare_list))
    list_b.sort(key=cmp_to_key(compare_list))

    i = 0
    while i < len(list_a) and list_a[i] == list_b[i]:
        i += 1

    return i == len(list_a)


class TestCombinationSum(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        output = self.sol.combinationSum([2, 3, 6, 7], 7)
        expected = [[2, 2, 3], [7]]
        self.assertTrue(test_equal(output, expected))

    def test_input2(self):
        output = self.sol.combinationSum([2, 3, 5], 8)
        expected = [[2, 2, 2, 2], [3, 3, 2], [5, 3]]
        self.assertTrue(test_equal(output, expected))

    def test_input3(self):
        output = self.sol.combinationSum([1, 2, 3], 5)
        expected = [[3, 2], [3, 1, 1], [1, 1, 1, 1, 1], [1, 2, 1, 1], [2, 2, 1]]
        self.assertTrue(test_equal(output, expected))


if __name__ == '__main__':
    unittest.main()

