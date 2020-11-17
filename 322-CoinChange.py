import unittest


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        cache = dict()

        # a standard dp algorithm
        def coinChangeRec(coins, amount):
            if amount in cache:
                return cache[amount]
            if amount < 0:
                return -1
            if amount == 0:
                return 0

            min_so_far = None
            for c in coins:
                rec = coinChangeRec(coins, amount - c)
                if rec != -1:
                    if min_so_far is None or rec + 1 < min_so_far:
                        min_so_far = rec + 1

            if min_so_far is None:
                cache[amount] = -1
            else:
                cache[amount] = min_so_far
            return cache[amount]

        return coinChangeRec(coins, amount)


class TestCoins(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.coinChange([4, 5, 10, 2, 13], 24), 3)

    def test_input2(self):
        self.assertEqual(self.sol.coinChange([4, 5, 10], 27), 5)

    def test_input3(self):
        self.assertEqual(self.sol.coinChange([4, 5, 13], 28), 4)

    def test_input4(self):
        self.assertEqual(self.sol.coinChange([4, 5], 7), -1)

if __name__ == '__main__':
    unittest.main()
