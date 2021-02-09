class Solution:
    def kClosest(self, points, K: int):
        def quick_select(lst, left, right):
            if right - left == 0:
                return lst[:right]

            piv = lst[right]
            i, j = left, left
            while j < right:
                if lst[j][0] * lst[j][0] + lst[j][1] * lst[j][1] < piv[0] * piv[0] + piv[1] * piv[1]:
                    lst[i], lst[j] = lst[j], lst[i]
                    i += 1
                j += 1

            lst[right], lst[i] = lst[i], lst[right]
            if i == K:
                return lst[:i]
            elif i < K:
                return quick_select(lst, i + 1, right)
            else:
                return quick_select(lst, left, i - 1)


        if K >= len(points):
            return points
        else:
            return quick_select(points, 0, len(points) - 1)


if __name__ == '__main__':
    Solution().kClosest([[1, 3], [-2, 2]], 1)