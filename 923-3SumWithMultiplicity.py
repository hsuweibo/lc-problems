import unittest

mod = 10 ** 9 + 7


class Solution:
    def threeSumMulti(self, arr, target: int) -> int:
        arr.sort()
        ret = 0
        for i in range(len(arr)):
            ret += self.countTwoSum(arr, i + 1, len(arr) - 1, target - arr[i]) % mod
            ret %= mod
        return ret

    def countTwoSum(self, arr, start, end, target):
        cnt = 0
        left, right = start, end
        while (left < right):
            if arr[left] + arr[right] == target:
                # Get number of elements within the range, and calculate N choose 2
                if arr[left] == arr[right]:
                    range_size = (right - left + 1)
                    cnt += int(((range_size) * (range_size - 1) / 2) % mod)
                    cnt %= mod
                    return cnt
                else:
                    right_cnt = 0
                    right_anchor = arr[right]

                    while (arr[right] == right_anchor):
                        right_cnt += 1
                        right -= 1

                    left_cnt = 0
                    left_anchor = arr[left]
                    while (arr[left] == left_anchor):
                        left_cnt += 1
                        left += 1

                    cnt += (left_cnt * right_cnt) % mod
                    cnt %= mod
            elif arr[left] + arr[right] < target:
                left += 1
            else:
                right -= 1

        return cnt

class TestSolution(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(Solution().threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8), 20)

if __name__ == '__main__':
    unittest.main()