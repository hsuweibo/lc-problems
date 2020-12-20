class Solution:
    # The idea is to find the first index i where nums[i - 1] < nums[i].
    # now nums[i-1] would be the most significant digit we need to change. Change to what? we need to change it to the
    # first larger digit that occurs at an index after it.
    # Once we find it, swap them, then sort the segment starting from nums[i]
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 1
        # Maintain the invariant that at the beginning of each iteration, the segment nums[i+1] ... nums[-1] is descendingly sorted
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
            print(nums)

        # If i > 0, then nums[i-1] < nums[i]. Find the first index j in the segment nums[i], ..., nums[-1] where nums[i-1] >= nums[j]
        # Then swap nums[j-1] and nums[i-1]
        if i > 0:
            j = i
            while j < len(nums) and nums[i - 1] < nums[j]:
                j += 1

            nums[j - 1], nums[i - 1] = nums[i - 1], nums[j - 1]

        # Reverse the segment nums[i], ..., nums[-1] so that it goes from descending order to ascending order
        for k in range((len(nums) - i) // 2):
            nums[i + k], nums[-(k + 1)] = nums[-(k + 1)], nums[i + k]
