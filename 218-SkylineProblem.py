
class Solution:
    def getSkyline(self, buildings):
        '''A divide and conquer solution'''
        if len(buildings) == 0:
            return []
        elif len(buildings) == 1:
            point1 = [buildings[0][0], buildings[0][2]]
            point2 = [buildings[0][1], 0]
            return [point1, point2]

        mid = len(buildings) // 2
        left_res = self.getSkyline(buildings[:mid])
        right_res = self.getSkyline(buildings[mid:])

        # l_ptr and r_ptr are next indices in the left_res and right_res
        # We also maintain l_y, which is the y-val/height of the last point we extract from left_res. r_y is similar.
        l_y = 0
        r_y = 0
        l_ptr = 0
        r_ptr = 0

        output = []

        while l_ptr < len(left_res) or r_ptr < len(right_res):
            # (curr_x, curr_y) is the next point we would potentially want to add to the output list
            if l_ptr == len(left_res):
                r_y = right_res[r_ptr][1]
                curr_x = right_res[r_ptr][0]
                curr_y = r_y
                r_ptr += 1
            elif r_ptr == len(right_res):
                l_y = left_res[l_ptr][1]
                curr_x = left_res[l_ptr][0]
                curr_y = l_y
                l_ptr += 1
            else:
                # We will get curr_x, the next smallest x-coordinate
                curr_x = min(right_res[r_ptr][0], left_res[l_ptr][0])

                # Depending on whether the point with the next smallest x-coordinate is from left_res or right_res,
                # Update the y-val and increment the pointer for the correspond side.
                if curr_x == left_res[l_ptr][0]:
                    l_y = left_res[l_ptr][1]
                    l_ptr += 1

                if curr_x == right_res[r_ptr][0]:
                    r_y = right_res[r_ptr][1]
                    r_ptr += 1

                curr_y = max(l_y, r_y)

            # Add to output if output is empty, or if it is not empty and the last point in output do not
            # share the same y-val.
            if len(output) == 0 or curr_y != output[-1][1]:
                output.append([curr_x, curr_y])

        return output


if __name__ == '__main__':
    Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])