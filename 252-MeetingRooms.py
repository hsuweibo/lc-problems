import unittest

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals = sorted(intervals, key=lambda i: i[0])
        i = 0
        busy_till = None
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            if i == 0:
                busy_till = end
            elif start < busy_till:
                return False

            busy_till = max(busy_till, end)
            i += 1
        return True



class TestRooms(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.canAttendMeetings([[15, 30], [20, 40], [5, 10], [12, 13]]), False)

    def test_input2(self):
        self.assertEqual(self.sol.canAttendMeetings([[20, 30], [10, 15], [35, 40], [55, 60]]), True)

    def test_empty(self):
        self.assertEqual(self.sol.canAttendMeetings([]), True)


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
