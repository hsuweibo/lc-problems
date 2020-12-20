import unittest


class Solution:
    # my solution (correct but less simpler)
    def my_firstMissingPositive(self, nums) -> int:
        # Use the given list as a hashset. Create a "present" marker.
        # For n from 1 to len(nums), if n is in the hashset, then nums[n-1] will be the present marker.
        present = -1
        seen_one = False

        # The answer can't be smaller than 1. Remove everything out of range by setting to one.
        # If there is no one, handle the special case separately
        for i in range(len(nums)):
            if nums[i] == 1:
                seen_one = True

            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = 1

        # If there is no ones in the original list, one is the answer
        if not seen_one:
            return 1

        # For each position that has not been already used as a hash bucket, do the following
        # Inspect the val at that position (set next to it), if that position has not already been used as a hashbucket,
        # Move current pointer to that position (set curr to next).
        # Then move next pointer to the position pointed to by the value at the current position,
        # before overwriting that value with the present marker.

        for i in range(len(nums)):
            if nums[i] != present:
                curr = i
                next = nums[curr] - 1
                while nums[next] != present:
                    curr = next
                    next = nums[next] - 1
                    nums[curr] = present

        # Now asks for n from 1 to len(nums) (incl.) if n is present in the hashset.
        for n in range(1, len(nums) + 1):
            if nums[n - 1] != present:
                return n

        # If all numbers from 1 to len(nums) is present, len(nums) + 1 is the answer.
        return len(nums) + 1

    def firstMissingPositive(self, nums) -> int:
        seen_one = False
        for i in range(len(nums)):
            if nums[i] == 1:
                seen_one = True

            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = 1

        if not seen_one:
            return 1

        # Use the negative sign to determine in a value is present.
        # For n from 1 to len(nums) - 1, nums[n] < 0 if n is present in the hash set.
        # nums[0] < 0 if len(nums) is present in the hash set
        for i in range(len(nums)):
            bucket = 0 if abs(nums[i]) == len(nums) else abs(nums[i])
            if nums[bucket] > 0:
                nums[bucket] = -nums[bucket]

        for n in range(1, len(nums) + 1):
            bucket = 0 if n == len(nums) else n
            if nums[bucket] > 0:
                return n
        return len(nums) + 1



class TestSolution(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(Solution().firstMissingPositive([2, 3, 5]), 1)

    def test_input2(self):
        self.assertEqual(Solution().firstMissingPositive([1, 2]), 3)

    def test_input3(self):
        self.assertEqual(Solution().firstMissingPositive([1, 5, 2, 1, 3, 5, 2]), 4)


if __name__ == '__main__':
    unittest.main()