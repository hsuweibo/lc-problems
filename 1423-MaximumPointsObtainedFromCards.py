import unittest

class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        # Look for a maximum window sum of size k in the array formed by concatenating
        # the last k numbers in cardPoints, and first k numbers in cardPoints
        window_sum = 0

        # python will automatically handle negative indices
        start = -k
        end = k - 1

        left, right = start, start
        answer = -1

        while right <= end:
            window_sum += cardPoints[right]
            if right - left + 1 == k:
                answer = max(answer, window_sum)
                window_sum -= cardPoints[left]
                left += 1
            right += 1

        return answer


class TestSolution:
    def test_input1(self):
        self.assertEqual(Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3), 12)


if __name__ == '__main__':
    unittest.main()