import random


class Solution:
    def __init__(self, w):
        self.prefix_sum = []
        self.total_sum = 0
        for num in w:
            self.total_sum += num
            self.prefix_sum.append(self.total_sum)

    def pickIndex(self) -> int:
        # Given a val, and a sorted list,
        # return the index that contains the smallest number strictly greater than val.
        def bin_search(lst, val):
            left = 0
            right = len(lst) - 1
            while left <= right:
                mid = (left + right) // 2
                if lst[mid] > val:
                    right = mid - 1
                else:
                    left = mid + 1

            return right + 1

        # Roll a random value between 0 and the total sum,
        # then use binary search to find the index this random value falls into
        val = random.random() * self.total_sum
        return bin_search(self.prefix_sum, val)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()