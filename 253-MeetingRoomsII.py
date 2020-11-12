import heapq
import unittest


class Solution:
    # nlogn runtime.
    def minMeetingRooms(self, intervals) -> int:
        # sort by start time
        intervals = sorted(intervals, key=lambda i: i[0])
        # a minheap. each entry in the heap represent a room. The heap records the end time of each room.
        rooms = []
        i = 0
        # iterate through each time block.
        # For each, check if the start time is after the end time of the earliest to-be-available room.
        # If yes, update that room's end time (by popping and pushing the new endtime). Otherwise, a new room is needed.
        while i < len(intervals):
            end = intervals[i][1]
            start = intervals[i][0]

            if len(rooms) > 0 and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)

            i += 1

        return len(rooms)

    # quadratic runtime, my first solution
    def quadMinMeetingRooms(self, intervals) -> int:
        # sort by start time
        intervals = sorted(intervals, key=lambda i: i[0])
        # each entry in the list represent a room. The list records the end time of each room.
        rooms = []
        i = 0
        # iterate through each time block.
        # For each, check if the start time is after the end time of any of the previous room.
        # If yes, update that room's end time. Otherwise, a new room is needed.
        while i < len(intervals):
            end = intervals[i][1]
            start = intervals[i][0]

            found = False
            for r in range(len(rooms)):
                if rooms[r] <= start:
                    rooms[r] = end
                    found = True
                    break

            if not found:
                rooms += [end]

            i += 1

        return len(rooms)


class TestRooms(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.minMeetingRooms([[15, 30], [20, 40], [5, 10], [12, 13]]), 2)

    def test_input2(self):
        self.assertEqual(self.sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]), 2)

    def test_empty(self):
        self.assertEqual(self.sol.minMeetingRooms([]), 0)


if __name__ == '__main__':
    unittest.main()