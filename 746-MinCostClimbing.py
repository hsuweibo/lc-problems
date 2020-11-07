import unittest

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        # maintain the cost to the floor two and one step before curr
        cost_to_two_step = 0
        cost_to_one_step = 0
        # start from floor 2 (index 2)
        for curr in range(2, len(cost) + 1):
            cost_to_curr = min(cost_to_two_step + cost[curr - 2], cost_to_one_step + cost[curr - 1])
            cost_to_two_step = cost_to_one_step
            cost_to_one_step = cost_to_curr

        return cost_to_one_step



class TestMinCost(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_input1(self):
        self.assertEqual(self.solution.minCostClimbingStairs([10, 15, 20]), 15)

    def test_input2(self):
        self.assertEqual(self.solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    def test_input3(self):
        self.assertEqual(self.solution.minCostClimbingStairs([2, 1, 4, 7, 1]), 6)


if __name__ == '__main__':
    unittest.main()