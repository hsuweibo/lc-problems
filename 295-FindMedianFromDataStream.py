from heapq import heappush, heappop
import unittest

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """

        # Maintain a left max heap, that contains the numbers in the first half (contains the first ceil(n/2) numbers)
        # The left min heap contains the numbers in the second half.
        # So if n is odd, the median is the first element of the left heap.
        # Otherwise, it is the average of the first elements of both heaps.
        self.left_max_heap = []
        self.right_min_heap = []
        self.n = 0

    def addNum(self, num: int) -> None:
        if self.n == 0:
            self.left_max_heap = [-num]
        else:
            # We first decide whether the number belongs in the right or left half, by comparing with the middle value.
            # Then depending on whether the size before the insertion was odd or even, we may need to move elements between
            # the two heaps in order to maintain the invariant (that the left heap contains first ceil(n/2) element)
            if num > -self.left_max_heap[0]:
                heappush(self.right_min_heap, num)
                if self.n % 2 == 0:
                    heappush(self.left_max_heap, -heappop(self.right_min_heap))
            else:
                heappush(self.left_max_heap, -num)
                if self.n % 2 == 1:
                    heappush(self.right_min_heap, -heappop(self.left_max_heap))

        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 1:
            return -self.left_max_heap[0]
        else:
            return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2


class TestMedianFinder(unittest.TestCase):
    def test_input1(self):
        mf = MedianFinder()
        mf.addNum(1)
        self.assertEqual(mf.findMedian(), 1)
        mf.addNum(2)
        self.assertEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertEqual(mf.findMedian(), 2)

    def test_input2(self):
        mf = MedianFinder()
        mf.addNum(-1)
        self.assertEqual(mf.findMedian(), -1)
        mf.addNum(-2)
        self.assertEqual(mf.findMedian(), -1.5)
        mf.addNum(-3)
        self.assertEqual(mf.findMedian(), -2)


if __name__ == '__main__':
    unittest.main()