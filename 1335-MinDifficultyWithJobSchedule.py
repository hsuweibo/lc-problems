import unittest

class Solution:
    def minDifficulty(self, jobDifficulty, num_days: int) -> int:
        num_jobs = len(jobDifficulty)
        dp = [[-1 for j in range(num_days)] for i in range(num_jobs)]
        dp[0][0] = jobDifficulty[0]

        for job in range(1, num_jobs):
            for day in range(min(job + 1, num_days)):
                if day == 0:
                    dp[job][day] = max(dp[job - 1][day], jobDifficulty[job])
                else:
                    first_job_today = job
                    day_j_diff = jobDifficulty[first_job_today]
                    while first_job_today >= day:
                        day_j_diff = max(day_j_diff, jobDifficulty[first_job_today])
                        if dp[job][day] == -1:
                            dp[job][day] = day_j_diff + dp[first_job_today - 1][day - 1]
                        else:
                            dp[job][day] = min(day_j_diff + dp[first_job_today - 1][day - 1], dp[job][day])
                        first_job_today -= 1
        return dp[-1][-1]


class TestSolution(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(Solution().minDifficulty([11,111,22,222,33,333,44,444],  6), 843)

    def test_input2(self):
        self.assertEqual(Solution().minDifficulty([6,5,4,3,2,1],  2), 7)

if __name__ == '__main__':
    unittest.main()