import unittest


class Solution(object):
    # dp solution.
    # The key to this question is noticing that the water area at an index can be determined from its left and right max
    def trap(self, height):
        left_max = [0] * len(height)
        right_max = [0] * len(height)


        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
            right_max[len(height) - 1 - i] = max(right_max[len(height) - i], height[len(height) - i])

        area = 0
        for i in range(len(height)):
            wall_height = min(left_max[i], right_max[i])
            if wall_height > height[i]:
                area += wall_height - height[i]

        return area


    # my first solution
    def first_sol_trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0

        curr = 1
        highest = height[0]
        area = 0
        while curr < len(height):
            if height[curr] > height[curr - 1]:
                lower = min(highest, height[curr])
                prev = curr - 1
                while prev >= 0 and height[prev] < lower:
                    area += lower - height[prev]
                    height[prev] = lower
                    prev -= 1

            highest = max(highest, height[curr])
            curr += 1
        return area


class TestTrap(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_input1(self):
        self.assertEqual(self.solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

if __name__ == '__main__':
    unittest.main()