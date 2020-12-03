from collections import deque
import unittest

class Solution(object):
    # We need to maintain (get and update) the maximum and minimum in the current sliding window efficiently (O(1)).
    # Use the same idea as in 239-Sliding window maximum: use a deque
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        class Pair:
            def __init__(self, val, index):
                self.val = val
                self.index = index

        # window_max contains a sequence of pairs in the current window with increasing index and decreasing val
        # window_min is the same, except the pairs have increasing val
        window_min, window_max = deque(), deque()
        left, right = 0, 0
        answer = 0

        while right < len(nums):
            right_pair = Pair(nums[right], right)

            # remove the left most pair if it is now out of bound
            if len(window_max) > 0 and window_max[0].index < left:
                window_max.popleft()

            # To insert the right pair, go as left as possible, removing any pair with lesser values along the way
            # It might seem this is O(window_size), but I believe the overall algorithm is O(len(nums)).
            # Each comparison either removes a pair or add the right pair. Each pair only gets added or removed once.
            # Since there are len(nums) pairs, there are 2*len(nums) comparisons.
            while len(window_max) > 0 and window_max[-1].val <= right_pair.val:
                window_max.pop()
            window_max.append(right_pair)

            if len(window_min) > 0 and window_min[0].index < left:
                window_min.popleft()
            while len(window_min) > 0 and window_min[-1].val >= right_pair.val:
                window_min.pop()
            window_min.append(right_pair)

            if abs(window_max[0].val - window_min[0].val) > limit:
                left += 1
            else:
                answer = max(answer, right - left + 1)
                right += 1

        return answer




class TestSolution(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(Solution().longestSubarray([8, 2, 4, 7], 4), 2)

    def test_input2(self):
        self.assertEqual(Solution().longestSubarray([1, 2, 3], 0), 1)

    def test_input2(self):
        self.assertEqual(Solution().longestSubarray([1, 2, 3, 2, 5, 4, 6], 1), 3)


if __name__ == '__main__':
    unittest.main()