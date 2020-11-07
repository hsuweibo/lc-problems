import unittest


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = [1] + nums + [1]
        # dp[i][j] stores the maximum coins for bursting balloons in the sublist nums[i:j+1],
        # where nums[i] and nums[j] represent the border 'unburstable' balloons
        dp = [[-1 for i in range(len(nums))] for j in range(len(nums))]

        def dp_rec(nums, left, right, dp):
            if left + 1 == right:
                return 0
            if dp[left][right] != -1:
                return dp[left][right]

            max_coins = 0
            # pick a balloon between the left and right boundary to be the LAST balloon to get burst.
            # when picking the last balloon to be bursted, the coin you get from the last balloon is that balloon's value times the boundary
            # bursting a balloon splits the list in half.
            # Recurse on each half, and the total coin is the maximal coin from each half plus the coin from the last bursted balloon.
            for i in range(left + 1, right):
                left_max_coins = dp_rec(nums, left, i, dp)
                right_max_coins = dp_rec(nums, i, right, dp)
                from_bursted_balloon = nums[i] * nums[left] * nums[right]
                max_coins = max(max_coins, from_bursted_balloon + left_max_coins + right_max_coins)
            dp[left][right] = max_coins
            return max_coins

        return dp_rec(nums, 0, len(nums) - 1, dp)


class TestMaxCoins(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_input1(self):
        self.assertEqual(self.solution.maxCoins([3,1,5,8]), 167)

if __name__ == '__main__':
    unittest.main()