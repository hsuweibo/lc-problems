# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    # This is a pretty standard backtracking problem.
    # The catch is the board isn't given to us, so we have to maintain the position of the robot ourself.
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        DIR = ['up', 'right', 'down', 'left']

        # Given a position, and the direction the robot is currently facing, calculate the new pos after moving forward.
        def calc_pos_after_move(pos, direction):
            if direction == 'up':
                return (pos[0] - 1, pos[1])
            elif direction == 'right':
                return (pos[0], pos[1] + 1)
            elif direction == 'down':
                return (pos[0] + 1, pos[1])
            else:
                return (pos[0], pos[1] - 1)

        # pos is the current position of the robot. direction is the direction the robot is facing
        def backtrack(pos, direction):
            visited.add(pos)
            robot.clean()
            for num_right_turns in range(1, 5):
                robot.turnRight()
                new_direction = DIR[(DIR.index(direction) + num_right_turns) % 4]
                new_pos = calc_pos_after_move(pos, new_direction)

                # Check if the neighbor cell is valid (has not been visited before, and is not an obstacle)
                if new_pos not in visited and robot.move():
                    backtrack(new_pos, new_direction)

                    # Go back
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()

                    # Restore direction/orientation
                    robot.turnRight()
                    robot.turnRight()

            return

        # maintain the set of visited grid positions
        visited = set()

        # The robot is initially facing up at (0, 0)
        backtrack((0, 0), 'up')