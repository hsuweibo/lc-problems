import unittest


 




class TestCombinationSum(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        output = self.sol.combinationSum3(3, 6)
        expected = [[1,2,3]]
        self.assertTrue(test_equal(output, expected))

    def test_input1(self):
        output = self.sol.combinationSum3(3, 12)
        expected = [[1, 9, 2], [1, 3, 8], [1, 4, 7], [1, 5, 6], [2, 3, 7], [2, 4, 6], [3, 4, 5]]
        self.assertTrue(test_equal(output, expected))

# test if two list of combinations are semantically equivalent
# e.g., [[1,2,3]] and [[3, 1, 2]] are equivalent
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


if __name__ == '__main__':
    unittest.main()