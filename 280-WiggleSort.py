import math
import unittest

class Solution:
    # linear time and space, my first solution
    def wiggleSort2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the median, and pick elements starting from the index 0 and the median, altering between the two.
        sorted_nums = sorted(nums)
        median = math.ceil(len(nums) / 2 - 1)
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = sorted_nums[i // 2]
            else:
                nums[i] = sorted_nums[median + 1 + i // 2]



    # linear time, constant space
    def wiggleSort3(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Sort the list, and swap adjacent element starting from the second element
        nums.sort()
        i = 1
        while i < len(nums) - 1:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2


    # linear time, constant space
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # At each index i, keep track of whether it should be the case nums[i] <= nums[i+1] (or nums[i] >= nums[i+1])
        # If the actual result is different from expected, do a swap.
        # This is a greedy strategy, and every swap guarantees that an index is fixed.
        # So when done, the entire list is fixed.
        i = 0
        less = True
        while i < len(nums) - 1:
            if less:
                if not (nums[i] <= nums[i+1]):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if not (nums[i] >= nums[i+1]):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            less = not less
            i += 1


class TestWiggle(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        l = [3,5,2,1,6,4]
        self.sol.wiggleSort(l)
        self.assertTrue(l, [1,4,2,5,3,6])

    def test_input2(self):
        l = [3,5,2,6,1,7,4]
        self.sol.wiggleSort(l)
        self.assertTrue(l, [3,5,2,6,1,7,4])


if __name__ == '__main__':
    unittest.main()