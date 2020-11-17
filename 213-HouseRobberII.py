class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        # Since the houses are arranged in a circle, we cant robbed the first and last house at the same time.
        # We either skip the first, and rob within the set nums[1] to nums[-1], or skip the last and rob from nums[0] to nums[-2]

        # Maintain two dp tables.
        # for 1 <= i < len(nums), dp_skip_first[i] represent the max profit by only considering houses in the range nums[1: i+1]
        # for 0 <= i < len(nums)-1, dp_skip_last[i] represent the max profit by only considering houses in the range nums[0: i+1]

        dp_skip_first = [0] * len(nums)
        dp_skip_last = [0] * len(nums)

        for i in range(len(nums) - 1):
            if i == 0:
                dp_skip_last[0] = nums[0]
            elif i == 1:
                dp_skip_last[1] = max(nums[0], nums[1])
            else:
                dp_skip_last[i] = max(nums[i] + dp_skip_last[i - 2], dp_skip_last[i - 1])

        for i in range(1, len(nums)):
            if i == 1:
                dp_skip_first[1] = nums[1]
            elif i == 2:
                dp_skip_first[2] = max(nums[1], nums[2])
            else:
                dp_skip_first[i] = max(nums[i] + dp_skip_first[i - 2], dp_skip_first[i - 1])

        return max(dp_skip_last[len(nums) - 2], dp_skip_first[len(nums) - 1])
