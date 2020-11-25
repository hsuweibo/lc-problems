class Solution:
    # quadratic time and space algorithm
    def minFallingPathSum(self, arr) -> int:
        num_rows = len(arr)
        num_cols = len(arr[0])

        # dp[i][j] stores the minimum falling path sum starting from arr[i][j]
        dp = [[None for j in range(num_cols)] for i in range(num_rows)]
        dp[-1] = arr[-1]

        # left_min[i] stores the minimum path sum starting at the current/next row among all columns j < i.
        # right_min is similar. left_min[0] and right_min[-1] is always None
        left_min = [None for i in range(num_cols)]
        right_min = [None for i in range(num_cols)]

        for row in range(num_rows - 1, -1, -1):
            if row != num_rows - 1:
                for col in range(num_cols):
                    if col == 0:
                        dp[row][col] = right_min[col] + arr[row][col]
                    elif col == num_cols - 1:
                        dp[row][col] = left_min[col] + arr[row][col]
                    else:
                        dp[row][col] = min(left_min[col], right_min[col]) + arr[row][col]

            for col in range(1, num_cols):
                if col == 1:
                    left_min[col] = dp[row][col - 1]
                else:
                    left_min[col] = min(left_min[col - 1], dp[row][col - 1])

            right_min[-1] = None
            for col in range(num_cols - 2, -1, -1):
                if col == num_cols - 2:
                    right_min[col] = dp[row][col + 1]
                else:
                    right_min[col] = min(right_min[col + 1], dp[row][col + 1])

        return min(dp[0])