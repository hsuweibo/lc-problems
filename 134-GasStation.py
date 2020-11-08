import unittest

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # The accumulated gas shortage
        shortage = 0
        # The starting gas station. Initialize to index 0
        starting = 0
        # Record how much fuel is in the gas tank currently
        curr_tank = 0

        # Starting from station 0, iterate through each station.
        # At each station (i), we see if we can make it to the next station (i+1). If curr_tank >= 0, then yes, otherwise no.
        # If we can't make it to the next station, then we know the current starting gas station can't be correct.
        # So we let the next station (i+1) to be the next possible starting point.
        # We also add the missing fuel amount (-curr_tank) to shortage.
        # -curr_tank represents the amount of extra fuel we need to get from the starting point to the next station.
        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                shortage += -curr_tank
                curr_tank = 0
                if i + 1 == len(gas):
                    starting = 0
                else:
                    starting = i + 1

        # Once we have iterated through all stations, it must be that
        # starting->...->station 0 is a valid path, with a surplus of curr_tank amount of fuel.
        # (starting could be 0, in which case curr_tank is 0).
        # Now we see if that surplus is able to power the accumulated shortage from before.
        if curr_tank >= shortage:
            return starting
        else:
            return -1


class TestCircuit(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]), 3)

    def test_input1(self):
        self.assertEqual(self.sol.canCompleteCircuit([2, 3, 4], [3,4,3]), -1)


if __name__ == '__main__':
    unittest.main()