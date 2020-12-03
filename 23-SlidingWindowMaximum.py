from collections import deque
import unittest

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        # on the deque, store indices of that contains the potential maximum for the current window
        # At any point, the window only contains indices whose value in nums is decreasing
        window = deque()
        right = 0
        answer = []
        while right < len(nums):
            left = right - k + 1
            # Remove indices that are now out of bound as a result of sliding window rightward
            while len(window) > 0 and window[0] < left:
                window.popleft()

            # from the right, remove any indices whose values are smaller than/equal to the current right end point
            # this way, the deque only contains indices with decreasing values in nums
            while len(window) > 0 and nums[window[-1]] <= nums[right]:
                window.pop()

            window.append(right)

            # by construction, the first element on the deque is always the index with maximum value
            if left >= 0:
                answer.append(nums[window[0]])
            right += 1
        return answer



class TestMaxSlidingWindow(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(Solution().maxSlidingWindow([3, 5, 4, 2, 5, 6, 4, 10], 3), [5, 5, 5, 6, 6, 10])

    def test_input2(self):
        self.assertEqual(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()