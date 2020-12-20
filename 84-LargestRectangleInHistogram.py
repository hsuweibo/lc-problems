import unittest


class Solution:
    # The largest rectangle can be obtained by iterating over all height[i], finding heights[r] and heights[l],
    # where l < i and heights[l] is the first bar < heights[i], and r > i and height[r] is the first bar < heights[i],
    # then multiplying the height (h = height[i]) by the width (r - l - 1).
    # We could do this for every i, finding r and l, which takes quadratic time.

    # The stack base solution takes linear time. The idea is to maintain a stack of bar indices. For index j, stack[j]
    # would be an index of heights, and heights[stack[j-1]] would be the first shorter (or equal*) bar left to heights[stack[j]].
    # In otherwords, for all bar indices in the stack, those bars' left bar has been determined. And their right bar
    # is still currently in search.

    # *turns out this won't affect the algorithm

    # The way the invariant is maintained is as we iterate through heights,

    # if heights[curr] >= heights[stack[-1]], then for bar curr,
    # the first shorter (or equal) left bar is heights[stack[-1]].
    # Then we append curr to stack. Invariant is maintained.

    # if heights[curr] < heights[stack[-1]], then that means for all bars on the stack whose value > heights[curr],
    # their first shorter right bar is heights[curr], so we pop them off,
    # calculate the area, and update our answer. After popping them all off,
    # it should be that heights[stack[-1]] <= heights[curr], then we append curr to stack, so invariant is maintained.
    def largestRectangleArea(self, heights) -> int:
        # The -1 is there to ensure that the algorithm works when calculating the width
        stack = [-1]
        ans = 0
        curr = 0
        while curr < len(heights):
            # For the last few bars on the stack that all have values larger than the curr bar, we found their right bar
            while stack[-1] != -1 and heights[curr] < heights[stack[-1]]:
                i = stack.pop()
                h = heights[i]
                r = curr  # The (index of) first shorter bar to the right of bar i
                l = stack[-1]  # The (index of) first shorter bar to the left of bar i
                area = h * (r - l - 1)
                ans = max(area, ans)
            stack.append(curr)
            curr += 1

        # if after iteration, the stack is not empty, that means some bar does not have a first shorter right bar
        # i.e., the heights array might have a nondecreasing subarray towards the end. Set r to len(heights) in order
        # for the width calculation to work
        r = len(heights)
        while stack[-1] != -1:
            i = stack.pop()
            h = heights[i]
            l = stack[-1]
            area = h * (r - l - 1)
            ans = max(area, ans)

        return ans





class TestSolution(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(Solution().largestRectangleArea([5, 1, 6, 3, 5, 2]), 9)

    def test_input2(self):
        self.assertEqual(Solution().largestRectangleArea([6, 7, 5, 2, 4, 5, 9, 3]), 16)


if __name__ == '__main__':
    unittest.main()
