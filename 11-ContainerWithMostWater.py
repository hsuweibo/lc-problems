import unittest

class Solution:
    # A two-pointer, greedy algorithm
    def maxArea(self, array):
        max_so_far = -1
        left = 0
        right = len(array) - 1

        # Start at the first and last bars and try to find larger area by shrinking the width incrementally
        # At any point, we could move the left or right pointer inwards.

        # However, if the left bar is the bottleneck for the height of the rectangle,
        # moving the right pointer inward will never result in a larger area.
        # On the otherhand, moving the left ptr inward may or may not result in a larger rectangle.

        # Similarly, if the right bar is the bottleneck, there is no point of moving the left pointer.

        # So, we choose which pointers to move in a greedy approach: always move the pointer that is the bottleneck, and hope that
        # the incremental shrinking would eventually find the globally largest rectangle.

        # To show the algorithm would really find the globally largest rectangle, let l_opt, r_opt be the optimal left and right indices.
        # We need to show two cases.

        # We need to show if the right ptr reaches r_opt first, the right pointer won't move left until the left pointer hits l_opt.
        # And if the left ptr reaches l_opt first, the left pointer won't move right untill the right pointer hits r_opt.

        # Consider the first case. If the right pointer reaches r_opt, then it must be the left ptr < l_opt.
        # Furthermore, it must be array[left_ptr] < min(array[l_opt], array[r_opt]).
        # Why? because if not, l_opt and r_opt would not be the optimal indices.
        # Therefore, by the algorithm, the left pointer would be the bottleneck, and the one that moves inward before the right ptr does.
        while left < right:
            curr_area = (right - left) * min(array[left], array[right])
            if (curr_area > max_so_far):
                max_so_far = curr_area

            if (array[left] < array[right]):
                left += 1
            else:
                right -= 1

        return max_so_far


class TestContainer(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_input2(self):
        self.assertEqual(self.sol.maxArea([4, 3, 2, 1, 4]), 16)

    def test_input3(self):
        self.assertEqual(self.sol.maxArea([1, 2, 1]), 2)


if __name__ == '__main__':
    unittest.main()